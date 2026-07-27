import pandas as pd

# Load scheme performance data
df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("=" * 60)
print("SCHEME PERFORMANCE ANALYSIS")
print("=" * 60)

print(f"\nRows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())

print("\nFirst 5 Records:")
print(df.head())

print("\nSummary Statistics:")
print(df.describe(include="all"))
print("\n" + "=" * 60)
print("PERFORMANCE INSIGHTS")
print("=" * 60)

# Top 5 schemes by 5-Year Return
print("\nTop 5 Schemes by 5-Year Return:")
top5 = df.sort_values("return_5yr_pct", ascending=False)
print(top5[["scheme_name", "return_5yr_pct"]].head())

# Highest Sharpe Ratio
print("\nTop 5 Sharpe Ratios:")
print(
    df.sort_values("sharpe_ratio", ascending=False)[
        ["scheme_name", "sharpe_ratio"]
    ].head()
)

# Largest AUM
print("\nTop 5 Largest Funds by AUM:")
print(
    df.sort_values("aum_crore", ascending=False)[
        ["scheme_name", "aum_crore"]
    ].head()
)

# Highest Expense Ratio
print("\nTop 5 Highest Expense Ratios:")
print(
    df.sort_values("expense_ratio_pct", ascending=False)[
        ["scheme_name", "expense_ratio_pct"]
    ].head()
)

# Morningstar Ratings
print("\nMorningstar Rating Distribution:")
print(df["morningstar_rating"].value_counts().sort_index())

# Risk Grade Distribution
print("\nRisk Grade Distribution:")
print(df["risk_grade"].value_counts())