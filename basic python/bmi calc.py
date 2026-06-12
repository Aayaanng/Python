print("this is a BMI calculator")
kg = float(input(" What is your weight in kgs"))
height = float(input("What is you height in meters"))
bmi = kg / (height ** 2)
if bmi < 18.5:
    print("you are underweight your bmi is", bmi)
elif 18.5 <= bmi <= 24.9:
    print("You are perfectaly healthy your bmi is", bmi)
elif 25.0 <= bmi <= 29.9:
    print("You are overweight. Your BMI is:", bmi)
else:
    print("You are obese. Your BMI is:", bmi)
