# For this laboratory we rely on the aiocoap library (0.4.x) - https://github.com/chrysn/aiocoap
# Dependencies are managed with uv. From the project root run: uv run coffee-get-client [resource_path]
#
# Test client sending a GET request to a resource of the Coffee Machine.
# The path of the resource can be passed as argument: temperature (default), capsule or coffee.

from coap_laboratory.config.config_manager import ConfigManager
import aiocoap
import asyncio
import logging
import sys

# Configuration variables
default_resource_path = "temperature"


async def send_get_request(config_manager: ConfigManager, resource_path: str) -> None:

    context = await aiocoap.Context.create_client_context()

    target_uri = config_manager.build_server_uri(resource_path)
    request = aiocoap.Message(code=aiocoap.GET, uri=target_uri)
    print(f"Sending GET request to: {target_uri}")

    try:
        response = await context.request(request).response
    except Exception as e:
        print(f"Failed to fetch resource: {e}")
    else:
        print(f"Response Code: {response.code}")
        print(f"Payload: {response.payload.decode('utf-8')}")
    finally:
        await context.shutdown()


def main() -> None:

    logging.basicConfig(level=logging.INFO)

    # Load the shared configuration (target server host and port) from the config.yaml file
    config_manager = ConfigManager()

    resource_path = sys.argv[1] if len(sys.argv) > 1 else default_resource_path

    asyncio.run(send_get_request(config_manager, resource_path))


if __name__ == "__main__":
    main()
