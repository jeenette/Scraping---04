# src/parser.py
from bs4 import BeautifulSoup

def parse_auction(html):
    soup = BeautifulSoup(html, "lxml")
    
    def get_value(label):
        td = soup.find("td", string=lambda t: t and label in t)
        if td:
            next_td = td.find_next_sibling("td")
            if next_td:
                return next_td.get_text(strip=True)
        return None
    
    return {
        "Property Address": get_value("Address"),
        "Owner Name": get_value("Defendant"),
        "Amount Owed": get_value("Debt Amount"),
        "Winning Bid": get_value("Winning Bid"),
        "Min. Bid": get_value("Minimum Bid"),
        "Sale Date": get_value("Auction Closed"),
        "Status": get_value("Status")
    }
