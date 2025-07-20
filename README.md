# 💸 Spenny Lite — Personal Expense Tracker

Spenny Lite is a lightweight full-stack web app for tracking your personal expenses. It allows users to add, view, and delete expenses, view total spending, and see a breakdown by category with a pie chart.

Built with simplicity in mind, Spenny Lite is perfect as a learning project and a useful personal tool.

---

## 🚀 Live Demo

🌐 [spenny-lite.onrender.com](https://spenny-lite.onrender.com)

---

## 📸 Features

- ✅ Add expenses (amount, category, description, date)
- ✅ View all expenses in a table
- ✅ Delete expenses
- ✅ See total amount spent
- ✅ View spending breakdown by category (Chart.js)
- ✅ Responsive and clean UI

---

## 🧰 Tech Stack

| Layer        | Tech                       |
|--------------|----------------------------|
| Frontend     | HTML, CSS, Jinja2, Chart.js |
| Backend      | Python, Flask              |
| Database     | PostgreSQL (via psycopg2)  |
| Deployment   | Render.com                 |
| Version Control | Git + GitHub           |

---

## 📦 Installation (Local Setup)

1. **Clone the repo:**
   ```bash
   git clone https://github.com/your-username/spenny-lite.git
   cd spenny-lite
   ```

2. **Create a virtual environment & activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variable:**
   - Create a `.env` file in the root directory:
     ```
     DATABASE_URL=postgres://youruser:yourpass@host:port/dbname
     ```

5. **Run the app:**
   ```bash
   python app.py
   ```

6. **Open your browser** and visit:
   ```
   http://localhost:5000
   ```

---

## 🛠 Deployment (Render)

1. Push your project to GitHub.
2. Create a new **Web Service** on [Render.com](https://render.com).
3. Add the following **environment variable** in the Render dashboard:
   - `DATABASE_URL` = your PostgreSQL connection string
4. Set the following:
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `gunicorn app:app`

---

## 📊 Example Screenshot

<img width="1271" height="779" alt="image" src="https://github.com/user-attachments/assets/256a585e-ad41-4dfc-ab68-cd880526fe84" />


---

## 🧠 Why This Project?

Spenny Lite is a practical demonstration of:
- Full-stack web development with Flask
- CRUD operations and routing
- Dynamic HTML rendering with Jinja2
- Integration of data visualization with Chart.js
- PostgreSQL database interaction with psycopg2
- Real-world app structure useful for fintech projects and portfolios

---

## 📝 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute it.

---

## 👤 Author

**Tharshen Subramaniam**  
📫 [tharshen1823@gmail.com](mailto:tharshen1823@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/tharshensubramaniam/)
