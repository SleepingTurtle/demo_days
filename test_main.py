from main import fetchWeather


def test_api_version():
    assert fetchWeather("41.409", "-75.6624") == "1.1"
