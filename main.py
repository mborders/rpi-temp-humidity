from time import sleep
from sensor import Sensor
import config

sensor = Sensor(config.SENSOR_PIN)

while True:
    t = sensor.readTemperature()
    h = sensor.readHumidity()
    print("Temp: {:.1f} F    Humidity: {}%".format(t, h))

    sleep(2.0)
