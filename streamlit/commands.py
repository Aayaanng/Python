import streamlit as st

st.title('🌍 My Learning Dashboard')
st.header('About Me')
st.subheader('A Python student from Delhi')

st.write('Welcome to my personal dashboard!')
st.write('I built this app using **Streamlit** and pure Python.')

st.markdown('---')  # Horizontal line

st.markdown('## My Favourite Topics')
st.markdown('- 🐍 Python programming')
st.markdown('- 🤖 Artificial Intelligence')
st.markdown('- 📊 Data Science')

st.success('Successfully built my first Streamlit app!')
st.info('This app was built in less than 10 minutes!')
st.warning('Remember to save your files before running!')
st.error('This is what an error message looks like.')

st.caption('Built with ❤️ using Streamlit and Python')
