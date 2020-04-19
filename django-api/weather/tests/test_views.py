# Pytest
import pytest

# Django
from django.urls import reverse

# Django REST Framework
from rest_framework import status
from rest_framework.test import APIClient


def test_temperature_view():
    client = APIClient()
    params = dict(
        latitude=44.0, 
        longitude=33.0, 
        filters=["accu_wather", "noaa", "wheather"],
    )
    response = client.get(reverse("weather:temperature"), params)
    
    expected_response = dict(
        latitude=44.0,
        longitude=33.0,
        filters=["accu_wather", "noaa", "wheather"],
        temperature=8.93,
    )
    
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_response


def test_temperature_with_two_filters():
    client = APIClient()
    params = dict(
        latitude=44.0, 
        longitude=33.0, 
        filters=["accu_wather", "noaa"],
    )
    response = client.get(reverse("weather:temperature"), params)
    
    expected_response = dict(
        latitude=44.0,
        longitude=33.0,
        filters=["accu_wather", "noaa"],
        temperature=12.0,
    )
    
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_response


def test_temperature_with_wrong_filters():
    client = APIClient()
    params = dict(
        latitude=44.0, 
        longitude=33.0, 
        filters=["accu_wather", "noaa", "eltiempo"],
    )
    response = client.get(reverse("weather:temperature"), params)
    
    expected_response = dict(
        filters=["You send a wrong filter, the aviable filters are: accu_wather, noaa, wheather"],
    )
    
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == expected_response


def test_temperature_with_wrong_latitude():
    client = APIClient()
    params = dict(
        latitude=150.0, 
        longitude=33.0, 
        filters=["accu_wather", "noaa"],
    )
    response = client.get(reverse("weather:temperature"), params)
    
    expected_response = dict(
        latitude=["The latitude must be a number between -90 and 90"],
    )
    
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == expected_response


def test_temperature_with_wrong_longitude():
    client = APIClient()
    params = dict(
        latitude=44.0, 
        longitude=350.0, 
        filters=["accu_wather", "noaa"],
    )
    response = client.get(reverse("weather:temperature"), params)
    
    expected_response = dict(
        longitude=["The longitude must be a number between -180 and 180"],
    )
    
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == expected_response
