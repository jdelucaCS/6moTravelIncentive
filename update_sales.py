import pandas as pd
import json
from datetime import datetime

# Load Excel data
df = pd.read_excel("sales_data.xlsx", engine="openpyxl")
df["Date"] = df["Date"].astype(str)
today = datetime.now().strftime("%Y-%m-%d")

# Find today's row
today_row = df[df["Date"] == today]

if not today_row.empty:
    goal = int(today_row["Goal"].values[0])
    actual = int(today_row["Actual"].values[0])

    # Load existing history
    with open("data/sales_history.json", "r") as f:
        history = json.load(f)

    # Avoid duplicates
    if not any(e["date"] == today for e in history):
        history.append({"date": today, "goal": goal, "actual": actual})
        with open("data/sales_history.json", "w") as f:
            json.dump(history, f, indent=2)
    else:
        print("Entry for today already exists.")
else:
    print("No data for today in Excel.")
