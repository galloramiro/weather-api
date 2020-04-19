import statistics

from weather.clients import (
    AccuWeatherClient, 
    NoaaClient, 
    WeatherClient,
)


class MockWeatherService:

    def get_average_temperature(self, latitude: float, longitude:float, filters: list):
        temperatures = list()

        if "accu_wather" in filters:
            temperatures.append(self._get_accu_weather_temperature(latitude, longitude))
        if "noaa" in filters:
            temperatures.append(self._get_noaa_temperature(latitude, longitude))
        if "wheather" in filters:
            temperatures.append(self._get_weather_temperature(latitude, longitude))
        
        return round(statistics.mean(temperatures), 2)
        
    def _get_accu_weather_temperature(self, latitude: float, longitude:float):
        client = AccuWeatherClient()
        response = client.get_temperature(int(latitude), int(longitude))
        current_temperature_celsius = response.json()["simpleforecast"]["forecastday"][0]["current"] 
        return float(current_temperature_celsius["celsius"])
    
    def _get_noaa_temperature(self, latitude: float, longitude:float):
        client = NoaaClient()
        response = client.get_temperature(latlon=f"{int(latitude)},{int(longitude)}")
        current_temperature_celsius = response.json()["today"]["current"] 
        return float(current_temperature_celsius["celsius"])
    
    def _get_weather_temperature(self, latitude: float, longitude:float):
        client = WeatherClient()
        response = client.get_temperature(lat=latitude, lon=longitude)
        current_temperature_farenheit = response.json()["query"]["results"]["channel"]["condition"]["temp"]  
        current_temperature_celsius = (float(current_temperature_farenheit) - 32) * 5/9
        return round(current_temperature_celsius, 2)


