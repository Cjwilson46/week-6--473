# Python Standard Libraries
import requests
from urllib.parse import urljoin  # For resolving relative URLs

# Python 3rd Party Libraries
from bs4 import BeautifulSoup

# Target webpage URL
url = 'http://python.org/'

# Retrieve web-page
page = requests.get(url)
if page.status_code == 200:
    # Convert the page into a BeautifulSoup object for processing
    soup = BeautifulSoup(page.text, 'html.parser')

    # Extract and print the page title
    page_title = soup.title.string
    print(f'Page Title: {page_title}\n')

    # Extract and print all hyperlink URLs
    print('Page Links URLs:')
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        if href:
            # Resolve relative URLs to absolute URLs
            full_url = urljoin(url, href)
            print(full_url)
    print()

    # Extract and print all images and their URLs
    print('Images Found on the Page:')
    images = soup.find_all('img')
    for image in images:
        src = image.get('src')
        if src:
            # Resolve relative image src to absolute URLs
            img_url = urljoin(url, src)
            print(img_url, '-', image.get('alt', 'No alt text provided'))
    print()

    print('End Script')
else:
    print('Failed to retrieve the webpage')
