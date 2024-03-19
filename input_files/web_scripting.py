import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    """
    Scrape content from a website.

    Args:
        url (str): URL of the website.

    Returns:
        str: Scraped content.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Extract relevant information from the HTML...
    scraped_content = soup.title.text
    return scraped_content

website_url = "https://example.com"
content = scrape_website(website_url)
print(content)
