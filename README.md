# **Library Management System**

A web-based application for managing books, authors, clients, and loan transactions in a library. Built with Flask and SQLite, it offers functionality for adding, viewing, editing, and deleting records, as well as tracking book loans and returns.

---

## **Table of Contents**

- [About the Project](#about-the-project)  
- [Features](#features)  
- [Technologies Used](#technologies-used)  
- [Usage](#usage)  
- [Screenshots](#screenshots)  


---

## **About the Project**

The Library Management System simplifies the management of books, clients, authors, and loans.  
Key highlights include:  
- A user-friendly web interface for all operations.  
- Efficient SQLite database management.  
- Real-time updates to loan and return statuses.  

---

## **Features**

- **Books Management**: Add, view, and delete books.  
- **Authors Management**: Manage a list of authors and their details.  
- **Clients Management**: Maintain client records and loan histories.  
- **Loan and Return**: Loan/return books and track which books are available and loaned out.  
- **Dynamic Views**: View detailed information for books, authors, and clients.
- **Responsive Design**: The web application automatically adjusts its layout to fit various screen sizes, ensuring a seamless user experience on desktops, tablets, and mobile devices.


---

## **Technologies Used**

- **Backend**: Python (Flask Framework)  
- **Frontend**: HTML5, CSS3  
- **Database**: SQLite  
- **Template Engine**: Flask Jinja2  

---

## **Usage**

### Available Pages:  

1. **Homepage** (`/`)  
   - Navigate to the main page of the application.  

2. **Books Management** (`/books`)  
   - View all books in the library.  
   - Add new books with ISBN, title, description, and assign them to authors.  
   - Delete books from the library database.  

3. **Authors Management** (`/author`)  
   - View a list of all authors.  
   - Add new authors to the database.  
   - View details about authors and the books they have written.  
   - Delete authors (along with their associated books).  

4. **Clients Management** (`/clients`)  
   - Add new clients with their first and last names.  
   - View a list of all registered clients.  
   - Delete clients and their associated loan records.  

5. **Loan and Return Management**:  
   - **Loan Books** (`/loan`)  
     - View a list of available books and registered clients.  
     - Assign a book to a client with the current date as the loan date.  
   - **Return Books** (`/return`)  
     - Record the return of a loaned book and update its status to available.  

6. **Detailed Views**:  
   - **Book Details** (`/book_details`)  
     - View detailed information about a specific book, including its author.  
   - **Client Details** (`/client_details`)  
     - View a client's loan history and details about the books they have borrowed.  
   - **Author Details** (`/author_details`)  
     - View a list of books written by a specific author.  

### Responsive Design:

The application is built with responsive web design principles, meaning it adapts to different screen sizes. Whether you're using a desktop, tablet, or smartphone, the layout will adjust for optimal viewing and ease of use.

---

## **Screenshots**

### Homepage  
<img width="1438" alt="image" src="https://github.com/user-attachments/assets/222e1b41-195f-435b-896e-1f2736949eb8" />

### Books Management Page  
<img width="1438" alt="image" src="https://github.com/user-attachments/assets/e1e5c39b-f104-4f6f-97fc-31637b222d2a" />

### Books Details Page  
<img width="1357" alt="image" src="https://github.com/user-attachments/assets/5398bc02-f6ba-4d81-b028-960401595f21" />

### Authors Management Page  
<img width="1439" alt="image" src="https://github.com/user-attachments/assets/50f6860d-4b84-491c-ad51-d870d448363c" />

### Authors Details Page  
<img width="1359" alt="image" src="https://github.com/user-attachments/assets/57fa5218-030a-46fb-819d-26dc1d7bf473" />

### Clients Management Page  
<img width="1439" alt="image" src="https://github.com/user-attachments/assets/aaeae6b0-5469-4202-bcf2-26a5a846df30" />

### Clients Details Page  
<img width="1355" alt="image" src="https://github.com/user-attachments/assets/239010be-1a81-4f1d-b77d-d8434ebc844b" />

### Loan and Return Pages  
<img width="1437" alt="image" src="https://github.com/user-attachments/assets/d43325a6-603a-4f0a-ad81-308653897730" />

<img width="1438" alt="image" src="https://github.com/user-attachments/assets/b28842d1-f09c-407b-962b-2cb13b75c1c6" />

### Responsive Design based on Book Management Page

#### Regular size:
<img width="1438" alt="image" src="https://github.com/user-attachments/assets/e1e5c39b-f104-4f6f-97fc-31637b222d2a" />

#### Medium size:
<img width="700" alt="image" src="https://github.com/user-attachments/assets/8be0d6b2-4546-4e30-8d26-2624eda400d3" />

#### Small size:
<img width="450" alt="image" src="https://github.com/user-attachments/assets/288a080e-5bc4-4a4b-b82a-4b76c44e8177" />

