class TemperatureSensor:
    def __init__(self, temperature):
        self.temperature = temperature  

    def verify_temperature(self):
        """ Verify if the temperature is valid. Raises an exception if the temperature is negative or above a certain threshold. """
        if self.temperature < 0:
            raise ValueError("Temperature cannot be negative.")
        elif self.temperature > 100:
            raise ValueError("Temperature exceeds valid range.")
        return True

class Logger:
    @staticmethod
    def log(message):
        """ Log a message to the console. """
        print(message)

if __name__ == '__main__':
    # Example usage
    temp = 25  # You can change this to test other values
    sensor = TemperatureSensor(temp)
    logger = Logger()
    try:
        if sensor.verify_temperature():
            logger.log(f"Temperature {temp} is valid.")
    except ValueError as e:
        logger.log(f"Error: {e}")