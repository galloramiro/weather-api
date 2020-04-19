"""Wather URLs."""

# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from weather.views import TemperatureView


router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path(r"temperature/", TemperatureView.as_view(), name="temperature")
]
