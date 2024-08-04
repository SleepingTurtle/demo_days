import requests


def fetchWeatherAPIVersion(lat, lon):
    response = requests.get(f"https://api.weather.gov/points/{lat},{lon}").json()
    x = response["@context"][1]["@version"]
    print("EVERTHING CAPS")
    return x


def fetchWeather(lat, lon):
    response = requests.get(f"https://api.weather.gov/points/{lat},{lon}").json()
    hourlyLink = response["properties"]["forecastHourly"]
    response = requests.get(f"{hourlyLink}").json()
    hourTemp = response["properties"]["periods"][0]["temperature"]
    return hourTemp


if __name__ == "__main__":
    temperature = fetchWeather("41.409", "-75.6624")
    print(f"The current temperature is: {temperature}F")
