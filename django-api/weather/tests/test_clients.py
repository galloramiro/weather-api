import pytest

# Django REST Framework
from rest_framework import status

# Clients
from weather.clients import (
    AccuWeatherClient,
    NoaaClient,
    WeatherClient,
)


def test_accu_weather_client():
    client = AccuWeatherClient()
    response = client.get_temperature(latitude=44, longitude=33)

    expected_response = dict(
        simpleforecast=dict(
            forecastday=[
                dict(
                    period=1,
                    high=dict(fahrenheit="68", celsius="20"),
                    low=dict(fahrenheit="50", celsius="10"),
                    current=dict(fahrenheit="55", celsius="12"),
                    conditions="Partly Cloudy",
                    icon="partlycloudy",
                    icon_url="http://icons-ak.wxug.com/i/c/k/partlycloudy.gif",
                    skyicon="mostlysunny",
                    pop=0,
                    qpf_allday={"in":0.0, "mm":0.0}
                )
            ]
        )
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_response


def test_noaa_client():
    client = NoaaClient()
    response = client.get_temperature("44,33")

    expected_response = dict(
        today=dict(
            high=dict(fahrenheit="68", celsius="20"),
            low=dict(fahrenheit="50", celsius="10"),
            current=dict(fahrenheit="55", celsius="12"),
        )
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_response


def test_weather_client():
    client = WeatherClient()
    response = client.get_temperature(lat=44.4,lon=33.3)

    expected_response = dict(
        query=dict(
            count=1,
            created="2017-09-21T17:00:22Z",
            lang="en-US",
            results=dict(
                channel=dict(
                    units=dict(temperature="F"),
                    description="Current Weather",
                    language="en-us",
                    lastBuildDate="Thu, 21 Sep 2017 09:00 AM AKDT",
                    ttl="60",
                    condition=dict(
                        code="33",
                        date="Thu, 21 Sep 2017 08:00 AM AKDT",
                        temp="37",
                        text="Mostly Clear",
                    ),
                    atmosphere=dict(
                        humidity="80",
                        pressure="1014.0",
                        rising="0",
                        visibility="16.1",
                    ),
                    astronomy=dict(
                        sunrise="8:42 am",
                        sunset="9:6 pm",
                    ),
                    item=dict(
                        title="Conditions for Nome, AK, US at 08:00 AM AKDT",
                        lat="64.499474",
                        long="-165.405792",
                        pubDate="Thu, 21 Sep 2017 08:00 AM AKDT",
                        guid=dict(
                            isPermaLink="false"
                        ),
                    ),
                )
            )
        )
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_response
