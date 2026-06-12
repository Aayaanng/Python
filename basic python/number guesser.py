import random

ans = random.randint(1, 100)
print("Welcome to the number guessing game!")
print("I have chosen a random number between 1 and 100.")
print("You have only 3 attempts to guess it.\n")

attempts = 3

while attempts > 0:
    user_input = input(f"Attempt {4 - attempts}/3 - Type your guess (or 'quit' to exit): ").strip()
    
    if user_input.lower() == "quit":
        print(f"You quit. The number was {ans}")
        break
    
    try:
        user = int(user_input)
    except ValueError:
        print("Please enter a valid number or 'quit'.")
        continue
    
    if user == ans:
        print(f"Wow! You guessed it correctly in {4 - attempts} attempts!")
        break
    elif user < ans:
        print("Too low!")
    else:
        print("Too high!")
    
    attempts -= 1
    
    if attempts > 0:
        print(f"You have {attempts} attempt{'s' if attempts > 1 else ''} left.\n")
    else:
        print(f"\nGame Over! The number was {ans}")

print("Thanks for playing!")
