import streamlit as st
import pandas as pd
import numpy as np

# Line chart
data = pd.DataFrame({'scores': [55, 72, 68, 88, 91, 79, 95]}, index=range(7))
st.line_chart(data)

# Bar chart
subjects = pd.DataFrame({
    'Marks': [88, 76, 92, 70, 85]},
    index=['Maths', 'English', 'Science', 'Hindi', 'Art']
)
st.bar_chart(subjects)

# Area chart
st.area_chart(data)

# For advanced charts use plotly (pip install plotly):
import plotly.express as px
fig = px.pie(values=[30, 20, 50], names=['A', 'B', 'C'])
st.plotly_chart(fig)

#colums and expanders
# Columns — side by side layout
col1, col2 = st.columns(2)         # Two equal columns
col1, col2, col3 = st.columns([2, 1, 1])  # Different widths

with col1:
    st.header('Left Section')
    st.write('Content on the left')

with col2:
    st.header('Right Section')
    st.write('Content on the right')
# Expander — hide/show content
with st.expander('Click to see more details'):
    st.write('This hidden content appears when expanded!')
    st.code('print("Hidden code!")')

# Sidebar — a permanent side panel
st.sidebar.title('Menu')
option = st.sidebar.selectbox('Navigate', ['Home', 'About', 'Contact'])
st.sidebar.write(f'You selected: {option}')
import time

# Progress bar
progress = st.progress(0)
for i in range(100):
    time.sleep(0.01)       # Simulate work
    progress.progress(i + 1)
st.success('Done!')

# Spinner — shows while something is loading
with st.spinner('Loading data...'):
    time.sleep(2)          # Simulate slow task
st.success('Data loaded!')