import pandas as pd

# Load NAV history data
df = pd.read_csv("data/raw/02_nav_history.csv")

print("=" * 60)
print("NAV HISTORY ANALYSIS")
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
print("NAV INSIGHTS")
print("=" * 60)

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Date range
print("\nDate Range:")
print("Start Date:", df["date"].min().date())
print("End Date:", df["date"].max().date())

# Number of schemes
print("\nNumber of Schemes:")
print(df["amfi_code"].nunique())

# Highest NAV recorded
highest = df.loc[df["nav"].idxmax()]
print("\nHighest NAV Recorded:")
print(highest)

# Lowest NAV recorded
lowest = df.loc[df["nav"].idxmin()]
print("\nLowest NAV Recorded:")
print(lowest)

# Latest NAV for each scheme
latest_nav = (
    df.sort_values("date")
      .groupby("amfi_code")
      .tail(1)
)

print("\nLatest NAV (First 10 Schemes):")
print(latest_nav[["amfi_code", "date", "nav"]].head(10))

# Average NAV by scheme
avg_nav = (
    df.groupby("amfi_code")["nav"]
      .mean()
      .sort_values(ascending=False)
)

print("\nTop 10 Average NAV:")
print(avg_nav.head(10))