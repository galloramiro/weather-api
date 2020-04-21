# weather-api

This API let you get the average temperature
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
  
### Set up the envirorment
```
$ git clone https://github.com/galloramiro/weather-api.git

$ cp weather-api/django-api/.env.template weather-api/django-api/.env
# In this new .env file you can chose your own variables or use the defaults

$ cd weather-api docker-compose up --build
```
**Run tests**
```
docker-compose run --rm django-api pytest -vv
```
