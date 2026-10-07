from devices import Device
import json

class Actuator(Device):

    def __init__(self,status,timestamp,device_id, device_type, device_manufacturer):
        """ Initialize the actuator with a devices ID, a devices type """
        super().__init__(device_id, device_type, device_manufacturer)

        # Initialize the measurement value to None and the timestamp
        # Subclasses should override the update_measurement method to set the value
        self.status = status

        # Set the timestamp to None, subclasses should set the timestamp when updating the measurement
        self.timestamp = timestamp

    def invoke_action(self, action):
        """ This method should be overridden by subclasses to implement the specific action of the actuator """
        raise NotImplementedError("This method should be overridden by subclasses")
    

