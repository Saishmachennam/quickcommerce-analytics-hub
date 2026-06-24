# QuickCommerce Analytics Hub

A comprehensive product analytics platform inspired by quick-commerce companies like Zepto, Blinkit, and Instamart. This project analyzes customer behavior, product performance, revenue trends, and retention metrics using Python, SQL, PostgreSQL, Tableau, and FastAPI.

## Project Overview

QuickCommerce Analytics Hub helps businesses understand:

* Revenue growth and sales trends
* Product and category performance
* Customer retention and repeat purchases
* Shopping basket behavior
* Business KPIs for data-driven decision making

The platform processes 50,000+ simulated transactions and generates actionable insights through analytics reports, dashboards, and API endpoints.

---

## Features

### Revenue Analytics

* Daily and monthly revenue tracking
* Revenue trend analysis
* Average order value calculation
* Revenue by category and city

### Product Analytics

* Top-selling products
* Category-wise sales performance
* Product contribution analysis
* Quantity sold tracking

### Customer Analytics

* Repeat purchase analysis
* Customer retention metrics
* Customer segmentation
* Purchase frequency tracking

### Basket Analysis

* Average basket size
* Product purchase patterns
* Frequently purchased items
* Order composition analysis

### Dashboard & Reporting

* Tableau-ready export datasets
* KPI summaries
* Revenue visualizations
* Business insight reports

### API Layer

* FastAPI-based analytics endpoints
* Revenue analytics API
* Retention metrics API
* Category performance API

---

## Tech Stack

| Component             | Technology          |
| --------------------- | ------------------- |
| Programming Language  | Python              |
| Database              | PostgreSQL          |
| Data Analysis         | Pandas, NumPy       |
| Visualization         | Tableau, Matplotlib |
| API Development       | FastAPI             |
| Database Connectivity | SQLAlchemy          |
| Data Generation       | Faker               |

---

## Project Architecture

```text
Customers
     ↓
Orders
     ↓
Order Items
     ↓
Python + SQL Analytics
     ↓
Business Insights Engine
     ↓
CSV Exports
     ↓
Tableau Dashboards
     ↓
FastAPI Endpoints
```

---

## Dataset

The project generates synthetic quick-commerce data consisting of:

| Dataset     | Records  |
| ----------- | -------- |
| Customers   | 5,000    |
| Products    | 20       |
| Orders      | 50,000   |
| Order Items | 150,000+ |

Product Categories:

* Fruits
* Vegetables
* Dairy
* Snacks
* Beverages

---

## Folder Structure

```text
QuickCommerce-Analytics-Hub/
│
├── api/
│   └── main.py
│
├── data/
│   ├── customers.csv
│   ├── products.csv
│   ├── orders.csv
│   └── order_items.csv
│
├── exports/
│   ├── revenue_summary.csv
│   ├── retention_metrics.csv
│   ├── category_performance.csv
│   ├── basket_analysis.csv
│   └── daily_sales.csv
│
├── notebooks/
│   └── product_analytics.ipynb
│
├── sql/
│   ├── schema.sql
│   ├── analytics_queries.sql
│   └── load_data.py
│
├── src/
│   ├── generate_data.py
│   ├── revenue_analysis.py
│   ├── category_analysis.py
│   ├── retention_analysis.py
│   ├── basket_analysis.py
│   ├── dashboard_exports.py
│   └── db.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/quickcommerce-analytics-hub.git

cd quickcommerce-analytics-hub
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Generate Dataset

```bash
cd src

python generate_data.py
```

Expected Output:

```text
Customers: 5000
Products: 20
Orders: 50000
Order Items: 150000+
```

---

## Run Analytics

```bash
python revenue_analysis.py

python category_analysis.py

python retention_analysis.py

python basket_analysis.py

python dashboard_exports.py
```

Generated Reports:

* Revenue Summary
* Category Performance
* Customer Retention Metrics
* Basket Analysis
* Dashboard Export Files

---

## Run FastAPI

```bash
uvicorn api.main:app --reload
```

Open Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Key Business Insights

* Analyze revenue growth across different time periods.
* Identify top-performing products and categories.
* Measure repeat purchase behavior and customer retention.
* Evaluate shopping basket size and purchasing patterns.
* Generate executive-level KPI reports.

---

## Sample KPIs

* Total Revenue
* Average Order Value
* Total Orders
* Repeat Purchase Rate
* Category Revenue
* Product Contribution
* Customer Retention Rate

---

## Future Enhancements

* Recommendation Engine
* Customer Segmentation using Machine Learning
* Real-Time Analytics Dashboard
* Inventory Analytics
* Predictive Sales Forecasting

---

## Resume Highlights

* Built a product analytics platform processing 50K+ quick-commerce transactions using Python, SQL, PostgreSQL, and Tableau.
* Performed customer retention, basket analysis, and category performance tracking to uncover business insights.
* Developed KPI dashboards and FastAPI-based analytics services for revenue monitoring and customer behavior analysis.

---

## Author

**Saishma Chennam**

B.Tech CSE | Data Analytics | Python | SQL | FastAPI | React Native
