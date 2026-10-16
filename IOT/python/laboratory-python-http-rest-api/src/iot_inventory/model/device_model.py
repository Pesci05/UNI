from datetime import timezone, datetime

class DeviceModel:
    def __init__(self, uuid:str, device_type:str, software_version:str, manufacturer:str) -> None:
        self.uuid = uuid
        self.device_type = device_type
        self.software_version = software_version
        self.manufacturer = manufacturer
        self.created_at = datetime.now(timezone.utc)

    
    