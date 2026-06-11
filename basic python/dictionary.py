me = {
    "name": "Aayaann Gupta",
    "age": 12,
    "city": "Delhi",
    "Fav_subject": "Sceince",
    "fav_food": "Sushi"
}
print(f"Hello {me['name']}") 
print(f"You're {me['age']} years old") 
print(f"You live in {me['city']}") 
print(f"Your favourite subject is {me['Fav_subject']}") 
print(f"Youre favourite food is {me['fav_food']}")
#project 2
countries = {
    "india": "New delhi",
    "France": "Paris",
    "Spain": "Madrid",
    "Japan": "tokyo",
    "Russia": "moscow"
}
user_country = input("Type a country name: ").title()
capital_look_up = countries.get(user_country, "Not Found in our database")
print(f"The capital of {user_country} is: {capital_look_up}\n")
print("--- Full List of Countries and Capitals ---")
for country, capital in countries.items():
    print(f"Country: {country} | Capital: {capital}")