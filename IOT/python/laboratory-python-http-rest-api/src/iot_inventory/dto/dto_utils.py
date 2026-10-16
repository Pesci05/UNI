from typing import Any


class DtoUtils:

    @staticmethod
    def validate_fields(data: Any, fields: tuple[str, ...]) -> dict[str, str]:
        if not isinstance(data, dict):
            raise ValueError("Invalid device data ! The body must be a JSON object")

        missing_fields = [field for field in fields if field not in data]
        if missing_fields:
            raise ValueError("Invalid device data ! Missing fields: " + ", ".join(missing_fields))

        unknown_fields = [field for field in data if field not in fields]
        if unknown_fields:
            raise ValueError("Invalid device data ! Unknown fields: " + ", ".join(unknown_fields))

        invalid_fields = [field for field in fields if not isinstance(data[field], str)]
        if invalid_fields:
            raise ValueError("Invalid device data ! Fields must be strings: " + ", ".join(invalid_fields))

        return data