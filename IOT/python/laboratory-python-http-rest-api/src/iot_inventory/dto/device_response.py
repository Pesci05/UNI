from dataclasses import dataclass, asdict
from iot_inventory.model.device_model import DeviceModel

@dataclass(frozen=True)
class DeviceResponse:
    uuid: str
    manufacturer: str
    softwareVersion: str
    deviceType: str

    @classmethod
    def from_model(cls, device_model: DeviceModel) -> 'DeviceResponse': 
        return cls(
            uuid=device_model.uuid,
            manufacturer=device_model.manufacturer,
            softwareVersion=device_model.software_version,
            deviceType=device_model.device_type
        )

    def to_json(self) -> dict[str, str]:
        return asdict(self)
