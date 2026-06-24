import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 1. Extract all paragraph text
all_paragraphs = soup.find_all("p")
for p in all_paragraphs:
    print(p.text)

# 2. Extract all URLs and link text
all_links = soup.find_all("a")
for link in all_links:
    print(link.get("href"))
    print(link.text)

# 3. Extract prices using class selection
prices = soup.find_all("p", class_="price_color")
for price in prices:
    print(price.text)

# 4. Extract individual book details by looping over product cards
products = soup.find_all("article", class_="product_pod")

for product in products:
    title = product.find("h3").find("a").get("title")
    price = product.find("p", class_="price_color").text

    # Safely extract the secondary class (the rating word) from the class list
    rating_classes = product.find("p", class_="star-rating").get("class")
    rating = rating_classes[1] if len(rating_classes) > 1 else "No Rating"

    print(f"Title: {title}")
    print(f"Price: {price}")
    print(f"Rating: {rating}")
    print("---")
#css selectors
# Select all <p> tags with class 'price_color'
prices = soup.select('p.price_color')

# Select element with id 'featured'
featured = soup.select('#featured')

# Select all <a> tags that are inside <h3> tags
titles = soup.select('h3 > a')

# Select all <li> items inside a <ul> with class 'breadcrumb'
breadcrumbs = soup.select('ul.breadcrumb li')
