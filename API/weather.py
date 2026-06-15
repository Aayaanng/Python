import requests

api_key = 'b793f0b2015f70453826df53c5189ce7'   
# Get free key at openweathermap.org
city = 'Delhi'

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
response = requests.get(url)

print(response.status_code)

print(response.text)