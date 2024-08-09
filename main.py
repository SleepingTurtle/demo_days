import requests


def fetchWeatherAPIVersion(lat, lon):
    response = requests.get(f"https://api.weather.gov/points/{lat},{lon}").json()
    x = response["@context"][1]["@version"]
    print("EVERTHING CAPS")
    return x

if __name__ == "__main__":

    fetchWeatherAPIVersion(44, 22)
