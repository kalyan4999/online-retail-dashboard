import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

st.set_page_config(layout="wide", page_title="Online Retail Analytics")
st.title("🛍️ Online Retail Business Dashboard")

# Connect to our local SQL database
conn = sqlite3.connect('retail_data.db')

# Sidebar Controls for dynamic filtering
st.sidebar.header("Filter Options")
countries = pd.read_sql("SELECT DISTINCT country FROM sales ORDER BY country;", conn)['country'].tolist()
selected_country = st.sidebar.selectbox("Select Country", ["All"] + countries)

# Build SQL query filters based on side panel choice
country_filter = "" if selected_country == "All" else f"WHERE country = '{selected_country}'"

# --- 1. Key Performance Indicators (KPIs) ---
metrics_query = f"""
SELECT 
    ROUND(SUM(quantity * price), 2) as revenue,
    COUNT(DISTINCT invoice) as transactions,
    COUNT(DISTINCT customer_id) as customers
FROM sales
{country_filter};
"""
metrics_df = pd.read_sql(metrics_query, conn)

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${metrics_df['revenue'].iloc[0]:,.2f}")
col2.metric("Total Transactions", f"{metrics_df['transactions'].iloc[0]:,}")
col3.metric("Unique Customers", f"{metrics_df['customers'].iloc[0]:,}")

# --- 2. Monthly Revenue Trend Line Chart ---
trend_query = f"""
SELECT 
    strftime('%Y-%m', invoice_date) as Month,
    ROUND(SUM(quantity * price), 2) as Revenue
FROM sales
{country_filter}
GROUP BY Month
ORDER BY Month;
"""
trend_df = pd.read_sql(trend_query, conn)

st.subheader("📈 Monthly Revenue Performance")
fig_trend = px.line(trend_df, x='Month', y='Revenue', markers=True, template="plotly_white")
st.plotly_chart(fig_trend, width="stretch")

# --- 3. Top Products Horizontal Bar Chart ---
product_filter = "WHERE description IS NOT NULL" if selected_country == "All" else f"WHERE description IS NOT NULL AND country = '{selected_country}'"
product_query = f"""
SELECT 
    description as Product,
    SUM(quantity) as UnitsSold
FROM sales
{product_filter}
GROUP BY Product
ORDER BY UnitsSold DESC
LIMIT 10;
"""
product_df = pd.read_sql(product_query, conn)

st.subheader("🏆 Top 10 Best Selling Products")
fig_prod = px.bar(product_df, x='UnitsSold', y='Product', orientation='h', template="plotly_white")
fig_prod.update_layout(yaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig_prod, width="stretch")

conn.close()
