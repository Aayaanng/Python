while True:
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Invalid number(s) entered. Please try again.")
        continue

    if op == '+':
        print(f"Result: {num1 + num2}")
    elif op == '-':
        print(f"Result: {num1 - num2}")
    elif op == '*':
        print(f"Result: {num1 * num2}")
    elif op == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"Result: {num1 / num2}")
    else:
        print("Error: Invalid operator entered.")
        
    exit = input("Press 'q' to quit, or any other key to continue: ").lower()
    if exit == 'q':
        break
