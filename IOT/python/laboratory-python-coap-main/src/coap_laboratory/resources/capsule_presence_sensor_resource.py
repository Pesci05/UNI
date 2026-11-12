import aiocoap
import aiocoap.resource as resource
from aiocoap.numbers import ContentFormat

from coap_laboratory.model.capsule_presence_sensor import CapsulePresenceSensor


class CapsulePresenceSensorResource(resource.Resource):
    """ CoAP resource of the Capsule Presence Sensor (/capsule).
    It supports only the GET method and returns the presence of the capsule as JSON """

    def __init__(self) -> None:
        """ Constructor for CapsulePresenceSensorResource class """
        super().__init__()
        self.sensor = CapsulePresenceSensor()

    async def render_get(self, request: aiocoap.Message) -> aiocoap.Message:
        """ GET /capsule: check the presence of the capsule and return it as JSON (2.05 Content) """

        print("CapsulePresenceSensorResource -> GET Request Received ...")

        self.sensor.check_capsule_presence()
        print(f"CapsulePresenceSensorResource -> Capsule Presence: {self.sensor.value}")

        payload_string = self.sensor.to_json()

        return aiocoap.Message(content_format=ContentFormat.JSON, payload=payload_string.encode("utf-8"))
