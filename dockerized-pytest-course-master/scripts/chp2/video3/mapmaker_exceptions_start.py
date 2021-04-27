
class Point():
    def __init__(self, name, latitude, longitude):
        if type(name) != str:
            raise TypeError("City name must be a string")
        self.name = name
        if not (-90 <= longitude <= 90) and (-180 <= latitude <= 180):
            raise ValueError("Invalid Coordinates")
        self.latitude = latitude
        self.longitude = longitude

    def get_lat_long(self):
        return (self.latitude, self.longitude)
