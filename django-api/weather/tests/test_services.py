import pytest

from weather.services import MockWeatherService


def test_get_accu_weather_temperature():
    service = MockWeatherService()
    temperature = service._get_accu_weather_temperature(44.0, 33.0)
    
    assert temperature == 12.0


def test_get_noaa_temperature():
    service = MockWeatherService()
    temperature = service._get_noaa_temperature(44.0, 33.0)
    
    assert temperature == 12.0


def test_get_weather_temperature():
    service = MockWeatherService()
    temperature = service._get_weather_temperature(44.0, 33.0)
    
    assert temperature == 2.78


def test_get_average_temperature_with_all_services():
    service = MockWeatherService()
    temperature = service.get_average_temperature(
        latitude=44.0, 
        longitude=33.0, 
        filters=["accu_wather", "noaa", "wheather"]
    )

    assert temperature == 8.93


def test_get_average_temperature_with_two_services():
    service = MockWeatherService()
    temperature = service.get_average_temperature(
        latitude=44.0, 
        longitude=33.0, 
        filters=["accu_wather", "noaa"]
    )

    assert temperature == 12.00


def test_get_average_temperature_with_one_services():
    service = MockWeatherService()
    temperature = service.get_average_temperature(
        latitude=44.0, 
        longitude=33.0, 
        filters=["accu_wather"]
    )

    assert temperature == 12.00
