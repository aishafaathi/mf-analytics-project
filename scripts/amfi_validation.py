import pandas as pd

# Load Fund Master data
df = pd.read_csv("data/raw/01_fund_master.csv")

print("=" * 60)
print("AMFI CODE VALIDATION")
print("=" * 60)

# Check for duplicate AMFI codes
duplicates = df["amfi_code"].duplicated().sum()
print(f"\nDuplicate AMFI Codes: {duplicates}")

# Check for missing AMFI codes
missing = df["amfi_code"].isnull().sum()
print(f"Missing AMFI Codes: {missing}")

# Check if all AMFI codes are unique
if df["amfi_code"].is_unique:
    print("\n✅ All AMFI codes are unique.")
else:
    print("\n❌ Duplicate AMFI codes found.")

# Display sample codes
print("\nFirst 10 AMFI Codes:")
print(df["amfi_code"].head(10).tolist())

# Number of schemes per fund house
print("\nSchemes by Fund House:")
print(df.groupby("fund_house")["scheme_name"].count().sort_values(ascending=False))