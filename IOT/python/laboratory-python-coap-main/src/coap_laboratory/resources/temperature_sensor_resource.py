import aiocoap
import aiocoap.resource as resource
from aiocoap.numbers import ContentFormat

from coap_laboratory.model.temperature_sensor import TemperatureSensor


class TemperatureSensorResource(resource.Resource):
    """ CoAP resource of the Temperature Sensor (/temperature).
    It supports only the GET method and returns the current temperature as JSON """

    def __init__(self) -> None:
        """ Constructor for TemperatureSensorResource class """
        super().__init__()
        self.temperature_sensor = TemperatureSensor()

    async def render_get(self, request: aiocoap.Message) -> aiocoap.Message:
        """ GET /temperature: measure a new value and return it as JSON (2.05 Content) """

        print("TemperatureSensorResource -> GET Request Received ...")

        self.temperature_sensor.measure_temperature()
        print(f"TemperatureSensorResource -> Updated Temperature Value: {self.temperature_sensor.value:.2f}")

        payload_string = self.temperature_sensor.to_json()

        # The code is not specified: aiocoap uses 2.05 Content as default for GET requests
        return aiocoap.Message(content_format=ContentFormat.JSON, payload=payload_string.encode("utf-8"))
