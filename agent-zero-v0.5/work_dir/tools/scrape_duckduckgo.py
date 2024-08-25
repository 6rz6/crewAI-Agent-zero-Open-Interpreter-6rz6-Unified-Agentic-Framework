import requests
from bs4 import BeautifulSoup

# URL to scrape
url = 'https://duckduckgo.com/?t=h_&q=paris+olimpics+results&ia=web'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all result items
results = soup.find_all('a', class_='result__a')

# Extracting title and URL for each result
scraped_results = [{'title': result.get_text(), 'link': result['href']} for result in results]

# Print the scraped results
for result in scraped_results:
    print(f"Title: {result['title']}\nLink: {result['link']}\n")
