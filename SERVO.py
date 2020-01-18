from gpiozero import LED
import paho.mqtt.client as mqtt
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
pwm=GPIO.PWM(18, 50)
pwm.start(0)
def SetAngle(angle):
        duty = float(angle)/18+2
print(duty)
       GPIO.output(40, True)
       pwm.ChangeDutyCycle(duty)
       sleep(1)
       GPIO.output(40, False)
       pwm.ChangeDutyCycle(0)
def baglanti_saglandiginda(client, userdata, flags, rc):
print("Baglandi, rc:" + str(rc))
        client.subscribe("", 0)
def mesaj_geldiginde(client, userdata, msg):
        derece = msg.payload
        SetAngle(derece)
istemci = mqtt.Client()
istemci.on_connect = baglanti_saglandiginda
istemci.on_message = mesaj_geldiginde
istemci.username_pw_set("", "")
istemci.connect("io.adafruit.com", port=1883)
istemci.loop_forever()
