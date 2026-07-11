# 🛍️ Online Retail Business Analytics Dashboard

An end-to-end data analytics and business intelligence application that cleans transaction data, stores it in a structured SQL database, and serves an interactive web dashboard for real-time performance tracking.

## 🚀 Live Demo
👉 **[Insert your Streamlit live link here once deployed]**

---

## 📊 Key Features
* **SQL Backend Infrastructure:** Converts raw transactional data into an optimized, local SQLite relational database for fast query execution.
* **Key Business KPIs:** Tracks total revenue, transaction counts, and unique customer acquisition metrics globally or filtered by country.
* **Interactive Data Visualization:** Displays dynamic monthly revenue trends and interactive product sales breakdowns via Plotly graphs.
* **Data Cleansing Pipeline:** Automatically filters out cancelled orders, adjustments, and negative or null transactional values to ensure metrics accuracy.

---

## 🛠️ Tech Stack & Libraries
* **Language:** Python
* **Database:** SQLite3 / SQL
* **Frontend UI:** Streamlit
* **Data Visualization:** Plotly Express
* **Data Manipulation:** Pandas

---

## 📂 Project Structure
```text
├── app.py                  # Streamlit frontend dashboard application code
├── retail_data.db          # Cleaned SQLite database containing the transaction tables
├── .gitignore              # Prevents large raw data files from being tracked by Git
└── README.md               # Project documentation and setup guide
