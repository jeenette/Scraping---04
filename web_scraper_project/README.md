Web Scraper Project: Surplus Funds Auction Data
Overview

This project demonstrates a hybrid web scraping pipeline using Selenium for browser automation and BeautifulSoup for HTML parsing. The goal is to extract structured auction data from public surplus funds listings, save it into a CSV file, and provide a foundation for further data analysis.

The scraper handles:

Parsing static HTML with BeautifulSoup.
Collecting dynamic data rendered by JavaScript (future Selenium integration).
Exporting structured data with timestamps for reproducibility.

Data points collected include:

Property Address
Owner Name
Amount Owed
Minimum Bid
Sale Date
Sales Amount
Status

PROJECT STRUCTURED
web_scraper_project/
├── data/
│   ├── raw/          # Unprocessed output from initial scrape
│   └── processed/    # Cleaned datasets ready for analysis
├── logs/             # Logs for script execution (future use)
├── src/
│   ├── __init__.py
│   ├── engine.py     # Selenium driver setup and navigation (future use)
│   ├── parser.py     # BeautifulSoup parsing functions
│   └── utils.py      # Helper functions (optional)
├── main.py           # Orchestrates scraping pipeline
├── scraper_test.py   # Requests + BeautifulSoup test scraper
├── requirements.txt  # Dependencies
└── README.md         # This file


Setup Instructions

1. Clone the repository and navigate to the project folder:

git clone https://github.com/jeenette/Scraping---04.git
cd web_scraper_project


2. Create a virtual environment and activate it:

python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

3. Install dependencies:

pip install -r requirements.txt

4. Run the test scraper (BeautifulSoup-only, no login required):

python scraper.py

This will:

Extract publicly available auction data.
Save results to data/raw/auction_test.csv.
Print the scraped data to the console.