from main import fetchWeatherAPIVersion, fetchWeather


def test_api_version():
    assert fetchWeatherAPIVersion("41.409", "-75.6624") == "1.1"


def test_feather_weather():
    data = fetchWeatherAPIVersion("41.409", "-75.6624")

    # Check if response is a temperate
    assert isinstance(data, str)
