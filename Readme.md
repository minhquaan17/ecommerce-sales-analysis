# 📊 E-Commerce Sales Analytics (Python + Power BI)

## 📌 Overview
This project analyzes an E-commerce sales dataset to extract insights about revenue, product performance, and order behavior.

The workflow follows a typical Data Analyst pipeline:

**Raw Data → Data Cleaning (Python) → Processed Dataset → Dashboard (Power BI)**

---

## 🎯 Objectives
- Clean and preprocess raw sales data
- Perform feature engineering for analysis
- Analyze revenue trends and product performance
- Build an interactive dashboard

---

## 🛠️ Tech Stack
- Python (Pandas)
- Power BI

---

#📂 Project Structure
ecommerce-sales-analysis/
│
├── data/
│   ├── raw/                  # Raw dataset (Amazon Sale Report)
│   └── processed/            # Cleaned dataset
│       └── all_orders.csv
│
├── scripts/
│   └── pipeline.py           # Data cleaning & processing script
│
├── images/
│   └── dashboard.png         # Dashboard screenshot
│
├── requirements.txt          # Python dependencies
└── README.md


---

## ⚙️ Data Processing

### 🔹 Data Cleaning
- Remove missing values in `AMOUNT`
- Convert `DATE` to datetime format
- Standardize `STATUS` and `CATEGORY`
- Remove duplicate records

### 🔹 Feature Engineering
- `REVENUE = QTY × AMOUNT`
- Extract `MONTH` and `YEAR`
- Create `ORDER_TYPE`:
  - SALES
  - CANCEL
  - OTHER
- Create `ORDER_SIZE`:
  - SMALL
  - MEDIUM
  - LARGE
  - VIP

---

## 📊 Final Dataset

| Column        | Description |
|--------------|------------|
| ORDER ID     | Unique order identifier |
| DATE         | Transaction date |
| STATUS       | Raw order status |
| ORDER_TYPE   | Sales / Cancel classification |
| SKU          | Product ID |
| CATEGORY     | Product category |
| QTY          | Quantity |
| AMOUNT       | Unit price |
| REVENUE      | Total revenue |
| ORDER_SIZE   | Order segment |
| MONTH        | Month |
| YEAR         | Year |

---

## 📈 Dashboard

### 🔹 KPIs
- Total Revenue
- Total Orders
- Average Order Value (AOV)
- Cancel Rate

### 🔹 Visualizations
- Revenue Trend (Line Chart)
- Revenue by Category (Bar Chart)
- Top Products (SKU)
- Order Distribution

---

## 🔍 Key Insights
- Revenue is concentrated in a small number of SKUs
- Category distribution is uneven
- Cancelled orders negatively impact performance
- Revenue fluctuates over time (monthly trends)

---
