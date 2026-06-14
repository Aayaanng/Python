import streamlit as st

# Initialize session state variable (only if it does not exist yet)
if 'count' not in st.session_state:
    st.session_state.count = 0

st.title('Counter App')
st.write(f'Count: {st.session_state.count}')

if st.button('Add 1'):
    st.session_state.count += 1

if st.button('Reset'):
    st.session_state.count = 0
# QUIZ APP using Session State
questions = [
    {'q': 'What is 5 + 3?',         'a': '8'},
    {'q': 'Capital of India?',       'a': 'New Delhi'},
    {'q': 'What language is this?',  'a': 'Python'},
]

# Initialize session state
if 'q_index' not in st.session_state: st.session_state.q_index = 0
if 'score'   not in st.session_state: st.session_state.score = 0
if 'done'    not in st.session_state: st.session_state.done = False

st.title('🧠 Mini Quiz')

if not st.session_state.done:
    i = st.session_state.q_index
    st.subheader(f'Q{i+1}: {questions[i]["q"]}')
    answer = st.text_input('Your answer:', key=f'ans_{i}')
    if st.button('Submit'):
        if answer.strip().lower() == questions[i]['a'].lower():
            st.success('Correct! ✅')
            st.session_state.score += 1
        else:
            st.error(f'Wrong! Answer was: {questions[i]["a"]}')
        st.session_state.q_index += 1
        if st.session_state.q_index >= len(questions):
            st.session_state.done = True
else:
    st.balloons()
    st.success(f'Quiz done! Score: {st.session_state.score}/{len(questions)}')
    if st.button('Restart'): st.session_state.clear()
