from math import sqrt

class GpsPosition:
    def __init__(self,lat,lng):
        self.lat = lat
        self.lng = lng
        self.alt = 0.0

    @property 
    def lng(self):
        return self.lng
    
    @lng.setter
    def lng(self,new_lng):
        self.lng = new_lng

    def distance(self,gps_pos: GpsPosition):
        return sqrt((self.lat-gps_pos.lat) **2 + (self.lng-gps_pos.lng) **2 )

    
pos_1 = GpsPosition(10.000,40.00000)
pos_2 = GpsPosition(10.2029,21.0949)
dist = pos_1.distance(pos_2)
print(pos_1.lng)
