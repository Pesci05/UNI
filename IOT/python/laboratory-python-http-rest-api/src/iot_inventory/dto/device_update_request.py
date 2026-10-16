from dataclasses import dataclass
from typing import Any
from iot_inventory.model.device_model import DeviceModel
from iot_inventory.dto.dto_utils import DtoUtils


@dataclass(frozen=True)
class DeviceUpdateRequest:
    device_type: str
    softwareVersion: str
    manufacturer: str

    @classmethod
    def from_json(cls, data:Any) -> 'DeviceUpdateRequest':
        if isinstance(data,dict) and "uuid" in data:
            raise ValueError("Invalid device data ! The device uuid cannot be changed: "
                             "remove the uuid field from the body (the device is identified by the URL)")
        return cls(**DtoUtils.validate_fields(data, ('device_type', 'softwareVersion', 'manufacturer')))

    def to_model(self,device:DeviceModel) -> DeviceModel:
        device.manufacturer = self.manufacturer
        device.device_type = self.device_type
        device.software_version = self.softwareVersion
