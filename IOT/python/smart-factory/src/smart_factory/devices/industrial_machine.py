from smart_factory.devices.device import Device
from smart_factory.devices.accelerometer import Accelerometer
from smart_factory.devices.energySensor import EnergySensor
from smart_factory.devices.switch import Switch
import json

class IndustrialMachine(Device):
    DEVICE_TYPE = "iot.industrial.machine"

    def __init__(self, device_id, accelerometer_sensor_number: int=3):
        super().__init__(device_id,IndustrialMachine.DEVICE_TYPE,"acme Inc.")
        self.energy_sensor = EnergySensor(f'{self.device_id}_energy_sensor')
        self.switch = Switch(f'{self.device_id}_switch')
        self.accelerometer_sensor_list = []

        for i in range(accelerometer_sensor_number):
            self.accelerometer_sensor_list.append(Accelerometer(f'{self.device_id}_accelerometer_{i}'))
