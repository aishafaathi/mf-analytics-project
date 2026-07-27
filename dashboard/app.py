import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Mutual Fund Analytics Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Mutual Fund Analytics Dashboard")
st.markdown("Interactive dashboard built using Python, SQLite, and Streamlit.")

# -----------------------------
# Load Data
# -----------------------------
df = pd.read_csv("dashboard/data/dashboard_dataset.csv")

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("Filters")

category = st.sidebar.selectbox(
    "Category",
    ["All"] + sorted(df["category"].unique().tolist())
)

fund_house = st.sidebar.selectbox(
    "Fund House",
    ["All"] + sorted(df["fund_house"].unique().tolist())
)

filtered_df = df.copy()

if category != "All":
    filtered_df = filtered_df[filtered_df["category"] == category]

if fund_house != "All":
    filtered_df = filtered_df[filtered_df["fund_house"] == fund_house]

# -----------------------------
# KPI Cards
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Funds", len(filtered_df))

col2.metric(
    "Average 5-Year Return",
    f"{filtered_df['return_5yr_pct'].mean():.2f}%"
)

col3.metric(
    "Average Expense Ratio",
    f"{filtered_df['expense_ratio_pct'].mean():.2f}%"
)

col4.metric(
    "Total AUM",
    f"{filtered_df['aum_crore'].sum():,.0f} Cr"
)

st.divider()

# -----------------------------
# Charts
# -----------------------------
left, right = st.columns(2)

with left:
    st.subheader("Top 10 Funds by 5-Year Return")

    top10 = filtered_df.nlargest(10, "return_5yr_pct")

    fig = px.bar(
        top10,
        x="return_5yr_pct",
        y="scheme_name",
        orientation="h"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader("Risk Category Distribution")

    fig = px.pie(
        filtered_df,
        names="risk_category"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("Fund House AUM")

aum = (
    filtered_df
    .groupby("fund_house")["aum_crore"]
    .sum()
    .reset_index()
)

fig = px.bar(
    aum,
    x="fund_house",
    y="aum_crore"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("Mutual Fund Details")

st.dataframe(filtered_df, use_container_width=True)