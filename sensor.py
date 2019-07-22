from adafruit_dht import DHT11


class Sensor:
    def __init__(self, sensor_pin):
        self.device = DHT11(sensor_pin)

    def readTemperature(self):
        try:
            temperature_c = self.device.temperature
            temperature_f = temperature_c * (9 / 5) + 32
            return temperature_f
        except RuntimeError:
            return 0
    
    def readHumidity(self):
        try:
            return self.device.humidity
        except RuntimeError:
            return 0
