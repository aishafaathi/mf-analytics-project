import pandas as pd
import os

# Folder containing all CSV files
data_folder = "data/raw"

# Get all CSV files
csv_files = [file for file in os.listdir(data_folder) if file.endswith(".csv")]

# Loop through each CSV
for file in csv_files:
    print("\n" + "=" * 60)
    print(f"Loading: {file}")
    print("=" * 60)

    file_path = os.path.join(data_folder, file)

    df = pd.read_csv(file_path)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())