import sys
import Adafruit_DHT
import requests
import time
from time import sleep

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 2)
    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
    data = requests.get("https://maker.ifttt.com/trigger/sicaklikNemYaz/with/key/bERDUgCMyLRcsdZFeKnP2Q",params={"value1": temperature, "value2": humidity})
    sleep(60)
