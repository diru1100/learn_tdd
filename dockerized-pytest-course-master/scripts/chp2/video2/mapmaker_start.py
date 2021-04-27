class Point():

    def __init__(self, city_name, latitude, longitude):
        self._city_name = city_name
        self._latitude = latitude
        self._longitude = longitude

    def get_lat_long(self):
        return (self._latitude, self._longitude)
