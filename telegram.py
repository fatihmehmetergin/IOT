#sudo pip install python-telegram-bot
#sudo pip install telepot
#git clone https://github.com/salmanfarisvp/TelegramBot.git 

import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

#LED
def on(pin):
    GPIO.output(pin,GPIO.HIGH)
    return
def off(pin):
    GPIO.output(pin,GPIO.LOW)
    return
# Pin secimi yapiliyor.
GPIO.setmode(GPIO.BOARD)
# 11.GPIO pini cikis yapiliyor.
GPIO.setup(40, GPIO.OUT)

def msj_gelirse(mesaj):
    chat_id = mesaj['chat']['id']
    komut = mesaj['text']

    print 'Sukur bir komut yolladin: %s' % komut
    if komut == 'Ac':
       bot.sendMessage(chat_id, on(40))
    elif komut =='Kapa':
       bot.sendMessage(chat_id, off(40))

bot = telepot.Bot('1082949995:AAGOh7PUfSC7gLljOg7qB7A1Nnomvkdne30')
bot.message_loop(msj_gelirse)
print ' Komut bekliyorum, artik yollayacak misin ?'

while 1:
     time.sleep(10)
