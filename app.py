from flask import Flask, render_template, request, redirect
import sqlite3
import json

app = Flask(__name__)

# Connect to database
def get_db_connection():
    conn = sqlite3.connect('expenses.db')
    conn.row_factory = sqlite3.Row
    return conn

# Home route — shows all expenses
@app.route('/')
def index():
    conn = get_db_connection()
    expenses = conn.execute('SELECT * FROM expenses ORDER BY date').fetchall()

    # Fetch category totals
    category_rows = conn.execute(
    'SELECT category, SUM(amount) as total FROM expenses GROUP BY category'
    ).fetchall()

    category_data = {row['category']: row['total'] for row in category_rows}

    total = conn.execute('SELECT SUM(amount) FROM expenses ').fetchone()[0] or 0
    conn.close()
    return render_template(
        'index.html',
        expenses=expenses,
        total=total,
        category_data=category_data  # or use tojson in HTML
    )


# Handle form submission
@app.route('/add', methods=['POST'])
def add_expense():
    amount = request.form['amount']
    description = request.form['description']
    category = request.form['category']
    date = request.form['date']

    conn = get_db_connection()
    conn.execute(
        'INSERT INTO expenses (amount, description, category, date) VALUES (?, ?, ?, ?)',
        (amount, description, category, date)
    )
    conn.commit()
    conn.close()
    return redirect('/')

# Delete an expense
@app.route('/delete/<int:id>')
def delete_expense(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM expenses WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')

import os

if not os.path.exists('expenses.db'):
    conn = sqlite3.connect('expenses.db')
    conn.execute('''CREATE TABLE expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        description TEXT NOT NULL,
        category TEXT NOT NULL,
        date TEXT NOT NULL
    )''')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    app.run(debug=True)
