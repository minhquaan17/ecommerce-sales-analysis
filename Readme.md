# E-Commerce Sales Analytics (Python + Power BI)

## Overview
This project analyzes an E-commerce sales dataset to extract insights about revenue, product performance, and order behavior.

The workflow follows a typical Data Analyst pipeline:
Raw Data → Data Cleaning (Python) → Final Dataset → Dashboard (Power BI)

---

## Objectives
- Clean and preprocess raw sales data
- Create features for analysis
- Analyze revenue trends and product performance
- Build an interactive dashboard

---

## Tech Stack
- Python (Pandas)
- Power BI

---

## Project Structure
sales_analytics_project/

├── data/raw/                  # raw data  
├── output/all_orders.csv      # cleaned dataset  
├── scripts/pipeline.py        # data processing  
├── images/dashboard.png       # dashboard screenshot  
└── README.md  

---

## Data Processing

### Data Cleaning
- Remove missing values (AMOUNT)
- Convert DATE to datetime
- Standardize STATUS, CATEGORY
- Remove duplicates

### Feature Engineering
- REVENUE = QTY * AMOUNT
- Extract MONTH, YEAR
- Create ORDER_TYPE (SALES / CANCEL / OTHER)
- Create ORDER_SIZE (SMALL / MEDIUM / LARGE / VIP)

---

## Final Dataset

Columns used:

- ORDER ID → unique order
- DATE → transaction date
- STATUS → order status
- ORDER_TYPE → sales or cancel
- SKU → product id
- CATEGORY → product category
- QTY → quantity
- AMOUNT → price
- REVENUE → total revenue
- ORDER_SIZE → order segment
- MONTH, YEAR → time analysis

---

## Dashboard

### KPIs
- Total Revenue
- Total Orders
- Average Order Value (AOV)
- Cancel Rate

### Charts
- Revenue Trend (Line Chart)
- Revenue by Category (Bar Chart)
- Top 10 Products (SKU)
- Order Distribution

---

## Key Insights
- Revenue is concentrated in a small number of SKUs
- Category distribution is uneven
- Cancelled orders reduce overall performance
- Revenue fluctuates by month

---

## How to Run

python scripts/pipeline.py

---

## Demo
- Dashboard screenshot: images/dashboard.png
- (Add Power BI link here if available)

---

## Conclusion
This project demonstrates:
- Data cleaning and transformation
- Analytical thinking
- Data visualization and storytelling