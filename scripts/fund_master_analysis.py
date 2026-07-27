print("Script started")

import pandas as pd

# Load the dataset
df = pd.read_csv("data/raw/01_fund_master.csv")

print("=" * 60)
print("FUND MASTER DATASET ANALYSIS")
print("=" * 60)

# Dataset size
print(f"\nRows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

# Column names
print("\nColumn Names:")
print(df.columns.tolist())

# Data types
print("\nData Types:")
print(df.dtypes)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# First five rows
print("\nFirst 5 Records:")
print(df.head())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe(include="all"))
print("\n" + "=" * 60)
print("BUSINESS INSIGHTS")
print("=" * 60)

# Number of Fund Houses
print("\nNumber of Fund Houses:")
print(df["fund_house"].nunique())

# List of Fund Houses
print("\nFund Houses:")
print(df["fund_house"].unique())

# Category-wise Count
print("\nCategory-wise Schemes:")
print(df["category"].value_counts())

# Risk Category Count
print("\nRisk Categories:")
print(df["risk_category"].value_counts())

# Top 10 Fund Managers
print("\nTop Fund Managers:")
print(df["fund_manager"].value_counts())

# Average Expense Ratio
print("\nAverage Expense Ratio:")
print(round(df["expense_ratio_pct"].mean(), 2), "%")

# Highest Expense Ratio
highest = df.loc[df["expense_ratio_pct"].idxmax()]
print("\nHighest Expense Ratio Scheme:")
print(highest[["scheme_name", "expense_ratio_pct"]])

# Lowest Expense Ratio
lowest = df.loc[df["expense_ratio_pct"].idxmin()]
print("\nLowest Expense Ratio Scheme:")
print(lowest[["scheme_name", "expense_ratio_pct"]])