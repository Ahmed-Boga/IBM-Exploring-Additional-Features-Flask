# IBM Exploring Additional Features in Flask

This repository contains a Flask-based web application to manage and analyze bank transactions. It demonstrates key CRUD (Create, Read, Update, Delete) operations, along with additional features like transaction search and total balance calculation.

---

## Project Structure

```bash
bash
Copy code
IBM-Exploring-Additional-Features-Flask/
│
├── app.py                        # Main Flask application
├── templates/                    # HTML templates for different pages
│   ├── transactions.html         # List transactions and balance
│   ├── edit.html                 # Edit transaction
│   ├── form.html                 # Add transaction
│   ├── search.html               # Search transactions
│
└── README.md                     # Project documentation

```

---

## Features

1. **Transaction Management**
    - View a list of all transactions with the total balance.
    - Add new transactions (income or expense).
    - Edit existing transactions.
    - Delete transactions.
2. **Search Transactions**
    
    Filter transactions by a specified range of amounts.
    
3. **Total Balance Display**
    
    Automatically calculates and displays the total balance from all transactions.
    
4. **User-Friendly Interface**
    
    Responsive and styled with Bootstrap for a clean user experience.
    

---

## Prerequisites

- Python 3.7+
- Flask
- Bootstrap (included via CDN in templates)

---

## Setup Instructions

1. **Clone the Repository**
    
    ```bash
    git clone https://github.com/your-repo/IBM-Exploring-Additional-Features-Flask.git
    cd IBM-Exploring-Additional-Features-Flask
    ```
    
2. **Install Dependencies**
    
    ```bash
    pip install flask
    ```
    
3. **Run the Application**
    
    ```bash
    python app.py
    ```
    
4. **Access the Application**
    
    Open a web browser and navigate to `http://127.0.0.1:5000`.
    

---

## Application Pages

1. **Home Page (Transaction List)**
    
    URL: `/`
    
    Displays all transactions along with their dates, amounts, and options to edit or delete.
    
2. **Add Transaction**
    
    URL: `/add`
    
    Allows users to add a new transaction (income or expense).
    
3. **Edit Transaction**
    
    URL: `/edit/<transaction_id>`
    
    Lets users modify details of an existing transaction.
    
4. **Search Transactions**
    
    URL: `/search`
    
    Provides a form to filter transactions within a specific amount range.
    
5. **Total Balance**
    
    URL: `/balance`
    
    Displays the cumulative balance of all transactions.
    

---

## Example Usage

### Adding a Transaction

1. Go to `/add`.
2. Fill in the date and amount.
3. Click "Add Transaction."

### Searching Transactions

1. Go to `/search`.
2. Enter the minimum and maximum amounts.
3. Click "Search."

---

## Contributing

1. Fork the repository.
2. Create a new branch for your changes.
3. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments

- **Flask**: Used for the backend server and routing.
- **Bootstrap**: Provides the responsive and polished UI styling.
- **Gradient Backgrounds**: Enhances visual appeal and user experience.

Enjoy managing your transactions! 😊
