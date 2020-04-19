# Django REST Framework
from rest_framework import serializers

# Services
from weather.services import MockWeatherService


class TemperatureSerializer(serializers.Serializer):
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    filters = serializers.ListField(default=["accu_wather", "noaa", "wheather"])
    temperature = serializers.SerializerMethodField()

    def validate_latitude(self, latitude):
        if latitude < -90 or latitude > 90:
            raise serializers.ValidationError("The latitude must be a number between -90 and 90")
        return latitude
    
    def validate_longitude(self, longitude):
        if longitude < -180 or longitude > 180:
            raise serializers.ValidationError("The longitude must be a number between -180 and 180")
        return longitude
    
    def validate_filters(self, filters):
        default_services = ["accu_wather", "noaa", "wheather"]

        for service in filters:
            if service not in default_services:
                raise serializers.ValidationError(
            "You send a wrong filter, the aviable filters are: accu_wather, noaa, wheather"
        )

        return filters

    def get_temperature(self, obj):
        latitude = self.validated_data["latitude"]
        longitude = self.validated_data["longitude"]
        filters = self.validated_data["filters"] 

        temperature_service = MockWeatherService()
        
        return temperature_service.get_average_temperature(latitude, longitude, filters)
