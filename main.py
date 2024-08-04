import requests


def fetchWeather(lat, lon):
    response =  requests.get(f"https://api.weather.gov/points/{lat},{lon}")  .json()
    x = response["@context"][1]["@version"]
    print("EVERTHING CAPS")
    return x


if __name__ == "__main__":
    print(fetchWeather('41.409','-75.6624'))


