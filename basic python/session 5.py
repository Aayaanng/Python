# f strings
name = input("What is your name.")
print(f"Hi {name} how are you")
# mini project 1
print(f"{name.upper()}")  
print(f"{name.title()}")  
#m.p 2
sent = input("type a sentence: ")
count = sent.lower().count('a')
print(f"The letter a appears {count} times in your sentence.")
#m.p 3
name = "Aayaann"
age = 12
city = "Delhi"

sentence = f"My name is {name}, I am {age} years old, and I live in {city}."
print(sentence)

# Bonus
print("\n" + "="*50 + "\n")

user_word = input("Please enter a word: ")
word2 = user_word.replace('a', '*').replace('e', '*').replace('i', '*').replace('o', '*').replace('u', '*')
word2 = word2.replace('A', '*').replace('E', '*').replace('I', '*').replace('O', '*').replace('U', '*')

print(f"Original word: {user_word}")
print(f"Word with vowels replaced by stars: {word2}")