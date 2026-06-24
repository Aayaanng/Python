import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the webpage
url = 'https://books.toscrape.com'
response = requests.get(url)

# Step 2: Check it worked
print(response.status_code)   # Should print 200

# Step 3: Parse the HTML
soup = BeautifulSoup(response.text, 'lxml')

# Step 4: Now soup is a Python object you can search!
print(soup.title)             # Prints the <title> tag
print(soup.title.text)        # Prints just the text inside <title
# book title scrape
import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# Find all book title elements
# Each book title is in an <h3> tag inside an <article> tag
books = soup.find_all('h3')

# Loop through and print each title
for book in books:
    title = book.find('a').get('title')   # The full title is in the 'title' attribute
    print(title)
