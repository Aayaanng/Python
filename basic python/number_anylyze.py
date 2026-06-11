num = int(input("Give me a number: "))

def analyze_number(number):
    if number == 0:
        print("This number is zero")
    elif number % 2 == 0:
        print("This is an even number")
    else:
        print("This number is odd")
analyze_number(num)
def thr_five(number):
    if num % 3 == 0 and num % 5 == 0:
        print("This number is divisible by 3 and 5")
    elif num % 3 == 0:
        print("This number is divisible by 3")
    elif num % 5 == 0:
        print("this number is divisible by 5")
    else:
        print("This number is not divisible by 3 and 5")
thr_five(num)