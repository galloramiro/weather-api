# Django REST Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Serializers
from weather.serializers import TemperatureSerializer


class TemperatureView(APIView):
    """This API let you get the average temperature
    based on 3 wather services.
    You can select what services we use to get the 
    temperature. By default we use it all. 

    params:
      - latitude -> float
      - longitude -> float
      - filters -> list ["accu_wather", "noaa", "wheather"]

    return:
      - latitude
      - longitude
      - filters
      - temperature
    """

    def get(self, request, format=None):
        serializer = TemperatureSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
