from flask import Flask, redirect, request, render_template, url_for, flash

# Instantiate Flask application
app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necessary for flash messages

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation: List all transactions
@app.route("/")
def get_transactions():
    total = sum(t['amount'] for t in transactions)  # Calculate total balance
    return render_template("transactions.html", transactions=transactions, total_balance=total)

# Create operation: Add a new transaction
@app.route("/add", methods=["GET", "POST"])
def add_transaction():
    if request.method == 'POST':
        try:
            # Validate the inputs
            date = request.form['date']
            amount = float(request.form['amount'])
            transaction = {
                'id': len(transactions) + 1,
                'date': date,
                'amount': amount
            }
            transactions.append(transaction)
            flash("Transaction added successfully!", "success")
            return redirect(url_for("get_transactions"))
        except ValueError:
            flash("Invalid input: Amount must be a number.", "danger")
            return render_template("form.html")

    return render_template("form.html")

# Update operation: Edit an existing transaction
@app.route("/edit/<int:transaction_id>", methods=["GET", "POST"])
def edit_transaction(transaction_id):
    transaction = next((t for t in transactions if t['id'] == transaction_id), None)
    if not transaction:
        flash("Transaction not found", "danger")
        return redirect(url_for("get_transactions"))

    if request.method == 'POST':
        try:
            transaction['date'] = request.form['date']
            transaction['amount'] = float(request.form['amount'])
            flash("Transaction updated successfully!", "success")
            return redirect(url_for("get_transactions"))
        except ValueError:
            flash("Invalid input: Amount must be a number.", "danger")

    return render_template("edit.html", transaction=transaction)

# Delete operation: Delete a transaction
@app.route("/delete/<int:transaction_id>", methods=["POST"])
def delete_transaction(transaction_id):
    transaction = next((t for t in transactions if t['id'] == transaction_id), None)
    if not transaction:
        flash("Transaction not found", "danger")
        return redirect(url_for("get_transactions"))

    transactions.remove(transaction)
    flash("Transaction deleted successfully!", "success")
    return redirect(url_for("get_transactions"))

# Exercise 1: Search Transactions
@app.route("/search", methods=["GET", "POST"])
def search_transactions():
    if request.method == 'POST':
        try:
            min_amount = float(request.form['min_amount'])
            max_amount = float(request.form['max_amount'])
            filtered_transactions = [t for t in transactions if min_amount <= t['amount'] <= max_amount]
            return render_template("transactions.html", transactions=filtered_transactions)
        except ValueError:
            flash("Invalid input: Amounts must be numbers.", "danger")
            return render_template("search.html")
    return render_template("search.html")

# Exercise 2: Total Balance
@app.route("/balance")
def total_balance():
    total = sum(t['amount'] for t in transactions)
    return f"Total Balance: {total}"

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
