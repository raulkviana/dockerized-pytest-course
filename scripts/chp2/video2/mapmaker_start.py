class Point():
    def __init__(self, name, longi, lati):
        # Verify if name variable is a string
        if not type(name) == str:
            raise(ValueError("Wrong type for name attribute")) 
        self._name = name

        # Verify if longitude or latitude are within the right range
        if not (180 >= longi >= -180 or  90 >= lati >= -90):
            raise(ValueError("Invalid latitude or longitude")) 
        self._longi = longi
        self._lati = lati

    def get_lat_long(self):
        return (self._longi, self._lati)
