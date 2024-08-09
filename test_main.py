import unittest
from unittest.mock import patch, Mock
import requests

def fetchWeatherAPIVersion(lat, lon):
    response = requests.get(f"https://api.weather.gov/points/{lat},{lon}").json()
    x = response["@context"][1]["@version"]
    print("EVERTHING CAPS")
    return x

class TestFetchWeatherAPIVersion(unittest.TestCase):

    @patch('requests.get')
    def test_fetchWeatherAPIVersion(self, mock_get):
        # Arrange
        mock_response = Mock()
        expected_version = "1.0"
        mock_response.json.return_value = {
            "@context": [
                {},
                {"@version": expected_version}
            ]
        }
        mock_get.return_value = mock_response
        
        lat = 38.8977
        lon = -77.0365
        
        # Act
        result = fetchWeatherAPIVersion(lat, lon)
        
        # Assert
        self.assertEqual(result, expected_version)
        mock_get.assert_called_once_with(f"https://api.weather.gov/points/{lat},{lon}")

    @patch('builtins.print')
    @patch('requests.get')
    def test_print_called(self, mock_get, mock_print):
        # Arrange
        mock_response = Mock()
        mock_response.json.return_value = {
            "@context": [
                {},
                {"@version": "1.0"}
            ]
        }
        mock_get.return_value = mock_response
        
        lat = 38.8977
        lon = -77.0365
        
        # Act
        fetchWeatherAPIVersion(lat, lon)
        
        # Assert
        mock_print.assert_called_once_with("EVERTHING CAPS")

if __name__ == "__main__":
    unittest.main()
