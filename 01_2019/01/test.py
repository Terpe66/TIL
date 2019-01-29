class LocalWeather(models.Model):
    location = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    temperature = models.FloatField(default=0.0)
    summary = models.CharField(max_length=50)
    search_time = models.DateTimeField("date published")

    def get_weather(input_location):
    from darksky import forecast
    from geopy.geocoders import Nominatim
    from datetime import datetime
    
    API_KEY = "7cbe2c49b01ebc4a748fca21952f5404"
    geo = Nominatim(user_agent="wj weather app")
    
    l = geo.geocode(input_location)
    lat = l.latitude
    lon = l.longitude
    location = forecast(API_KEY, lat, lon)
    temperature = round((location.currently["temperature"]-32)/1.8, 2)
    summary = location.currently["summary"]
    t = datetime.utcfromtimestamp(location.time)
    return (lat, lon, temperature, summary, t)




