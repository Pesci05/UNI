# For this laboratory we rely on the aiocoap library (0.4.x) - https://github.com/chrysn/aiocoap
# Dependencies are managed with uv. From the project root run: uv run coffee-machine-server
#
# CoAP Server of the Coffee Machine exposing three resources:
# - /temperature: Temperature Sensor (GET)
# - /capsule: Capsule Presence Sensor (GET)
# - /coffee: Coffee Actuator (GET, POST, PUT), observable

from coap_laboratory.config.config_manager import ConfigManager
from coap_laboratory.resources.capsule_presence_sensor_resource import CapsulePresenceSensorResource
from coap_laboratory.resources.coffee_actuator_resource import CoffeeActuatorResource
from coap_laboratory.resources.temperature_sensor_resource import TemperatureSensorResource
import aiocoap
import aiocoap.resource as resource
import asyncio
import logging


async def run_server(config_manager: ConfigManager) -> None:

    # Resource tree creation: each resource is registered on its path
    root = resource.Site()
    root.add_resource(["temperature"], TemperatureSensorResource())
    root.add_resource(["capsule"], CapsulePresenceSensorResource())
    root.add_resource(["coffee"], CoffeeActuatorResource())

    # Create the server context bound to the configured address and UDP port
    await aiocoap.Context.create_server_context(root, bind=(config_manager.server_bind_host, config_manager.server_port))

    print(f"Coffee Machine CoAP Server listening on coap://{config_manager.server_bind_host}:{config_manager.server_port}")

    # Keep the server running forever: the requests are served by the event loop (CTRL+C to stop the process)
    await asyncio.get_running_loop().create_future()


def main() -> None:

    # Log level of aiocoap: INFO shows the main events, DEBUG also shows every received and sent message
    logging.basicConfig(level=logging.INFO)
    # logging.getLogger("coap-server").setLevel(logging.DEBUG)

    # Load the shared configuration (bind address and port of the server) from the config.yaml file
    config_manager = ConfigManager()

    try:
        asyncio.run(run_server(config_manager))
    except KeyboardInterrupt:
        print("Coffee Machine CoAP Server stopped")


if __name__ == "__main__":
    main()
