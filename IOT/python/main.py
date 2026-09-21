def read_temperature():
    return 21.5

def main() -> None:
    print("Running sensor_utils.py directly - starting the sensor loop...")
    print(read_temperature())


if __name__ == "__main__":
    main()
