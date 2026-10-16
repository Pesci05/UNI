from dataclasses import dataclass
from typing import Any
from iot_inventory.model.device_model import DeviceModel
from iot_inventory.dto.dto_utils import DtoUtils

@dataclass(frozen=True)
class DeviceCreationRequest:
    uuid: str
    device_type: str
    softwareVersion: str
    manufacturer: str

    @classmethod
    def from_json(cls, data:Any) -> 'DeviceCreationRequest':
        return cls(**DtoUtils.validate_fields(data, ('uuid', 'device_type', 'softwareVersion', 'manufacturer')))

    def to_model(self) -> DeviceModel:
        return DeviceModel(
            uuid=self.uuid,
            device_type=self.device_type,
            software_version=self.softwareVersion,
            manufacturer=self.manufacturer
        )