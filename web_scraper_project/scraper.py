import requests
from bs4 import BeautifulSoup

url = "https://www.bid4assets.com/auction/index/1245119"
headers = {"User-Agent": "Mozilla/5.0"}  # pretend we are a browser

response = requests.get(url, headers=headers, timeout=10)
response.raise_for_status()  # stop if there is an error

soup = BeautifulSoup(response.text, "lxml")

def get_value_by_label(label_text):
    label = soup.find(string=lambda t: t and label_text in t)
    if not label:
        return None
    value = label.find_next()
    return value.get_text(strip=True) if value else None

data = {
    "Property Address": get_value_by_label("Address"),
    "Owner Name": get_value_by_label("Defendant"),
    "Amount Owed": get_value_by_label("Debt Amount"),
    "Sale Amount": get_value_by_label("Winning Bid"),
    "Min. Bid": get_value_by_label("Minimum Bid"),
    "Sale Date": get_value_by_label("Auction Closed"),
    "Status": get_value_by_label("Your Bid Status")
}

for key, value in data.items():
    print(f"{key}: {value}")
