import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

url = "https://www.bid4assets.com/auction/index/1245119"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers, timeout=10)
response.raise_for_status()
soup = BeautifulSoup(response.text, "lxml")

def get_value_by_label(label_text):
    td = soup.find("td", string=lambda t: t and label_text in t)
    if td:
        next_td = td.find_next_sibling("td")
        if next_td:
            return next_td.get_text(strip=True)
    return None

# --- Step 1: Collect data ---
data = {
    "Property Address": get_value_by_label("Address"),
    "Owner Name": get_value_by_label("Defendant"),
    "Amount Owed": get_value_by_label("Debt Amount"),
    "Min. Bid": get_value_by_label("Minimum Bid"),
    "Sale Date": get_value_by_label("Auction Closed"),
}

# --- Step 2: Add timestamp and save CSV ---
data["scraped_at"] = datetime.now()
df = pd.DataFrame([data])
df.to_csv("data/raw/auction_test.csv", index=False)

# --- Step 3: Print to verify ---
for key, value in data.items():
    print(f"{key}: {value}")

print("Saved test CSV!")
