import streamlit as st

st.title('🧮 Mini Calculator')

num1 = st.number_input('First number:', value=0.0)
operation = st.selectbox('Operation:', ['+', '-', '×', '÷'])
num2 = st.number_input('Second number:', value=0.0)

if st.button('Calculate'):
    if operation == '+': result = num1 + num2
    elif operation == '-': result = num1 - num2
    elif operation == '×': result = num1 * num2
    elif operation == '÷':
        result = num1 / num2 if num2 != 0 else 'Cannot divide by zero!'
    st.success(f'Result: {result}')
