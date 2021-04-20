"""
This file is the main running program of the file. Thanks to the developers of 
Pyrebase and the luma.core libraries I was able to connect to my database and 
display these messages! 

I tried using the firebase_admin library provided by google but it seemed that 
their api was not designed for ARM so I retired that idea and used Pyrebase instead.

from here I just added this to my /etc/rc.local to run it on boot from my 
Pi zero W

sudo python3 /PATH/display.py

I also had to install pyrebase in the rc.local environment so I added this line

sudo pip3 install pyrebase

before I ran display.py
"""

import time
import pyrebase
import datetime as dt
import RPi.GPIO as GPIO
from cred import getCreds

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

conf = {
    "apiKey" : getCreds(),
    "authDomain" : "text-scroller-ccc3c.firebaseapp.com",
    "databaseURL" : "https://text-scroller-ccc3c-default-rtdb.firebaseio.com/",
    "storageBucket" : "text-scroller-ccc3c.appsop.com",
    "serviceAccount" : "/home/pi/scroller/serviceAccountKey.json"
}

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def main():
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=4, block_orientation=-90,
                     rotate=0, blocks_arranged_in_reverse_order=False)

    UPDATERATE = 10
    today = str(dt.date.today())
    print(today)

    msg = dbFetch(today)
    display(device, msg)

    while(True):
        t = dt.datetime.today()
        if(t.minute%UPDATERATE == 0 and t.second < 5.0):
            today = str(dt.date.today())
            msg = dbFetch(today)

        if(GPIO.input(22) == GPIO.HIGH):
            display(device, msg)
        time.sleep(1)


def dbFetch(date):
    defaultMsg = "Have a good day!"
    try:
        print("fetching")
        fb = pyrebase.initialize_app(conf)
        db = fb.database()

        msg = str(db.child(date).get().val())
        print("received")
        if(msg == "None"):
            return defaultMsg
        return msg
    except request.Timeout:
        return defaultMsg


def show_welcome(device):
    msg = "Hi baby :)"
    show_message(device, msg, fill="white", font=proportional(CP437_FONT))
    time.sleep(1)

def display(device, msg):
    show_message(device, msg, fill="white", font=proportional(CP437_FONT))
    time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
