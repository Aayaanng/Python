import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# Empty lists to store our data
titles  = []
prices  = []
ratings = []

# Find all book cards on the page
products = soup.find_all('article', class_='product_pod')

for product in products:
    title  = product.find('h3').find('a').get('title')
    price  = product.find('p', class_='price_color').text.strip()
    rating = product.find('p', class_='star-rating').get('class')[1]

    titles.append(title)
    prices.append(price)
    ratings.append(rating)

print(f'Scraped {len(titles)} books!')
#create dataframe
import pandas as pd

# Create a DataFrame from the lists
df = pd.DataFrame({
    'Title':  titles,
    'Price':  prices,
    'Rating': ratings
})

# View the first 5 rows
print(df.head())

# View shape (rows, columns)
print(df.shape)

# Basic stats
print(df.describe())
#clean and sort the data
# Remove the currency symbol and convert price to a float
# Strip away all characters except digits and decimal points
df["Price"] = df["Price"].str.replace(r"[^\d.]", "", regex=True).astype(float)


# Sort by price (cheapest first)
df_sorted = df.sort_values('Price')
print(df_sorted.head(10))

# Filter — only show 5-star rated books
five_star = df[df['Rating'] == 'Five']
print(five_star)

# Save to a CSV file
df.to_csv(r'C:\Users\aayaa\OneDrive\Desktop\rancholabs\Web Scraping\books_data.csv', index=False)
print('Data saved to books_data.csv!')