from time import sleep
from adafruit_dht import DHT11
import board

SENSOR_PIN = board.D18
DEVICE = DHT11(SENSOR_PIN)

while True:
    try:
        temperature_c = DEVICE.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print("Temp: {:.1f} F    Humidity: {}%"
              .format(temperature_f, humidity))

    except RuntimeError as error:
        # print(error.args[0])

    sleep(2.0)
