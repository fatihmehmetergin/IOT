from gpiozero import LED
import paho.mqtt.client as mqtt
from time import sleep
import sys
import Adafruit_DHT
led = LED (21)
def baglanti_saglandiginda(client, userdata, flags, rc):
    print ('Baglandi, rc' + str(rc))
def mesaj_geldiginde(client, userdata, msg):
    mesaj = msg.payload
def onPublish(client, userdata, result):
    print ('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity), '  published')
istemci = mqtt.Client()
istemci.on_connect = baglanti_saglandiginda
istemci.on_message = mesaj_geldiginde
istemci.on_publish = onPublish
istemci.username_pw_set("----USERNAME------", "------------------AIO KEY----------------------------") 
istemci.connect("io.adafruit.com", port = 1883)
while True:
    istemci.loop_start()
    humidity, temperature =Adafruit_DHT.read_retry(11, 2)
    istemci.publish('----------/feeds/sicaklik', temperature)
    istemci.publish('----------/feeds/nem', humidity)
    led.on()
    sleep(10)
    led.off()
    istemci.loop_stop()# publish metodu kullanilirken loop_forever() kullanilamaz
