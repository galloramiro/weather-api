import requests


class MockWeatherApiClient:
    _BASE_URL = "http://flask-api:5000/"

    def _get(self, url: str, params: dict):
        return requests.get(f"{self._BASE_URL}{url}", params)

    def _post(self, url: str, params: dict):
        return requests.post(f"{self._BASE_URL}{url}", json=params)


class AccuWeatherClient(MockWeatherApiClient):
    _URL = "accuweather"
    
    def get_temperature(self, latitude: int, longitude: int):
        params = dict(latitude=latitude, longitude=longitude)
        return self._get(url=self._URL, params=params)


class NoaaClient(MockWeatherApiClient):
    _URL = "noaa"
    
    def get_temperature(self, latlon: str):
        params = dict(latlon=latlon)
        return self._get(url=self._URL, params=params)


class WeatherClient(MockWeatherApiClient):
    _URL = "weatherdotcom"
    
    def get_temperature(self, lat: float, lon: float):
        params = dict(lat=lat, lon=lon)
        return self._post(url=self._URL, params=params)
