import time
import random

class Device:
    def __init__(self,id,type,manufacturer,timestamp):
        self.id = id
        self.type = type
        self.manufacturer = manufacturer
        self.timestamp = timestamp

    @property
    def id(self):
        return self.id
    @property
    def type(self):
        return self.type
    @property
    def manufacturer(self):
        return self.manufacturer
    @property
    def timestamp(self):
        return self.timestamp

class Sensor(Device):
    def __init__(self, id, type, manufacturer, timestamp,value):
        super().__init__(id, type, manufacturer, timestamp)
        self.value = value
        