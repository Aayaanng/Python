import streamlit as st

st.title('BMI Calculator')

# Input fields
name = st.text_input("Enter your name:")

height = st.number_input("Height (cm)", 
                        min_value=50, 
                        max_value=250, 
                        value=170)

weight = st.number_input("Weight (kg)", 
                        min_value=1, 
                        max_value=300, 
                        value=70)

if st.button('Calculate BMI'):
    if height > 0 and weight > 0:
        bmi = weight / ((height / 100) ** 2)
        bmi = round(bmi, 2)
        
        st.write(f"Hello **{name}**, your BMI is: **{bmi}**")
        
        # BMI categories with appropriate messages
        if bmi < 18.5:
            st.error("Underweight")
            st.info("You may need to gain some weight for better health.")
        elif 18.5 <= bmi < 25:
            st.success("Normal weight")
            st.info("Great! You're in a healthy range.")
        elif 25 <= bmi < 30:
            st.warning("Overweight")
            st.info("Consider some lifestyle changes.")
        else:
            st.error("Obese")
            st.info("It's recommended to consult a healthcare professional.")
        
        # BONUS: Progress bar (scaled to a reasonable BMI range 0-40)
        progress = min(max(bmi / 40, 0), 1.0)
        st.progress(progress)
        st.caption(f"BMI Progress (0–40 scale): {bmi}")
    else:
        st.error("Please enter valid height and weight.")