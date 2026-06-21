a = int(input("What is the first number"))
b = int(input("What is the second number"))
c = (input("which operation do you choose write in symbols +, -, *, /"))
print("Aayaann calculater app")
if c == "+":
    print("the answer is", a + b)
elif c == "-":
    print("the answer is", a - b)
elif c == "*":
    print("the answer is", a * b)
elif c == "/":
    print("the answer is", a / b)
    print("the remainder is", a % b)
elif a == 0 or b == 0 and c == "/":
    print("You cannot divide by zero")
else:
    print("Invalid operation plz try again")

print("Thank you for using this calculator")