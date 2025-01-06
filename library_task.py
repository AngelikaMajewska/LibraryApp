from flask import Flask, render_template, request
from flask import redirect, url_for
import datetime

app = Flask(__name__)
import sqlite3

def connect_to_db():
    connection = sqlite3.connect('library.db')
    cursor = connection.cursor()
    return cursor, connection

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        cursor, connection = connect_to_db()
        cursor.execute("SELECT b.id, b.isbn,b.name,b.description,b.is_loaned,a.name, a.id FROM book b JOIN author a ON b.author_id = a.id ORDER BY a.name ;")
        connection.commit()
        my_books = cursor.fetchall()
        cursor.execute("SELECT id, name FROM author  ORDER BY id ASC;")
        connection.commit()
        authors = cursor.fetchall()
        connection.close()
        return render_template('book.html', data="abc", books=my_books, authors=authors)
    elif request.method == 'POST':
        isbn = request.form['isbn']
        title = request.form['title']
        description = request.form['desc']
        author_id = int(request.form['chosen_author'])

        for item in [int(isbn), title, description, int(author_id)]:
            if type(item) != str and type(item) != int:
                answer = "Data uncorrect, try again!"
                return render_template('book.html', data=None, answer=answer)
        cursor, connection = connect_to_db()
        cursor.execute("Select * from book")
        all_books = cursor.fetchall()
        for row in all_books:
            if isbn == row[1]:
                answer = "ISBN already in the database! Add different book."
                return render_template('book.html', data=None, answer=answer)
        cursor.execute("Select id from author;")
        connection.commit()
        all_authors = cursor.fetchall()
        author_ids = [int(row[0]) for row in all_authors]

        if author_id not in author_ids:
            answer = "Author not in the database! Add author first."
            return render_template('book.html', data=None, answer=answer)

        query = "INSERT INTO book(isbn,name, description, author_id) VALUES (?,?,?,?);"

        cursor.execute(query, (isbn, title, description, author_id))
        connection.commit()

        cursor.execute("SELECT id, name FROM author  ORDER BY id ASC;")
        connection.commit()
        authors = cursor.fetchall()
        cursor.execute(
            "SELECT b.id, b.isbn,b.name,b.description,b.is_loaned,a.name, a.id FROM book b JOIN author a ON b.author_id = a.id ORDER BY a.name ;")
        connection.commit()
        my_books = cursor.fetchall()
        connection.close()
        return render_template('book.html', books=my_books, data='abc', authors=authors)

@app.route('/book_details')
def book_details():
    book_id = request.args.get('id')
    cursor, connection = connect_to_db()
    query = "SELECT b.id, b.isbn, b.name, b.description, a.name, b.author_id FROM book b JOIN author a ON b.author_id = a.id WHERE b.id = ?;"
    cursor.execute(query, (book_id,))
    connection.commit()
    my_book = cursor.fetchone()
    connection.close()
    return render_template('book_details.html', book=my_book)

@app.route('/delete_book', methods=['GET', 'POST'])
def remove_book():
    if request.args.get('id'):
        book_id = request.args.get('id')
        cursor, connection = connect_to_db()
        query = "DELETE FROM book WHERE id = ?;"
        cursor.execute(query, (book_id,))
        connection.commit()
        connection.close()
        return redirect(url_for('books'))

@app.route('/clients' , methods=['GET', 'POST'])
def clients():
    if request.method == "GET":
        cursor, connection = connect_to_db()
        cursor.execute("SELECT * FROM client;")
        connection.commit()
        my_clients = cursor.fetchall()
        connection.close()
        return render_template('clients.html', clients=my_clients)
    elif request.method == "POST":
        first_name = request.form['first']
        last_name = request.form['last']
        cursor, connection = connect_to_db()
        query = "INSERT INTO client(first_name, last_name) VALUES (?,?);"
        cursor.execute(query, (first_name, last_name))
        connection.commit()
        cursor.execute("SELECT * FROM client;")
        my_clients = cursor.fetchall()
        connection.close()
        return render_template('clients.html', clients=my_clients)

@app.route('/delete_client', methods=['GET', 'POST'])
def remove_client():
    if request.args.get('id'):
        client_id = request.args.get('id')
        cursor, connection = connect_to_db()
        query = "DELETE FROM client_book WHERE client_id = ?;"
        cursor.execute(query, (client_id,))
        connection.commit()
        query = "DELETE FROM client WHERE id = ?;"
        cursor.execute(query, (client_id,))
        connection.commit()
        connection.close()
        return redirect(url_for('clients'))

@app.route('/client_details', methods=['GET', 'POST'])
def client_details():
    client_id = request.args.get('id')
    cursor, connection = connect_to_db()
    query = "SELECT cb.book_id,cb.loan_date, cb.return_date, b.name, c.first_name, c.last_name, c.id FROM client_book cb JOIN book b ON cb.book_id=b.id JOIN client c ON cb.client_id = c.id WHERE client_id = ? ORDER BY cb.return_date, cb.loan_date ASC;"
    cursor.execute(query,(client_id,))
    connection.commit()
    client_books = cursor.fetchall()
    if client_books:
        client = [client_books[0][6], client_books[0][4], client_books[0][5]]
        books = [[book[0], book[3], book[1], book[2]] for book in client_books]
    else:
        query = "SELECT id, first_name, last_name FROM client WHERE id = ?;"
        cursor.execute(query, (client_id,))
        connection.commit()
        client = cursor.fetchone()
        if client:
            books = None
        else:
            books = None
            client = None
    connection.close()
    return render_template('client_details.html', client=client, books=books, get=1)

@app.route('/loan', methods=['GET', 'POST'])
def loan():
    cursor, connection = connect_to_db()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM client ORDER BY id ASC;")
        connection.commit()
        clients = cursor.fetchall()
        cursor.execute("SELECT b.id, b.isbn, b.name, b.description, a.name FROM book b JOIN author a ON b.author_id = a.id WHERE b.is_loaned = False ORDER BY b.name;")
        connection.commit()
        books = cursor.fetchall()
        available = []
        for book in books:
            available.append(book)
        return render_template('loan.html', clients=clients, books=available)
    elif request.method == 'POST':
        book_id = request.form['chosen_book']
        client_id = request.form['chosen_client']
        date = datetime.datetime.today().strftime('%Y-%m-%d')
        query = f"INSERT INTO client_book(book_id, client_id, loan_date) VALUES (?,?,?);"
        cursor.execute(query, (book_id, client_id, date))
        connection.commit()
        query = "UPDATE book SET is_loaned = True WHERE id = ?;"
        cursor.execute(query, (book_id,))
        connection.commit()
        return redirect(url_for('loan'))
    connection.close()

@app.route('/return', methods=['GET', 'POST'])
def return_book():
    cursor, connection = connect_to_db()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM client ORDER BY id ASC;")
        connection.commit()
        clients = cursor.fetchall()
        cursor.execute(
            "SELECT cb.book_id, b.name,cb.loan_date, c.first_name, c.last_name FROM client_book cb JOIN book b ON b.id = cb.book_id JOIN client c ON cb.client_id = c.id WHERE b.is_loaned = True and cb.return_date IS NULL;")
        connection.commit()
        books = cursor.fetchall()
        loaned = []
        for book in books:
            loaned.append(book)
        return render_template('return.html', clients=clients, books=loaned)
    elif request.method == 'POST':
        book_id = request.form['chosen_book']
        client_id = request.form['chosen_client']
        query = "SELECT * FROM client_book WHERE return_date IS NULL and book_id = ? and client_id = ?;"
        cursor.execute(query, (book_id,client_id))
        connection.commit()
        client_books = cursor.fetchall()
        if client_books:
            date = datetime.datetime.today().strftime('%Y-%m-%d')
            query = "UPDATE client_book SET return_date = ? WHERE client_id = ? and book_id = ?;"
            cursor.execute(query, (date, client_id, book_id))
            connection.commit()
            query = "UPDATE book SET is_loaned = False WHERE id = ?;"
            cursor.execute(query, (book_id,))
            connection.commit()
            clients = None
            available = None
            answer = "Return successful!"
            return redirect(url_for('return_book'))
            # return render_template('return.html', clients=clients, books=available, answer=answer)
        else:
            clients = None
            available = None
            answer = "This client didn't loan this book!"
            return render_template('return.html', clients=clients, books=available, answer=answer)

    connection.close()

@app.route('/author', methods=['GET', 'POST'])
def author():
    cursor, connection = connect_to_db()
    cursor.execute("SELECT * FROM author;")
    connection.commit()
    authors = cursor.fetchall()
    connection.close()
    return render_template('authors.html', authors=authors)

@app.route('/delete_author', methods=['GET', 'POST'])
def remove_author():
    if request.args.get('id'):
        author_id = request.args.get('id')
        cursor, connection = connect_to_db()
        query = "SELECT id FROM book WHERE author_id = ?;"
        cursor.execute(query, (author_id,))
        connection.commit()
        query = "DELETE FROM book WHERE author_id = ?;"
        cursor.execute(query, (author_id,))
        connection.commit()
        query = "DELETE FROM author WHERE id = ?;"
        cursor.execute(query, (author_id,))
        connection.commit()
        connection.close()
        return redirect(url_for('author'))

@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    cursor, connection = connect_to_db()
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        query = "INSERT into author(name) VALUES (?);"
        cursor.execute(query, (full_name,))
        connection.commit()
        cursor.execute("SELECT * FROM author;")
        connection.commit()
        authors = cursor.fetchall()
        return render_template('authors.html', authors=authors)

@app.route('/author_details', methods=['GET', 'POST'])
def author_details():
    author_id = int(request.args.get('id'))
    cursor, connection = connect_to_db()
    query = "SELECT id, isbn, name, description FROM book WHERE author_id = ?"
    cursor.execute(query,(author_id,))
    connection.commit()
    author_books = cursor.fetchall()
    if author_books:
        books = [[book[0], book[3], book[1], book[2]] for book in author_books]
        return render_template('author_details.html', books=books, answer = None)
    else:
        answer = "Books for this author not found!"
        return render_template('author_details.html', answer = answer)


app.run(debug=True)