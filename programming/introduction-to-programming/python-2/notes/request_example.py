import requests


r = requests.get('https://www.google.com/monkeybagel/')
if r.status_code == 404:
    print("Page not found.")

r = requests.get('https://www.metaweather.com/api/location/2455920')
d = r.json()
for forecast in d['consolidated_weather']:
    date = forecast['applicable_date']
    humidity = forecast['humidity']
    print(f"Date: {date}, Humidity: {humidity}")