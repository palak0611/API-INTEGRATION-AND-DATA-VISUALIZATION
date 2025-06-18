import requests
import pandas as pd
import matplotlib.pyplot as plt
API_KEY = 'a49124700a0abe04374189d9e3497db8'

latitude = 44.34
longitude = 10.99
city_name = 'Example City (44.34, 10.99)'

url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=a49124700a0abe04374189d9e3497db8&units=metric"

response = requests.get(url)
data = response.json()

weather = {
    'City': city_name,
    'Temperature (C)': data['main']['temp'],
    'Humidity (%)': data['main']['humidity'],
    'Pressure (hPa)': data['main']['pressure']
}


df = pd.DataFrame([weather])
print("Weather Data:\n", df)


plt.figure(figsize=(8, 5))
plt.bar(['Temperature (C)', 'Humidity (%)', 'Pressure (hPa)'],
        [weather['Temperature (C)'], weather['Humidity (%)'], weather['Pressure (hPa)']],
        color=['orange', 'skyblue', 'lightgreen'])

plt.title(f"Weather at {city_name}")
plt.ylabel("Values")
plt.grid(True)
plt.tight_layout()
plt.show()