from flask import Flask, render_template, request, redirect
import sqlite3
import psycopg2
import os

app = Flask(__name__)

IS_PRODUCTION = 'DATABASE_URL' in os.environ

# Connect to database
def get_db_connection():
    if IS_PRODUCTION:
        return psycopg2.connect(os.environ['DATABASE_URL'])
    else:
        conn = sqlite3.connect('expenses.db')
        conn.row_factory = sqlite3.Row
        return conn

# Home route
@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute('SELECT * FROM expenses ORDER BY date DESC, category ASC, amount DESC')
    expenses = cur.fetchall()

    cur.execute('SELECT category, SUM(amount) FROM expenses GROUP BY category')
    category_rows = cur.fetchall()
    category_data = {row[0]: row[1] for row in category_rows}

    cur.execute('SELECT SUM(amount) FROM expenses')
    total = cur.fetchone()[0] or 0

    cur.close()
    conn.close()

    return render_template(
        'index.html',
        expenses=expenses,
        total=total,
        category_data=category_data
    )

# Add expense
@app.route('/add', methods=['POST'])
def add_expense():
    amount = request.form['amount']
    description = request.form['description']
    category = request.form['category']
    date = request.form['date']

    conn = get_db_connection()
    cur = conn.cursor()

    if IS_PRODUCTION:
        cur.execute(
            'INSERT INTO expenses (amount, description, category, date) VALUES (%s, %s, %s, %s)',
            (amount, description, category, date)
        )
    else:
        cur.execute(
            'INSERT INTO expenses (amount, description, category, date) VALUES (?, ?, ?, ?)',
            (amount, description, category, date)
        )

    conn.commit()
    cur.close()
    conn.close()
    return redirect('/')

# Delete expense
@app.route('/delete/<int:id>')
def delete_expense(id):
    conn = get_db_connection()
    cur = conn.cursor()

    if IS_PRODUCTION:
        cur.execute('DELETE FROM expenses WHERE id = %s', (id,))
    else:
        cur.execute('DELETE FROM expenses WHERE id = ?', (id,))

    conn.commit()
    cur.close()
    conn.close()
    return redirect('/')

# Auto-create SQLite table if needed
if not IS_PRODUCTION and not os.path.exists('expenses.db'):
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
