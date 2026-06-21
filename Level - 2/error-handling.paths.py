try:
    num = int(input("Enter a number"))
    result = 10/num

except ValueError:
    print("invalid input, Please enter a valid number")

except ZeroDivisionError:
    print("You cannot divide by zero")

else:
    print("The result is", result)

finally:
    print("this block is always executed")