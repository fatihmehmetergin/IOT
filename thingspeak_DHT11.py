# VCC 1, GND 6, Sign 3

import RPi.GPIO as GPIO
import sys
import Adafruit_DHT
import urllib
from time import sleep

API_KEY = "155SMRKTO3TNWCYK"

GPIO.setmode(GPIO.BCM)

while True:
	humidity, temperature = Adafruit_DHT.read_retry(11, 2)
	print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
	
	istek = urllib.urlopen("https://api.thingspeak.com/update?api_key={}&field1={}&field2={}". format(API_KEY ,temperature, humidity))
	
	sleep(10)
