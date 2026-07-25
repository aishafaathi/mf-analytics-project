import requests
import pandas as pd

# API URL
url = "https://api.mfapi.in/mf/125497"

# Send GET request
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    data = response.json()

    # Print scheme name
    print("Scheme Name:")
    print(data["meta"]["scheme_name"])

    # Convert NAV history to DataFrame
    df = pd.DataFrame(data["data"])

    print("\nFirst 5 Rows:")
    print(df.head())

    # Save to CSV
    df.to_csv("data/raw/HDFC_Top100_Live_NAV.csv", index=False)

    print("\n✅ CSV saved successfully!")

else:
    print(f"Error: {response.status_code}")