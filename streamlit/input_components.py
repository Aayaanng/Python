import streamlit as st

# Single line text input
name = st.text_input('What is your name?', placeholder='Type your name here...')

# Multi-line text area
feedback = st.text_area('Share your feedback:', height=150)

if name:
    st.write(f'Hello, {name}! Nice to meet you!')
if feedback:
    st.write(f'Thanks for your feedback!')
# Number input box
age = st.number_input('Enter your age:', min_value=1, max_value=120, value=10)
st.write(f'You are {age} years old!')

# Slider — drag to pick a value
score = st.slider('Pick a score:', min_value=0, max_value=100, value=50)
st.write(f'Score selected: {score}')

# Range slider — pick a range
price_range = st.slider('Price range (₹):', 0, 10000, (500, 5000))
st.write(f'Min: ₹{price_range[0]}  Max: ₹{price_range[1]}')
# Button — returns True when clicked
if st.button('Click Me! 🎉'):
    st.balloons()  # Fun celebration animation!
    st.success('You clicked the button!')

# Checkbox — returns True or False
show_info = st.checkbox('Show extra information')
if show_info:
    st.info('Here is the extra information you asked for!')

# Radio buttons — pick ONE option
favourite = st.radio('What is your favourite?', ['Python', 'JavaScript', 'Java', 'C++'])
st.write(f'You chose: {favourite}')
# Selectbox — dropdown, pick ONE option
city = st.selectbox('Choose your city:', ['Delhi', 'Mumbai', 'Bangalore', 'Chennai'])
st.write(f'Selected city: {city}')

# Multiselect — dropdown, pick MULTIPLE options
hobbies = st.multiselect('Choose your hobbies:',
    ['Reading', 'Gaming', 'Sports', 'Music', 'Coding', 'Art'])
st.write(f'Your hobbies: {hobbies}')

# Date picker
from datetime import date
birthday = st.date_input('When is your birthday?', date(2014, 1, 1))
st.write(f'Birthday: {birthday}')
