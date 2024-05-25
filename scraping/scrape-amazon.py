"""
A script to scrape Amazon for different categories of products
and save the data to S3.
"""

import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    # Modularize into an Airflow task DAG
    # https://www.amazon.com/s?k=beauty
    search_term = "beauty"
    url = f"https://www.amazon.com/s?k={search_term}"

    headers = {"User-Agent": "Mozilla/5.0", "Accept-Language": "en-US,en;q=0.5"}

    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, "html.parser")
        links = soup.find_all("a", {"class": "a-link-normal s-no-outline"})
        for link in links:
            full_link = f"https://www.amazon.com{link.get('href')}"
            # Dump the product page html into a file and save to S3
            # productTitle
            # productDescription
            # aboutthisitem
            # Save this data for a batch insertion
            # Fire off a Knowledge graph task which will process the data seperately
            # Run batch insertions at N intervals
