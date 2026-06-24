import streamlit as st
import pandas as pd

st.title('Book Scraper Dashboard')
st.write('Data scraped from books.toscrape.com')

# Load the scraped data
df = pd.read_csv('C:\Users\aayaa\OneDrive\Desktop\rancholabs\Web Scraping\books_data.csv')

# --- SIDEBAR FILTERS ---
st.sidebar.header('Filter Books')

# Filter by rating
ratings = ['All'] + sorted(df['Rating'].unique().tolist())
selected_rating = st.sidebar.selectbox('Rating', ratings)

# Filter by max price
max_price = st.sidebar.slider('Max Price (£)', 0.0, float(df['Price'].max()), float(df['Price'].max()))

# Apply filters
filtered = df.copy()
if selected_rating != 'All':
    filtered = filtered[filtered['Rating'] == selected_rating]
filtered = filtered[filtered['Price'] <= max_price]

# --- DISPLAY ---
st.subheader(f'Showing {len(filtered)} books')
st.dataframe(filtered)

# --- CHART ---
st.subheader('Price Distribution')
st.bar_chart(filtered['Price'])

# --- STATS ---
st.subheader('Summary Statistics')
st.write(filtered.describe())
