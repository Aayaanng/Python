import streamlit as st
import pandas as pd

# ---- PAGE CONFIG ----
st.set_page_config(page_title='Grade Dashboard', page_icon='🎓', layout='wide')

# ---- SESSION STATE ----
if 'students' not in st.session_state:
    st.session_state.students = []

# ---- HEADER ----
st.title('🎓 Student Grade Dashboard')
st.caption('A Streamlit app to track student scores')
st.divider()

# ---- SIDEBAR: Add Student ----
st.sidebar.header('Add New Student')
name  = st.sidebar.text_input('Name')
score = st.sidebar.slider('Score', 0, 100, 75)
subj  = st.sidebar.selectbox('Subject', ['Maths','Science','English'])

if st.sidebar.button('Add Student ➕'):
    if name:
        st.session_state.students.append({'Name':name,'Score':score,'Subject':subj})
        st.sidebar.success(f'{name} added!')
    else:
        st.sidebar.error('Please enter a name!')

# ---- MAIN: Display Data ----
if st.session_state.students:
    df = pd.DataFrame(st.session_state.students)

    col1, col2, col3 = st.columns(3)
    col1.metric('Total Students', len(df))
    col2.metric('Average Score',  f"{df['Score'].mean():.1f}")
    col3.metric('Highest Score',  df['Score'].max())

    st.subheader('All Students')
    st.dataframe(df, use_container_width=True)

    st.subheader('Score Distribution')
    st.bar_chart(df.set_index('Name')['Score'])

    if st.button('Clear All Data'):
        st.session_state.students = []
        st.rerun()
else:
    st.info('No students yet. Add one from the sidebar! 👈')
