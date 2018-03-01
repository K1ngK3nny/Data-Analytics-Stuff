import numpy as np
from citipy import citipy
import random
import pandas as pd
import requests as req
import matplotlib.pyplot as plt
#lon_num = []
#lat_num = []

# for num in range(10):
#lat_num.append((np.random.uniform(-90, 90)))
#lon_num.append((np.random.uniform(-180, 180)))

latitude = random.uniform(-180, 180)
longitude = random.uniform(-90, 90)
coordinates = latitude, longitude
# print(coordinates)
lat = str(latitude)
lon = str(longitude)
# print(lat)
# print(lon)
url = 'http://api.openweathermap.org/data/2.5/weather?'
api_key = "9ef922d0ab5fd420158534ff5ea78e9e"
response_json = []
lat_indices = random.sample(list(range(-90, 90)), 500)
long_indices = random.sample(list(range(-180, 180)), 500)
# Build query URL and request your results in Celsius
query_url = url + "appid=" + api_key  # + "&lat=" + lat + "&lon=" + lon

for i in range(0, len(lat_indices)):
    print("Making request number " + str(i) +
          " for coordinate (" + str(lat_indices[i]) + ", " + str(long_indices[i]) + ").")     # do I need to make these variables random choices and increase indice size?
    post_response = req.get(query_url + "&lat=" +
                            str(lat_indices[i]) + "&lon=" + str(long_indices[i]))
    response_json.append(post_response.json())

print(response_json)
#json_data = req.get(query_url).json()
# print(json_data)
lat_data = [data.get("coord").get("lat") for data in response_json]
temp_data = [data.get("main").get("temp") for data in response_json]

weather_data = {"temp": temp_data, "lat": lat_data}
weather_data = pd.DataFrame(weather_data)
weather_data.head()
plt.scatter(weather_data["lat"], weather_data["temp"], marker="o")

# Incorporate the other graph properties
plt.title("Temperature in World Cities")
plt.ylabel("Temperature (Celsius)")
plt.xlabel("Latitude")
plt.grid(True)

# Save the figure
plt.savefig("TemperatureInWorldCities.png")

# Show plot
plt.show()

lat_data = [data.get("coord").get("lat") for data in response_json]
temp_data = [data.get("main").get("humidity") for data in response_json]

weather_data = {"humidity": temp_data, "lat": lat_data}
weather_data = pd.DataFrame(weather_data)
weather_data.head()
plt.scatter(weather_data["lat"], weather_data["humidity"], marker="o")
plt.title("Humidity in World Cities")
plt.ylabel("Humidity")
plt.xlabel("Latitude")
plt.grid(True)

# Save the figure
plt.savefig("HumidityInWorldCities.png")

# Show plot
plt.show()





lat_data = [data.get("coord").get("lat") for data in response_json]
temp_data = [data.get("clouds").get("all") for data in response_json]

weather_data = {"all": temp_data, "lat": lat_data}
weather_data = pd.DataFrame(weather_data)
weather_data.head()

plt.scatter(weather_data["lat"], weather_data["all"], marker="o")

# Incorporate the other graph properties
plt.title("Clouds in World Cities")
plt.ylabel("Clouds")
plt.xlabel("Latitude")
plt.grid(True)

# Save the figure
plt.savefig("CloudsInWorldCities.png")
plt.show()


lat_data = [data.get("coord").get("lat") for data in response_json]
temp_data = [data.get("wind").get("speed") for data in response_json]

weather_data = {"speed": temp_data, "lat": lat_data}
weather_data = pd.DataFrame(weather_data)
weather_data.head()
plt.scatter(weather_data["lat"], weather_data["speed"], marker="o")
plt.title("Wind in World Cities")
plt.ylabel("Wind")
plt.xlabel("Latitude")
plt.grid(True)

# Save the figure
plt.savefig("WindInWorldCities.png")

# Show plot
plt.show()
