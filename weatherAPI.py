"""
- Team 2 
- weatherAPI.py
- Used to make api requests 

"""

import requests

URL = "http://api.openweathermap.org/data/2.5/weather"
city = input("Enter the city: ")

API_KEY = '51feb6438334e6502cf871203e59a9af'

body = {'appid': API_KEY, 'q' : city}
response = requests.get(URL, params = body)

print(response.json())