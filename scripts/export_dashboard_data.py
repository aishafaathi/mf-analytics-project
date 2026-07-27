import sqlite3
import pandas as pd
import os

# Create output folder if it doesn't exist
os.makedirs("dashboard/data", exist_ok=True)

# Connect to SQLite database
conn = sqlite3.connect("database/mutual_funds.db")

# Views to export
views = [
    "performance_summary",
    "latest_nav",
    "dashboard_dataset"
]

for view in views:
    print(f"Exporting {view}...")

    df = pd.read_sql(f"SELECT * FROM {view}", conn)

    output_path = f"dashboard/data/{view}.csv"
    df.to_csv(output_path, index=False)

print("\nDashboard datasets exported successfully!")

conn.close()