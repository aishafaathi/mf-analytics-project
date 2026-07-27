# 📈 Mutual Fund Analytics Dashboard

An end-to-end Mutual Fund Analytics project developed using **Python, Pandas, SQLite, SQL, Plotly, and Streamlit**. This project analyzes mutual fund performance, risk, assets under management (AUM), expense ratios, and NAV trends through an interactive dashboard.

---

## 🚀 Project Overview

This project demonstrates a complete data analytics workflow:

- Data ingestion and preprocessing
- Exploratory Data Analysis (EDA)
- SQL database creation
- SQL queries and views
- Interactive Streamlit dashboard
- Data visualization and reporting

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- SQLite
- SQL
- Plotly
- Streamlit
- VS Code
- Git & GitHub

---

## 📂 Project Structure

```
mf-analytics-project/
│
├── dashboard/
│   ├── app.py
│   └── data/
│       ├── dashboard_dataset.csv
│       ├── latest_nav.csv
│       └── performance_summary.csv
│
├── data/
│   ├── raw/
│   └── processed/
│
├── database/
│   └── mutual_funds.db
│
├── scripts/
│   ├── fund_master_analysis.py
│   ├── nav_history_analysis.py
│   ├── performance_analysis.py
│   ├── load_to_sqlite.py
│   └── export_dashboard_data.py
│
├── sql/
│   ├── 01_basic_queries.sql
│   ├── 02_advanced_queries.sql
│   ├── 03_create_views.sql
│   └── 04_dashboard_queries.sql
│
├── reports/
│   └── screenshots/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 📊 Dashboard Features

- KPI Cards
  - Total Funds
  - Average 5-Year Return
  - Average Expense Ratio
  - Total Assets Under Management (AUM)

- Interactive Filters
  - Category
  - Fund House
  - Scheme Search

- Visualizations
  - Top 10 Funds by 5-Year Return
  - Risk Category Distribution
  - Fund House AUM Comparison

- Interactive Data Table

- Download Filtered Dataset

---

## 📈 Key Insights

- Analyzed **40 mutual fund schemes**.
- Compared equity and debt fund performance.
- Identified the top-performing funds based on 5-year returns.
- Evaluated risk categories and Morningstar ratings.
- Compared Assets Under Management (AUM) across fund houses.
- Created SQL views for dashboard-ready datasets.

---

## ▶️ How to Run the Project

### Clone the repository

```bash
git clone <your-github-repository-url>
cd mf-analytics-project
```

### Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Launch the dashboard

```bash
streamlit run dashboard/app.py
```

---

## 📸 Dashboard Screenshots

Add screenshots inside:

```
reports/screenshots/
```

Example:

- Dashboard Overview
- Performance Analysis
- Fund House Comparison
- Data Table

---

## 📌 Future Improvements

- Live NAV API integration
- Portfolio optimization analysis
- Mutual fund recommendation engine
- Predictive analytics using Machine Learning
- Streamlit Cloud deployment

---

## 👩‍💻 Author

**Aisha Faathihah Nalakath**

Mutual Fund Analytics Project

Built using Python, SQL, SQLite and Streamlit.