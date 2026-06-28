# Product Data Web Scraper

A robust web scraping pipeline built with Python and Scrapy to extract structured product data.

##  Key Features
- **Asynchronous Crawling:** Uses Scrapy for high-performance, non-blocking data extraction.
- **Data Integrity:** Implemented `AutoThrottle` and `robots.txt` compliance for ethical data collection.
- **Automation:** Handles pagination automatically to scrape entire product catalogs.
- **Scalable Design:** Structured with modular components for easy maintenance and expansion.

##  Tech Stack
- **Framework:** Python, Scrapy
- **Data Output:** JSON, CSV
- **Environment:** Virtualenv, Git

##  How to Run
1. Clone the repository: `git clone https://github.com/YOUR_USERNAME/product-data-scraper.git`
2. Install requirements: `pip install scrapy`
3. Run the spider: `scrapy crawl books -o output.json`