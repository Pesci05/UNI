import aiocoap
import aiocoap.resource as resource
from aiocoap.numbers import ContentFormat

from coap_laboratory.dto.make_coffee_request import MakeCoffeeRequest
from coap_laboratory.model.coffee_history import CoffeeHistory


class CoffeeActuatorResource(resource.ObservableResource):
    """ Observable CoAP resource of the Coffee Actuator (/coffee):
    - GET: return the statistics of the coffees made by the machine (JSON)
    - POST (no payload): make a coffee of the default type (short)
    - PUT (JSON payload {"type": "short" | "medium" | "long"}): make a coffee of the requested type
    Every time a new coffee is made the observers receive a notification with the updated statistics """

    def __init__(self) -> None:
        """ Constructor for CoffeeActuatorResource class """
        super().__init__()
        self.coffee_history = CoffeeHistory()

    def build_history_payload(self) -> bytes:
        """ Build the JSON payload with the current statistics of the coffees """
        return self.coffee_history.to_json().encode("utf-8")

    def notify_new_coffee(self) -> aiocoap.Message:
        """ Notify the observers about the new coffee and build the response (2.04 Changed + updated statistics) """

        # aiocoap calls render_get() for each observer and sends the notification
        self.updated_state()
        print(f"CoffeeActuatorResource -> Coffee History: {self.coffee_history.to_json()}")

        return aiocoap.Message(code=aiocoap.CHANGED,
                               content_format=ContentFormat.JSON,
                               payload=self.build_history_payload())

    async def render_get(self, request: aiocoap.Message) -> aiocoap.Message:
        """ GET /coffee: return the statistics of the coffees (also used for the notifications to the observers) """

        print("CoffeeActuatorResource -> GET Request Received ...")
        return aiocoap.Message(content_format=ContentFormat.JSON, payload=self.build_history_payload())

    async def render_post(self, request: aiocoap.Message) -> aiocoap.Message:
        """ POST /coffee (no payload): make a coffee of the default type (short) """

        print("CoffeeActuatorResource -> POST Request Received -> Making a default (short) coffee ...")

        self.coffee_history.increase_short_coffee()
        return self.notify_new_coffee()

    async def render_put(self, request: aiocoap.Message) -> aiocoap.Message:
        """ PUT /coffee (JSON payload): make a coffee of the type specified in the request """

        print(f"CoffeeActuatorResource -> PUT Request Received - Payload: {request.payload!r}")

        # The payload must be JSON: 4.15 Unsupported Content-Format otherwise
        if request.opt.content_format != ContentFormat.JSON:
            print("CoffeeActuatorResource -> Unsupported Content-Format -> 4.15 Unsupported Content-Format")
            return aiocoap.Message(code=aiocoap.UNSUPPORTED_CONTENT_FORMAT)

        # Deserialize the request: 4.00 Bad Request if the payload is not valid
        try:
            make_coffee_request = MakeCoffeeRequest.from_json(request.payload.decode("utf-8"))
        except (UnicodeDecodeError, ValueError) as e:
            print(f"CoffeeActuatorResource -> Invalid Request ({e}) -> 4.00 Bad Request")
            return aiocoap.Message(code=aiocoap.BAD_REQUEST)

        print(f"CoffeeActuatorResource -> Coffee Type Requested: {make_coffee_request.coffee_type}")

        if make_coffee_request.coffee_type == MakeCoffeeRequest.COFFEE_TYPE_SHORT:
            self.coffee_history.increase_short_coffee()
        elif make_coffee_request.coffee_type == MakeCoffeeRequest.COFFEE_TYPE_MEDIUM:
            self.coffee_history.increase_medium_coffee()
        elif make_coffee_request.coffee_type == MakeCoffeeRequest.COFFEE_TYPE_LONG:
            self.coffee_history.increase_long_coffee()
        else:
            print("CoffeeActuatorResource -> Unsupported Coffee Type -> 4.00 Bad Request")
            return aiocoap.Message(code=aiocoap.BAD_REQUEST)

        return self.notify_new_coffee()
