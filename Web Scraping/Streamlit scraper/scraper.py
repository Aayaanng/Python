import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_books():
    url = 'https://books.toscrape.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    titles, prices, ratings = [], [], []

    for product in soup.find_all('article', class_='product_pod'):
        titles.append(product.find('h3').find('a').get('title'))
        prices.append(float(product.find('p', class_='price_color').text.replace('£','').strip()))
        ratings.append(product.find('p', class_='star-rating').get('class')[1])

    df = pd.DataFrame({'Title': titles, 'Price': prices, 'Rating': ratings})
    df.to_csv('books_data.csv', index=False)
    print('Scraping complete! Data saved.')
    return df

if __name__ == '__main__':
    scrape_books()
