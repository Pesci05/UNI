from iot_inventory.model.device_model import DeviceModel

class DataManager:
    def __init__(self) -> None:
        self.device_dictionary:dict [str,DeviceModel] = {}
    
    def add_device(self, device: DeviceModel) -> None:
        if isinstance(device, DeviceModel):
            self.device_dictionary[device.uuid] = device
        else:
            raise TypeError("Error adding new device ! Only DeviceModel are allowed !")

    def remove_device(self, device: DeviceModel) -> None:
        if device.uuid in self.device_dictionary:
            del self.device_dictionary[device.uuid]
        else:
            raise ValueError(f"Device with UUID {device.uuid} not found in the dictionary.")

    def update_device(self, device: DeviceModel) -> None:
        if device.uuid in self.device_dictionary:
            self.device_dictionary[device.uuid] = device
        else:
            raise ValueError(f"Device with UUID {device.uuid} not found in the dictionary.")

    def get_device(self, uuid: str) -> DeviceModel:
        if uuid in self.device_dictionary:
            return self.device_dictionary[uuid]
        else:
            raise ValueError(f"Device with UUID {uuid} not found in the dictionary.")

    def get_all_devices(self) -> list[DeviceModel]:
        return list(self.device_dictionary.values())

    