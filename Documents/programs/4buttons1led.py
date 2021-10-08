#JFC
#Four Buttons, One LED

#Use a module fpr requesting data online
import requests

#Use a module to control time
import time

#Set up for buttons and leds
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering


#Set up each ppin number
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Start an infinite loop
while True:
    #Wait for one second
    time.sleep(1)
    #Check the 1st button
    if GPIO.input(6) == GPIO.LOW:
        print("Button 6 was pressed")
        requests.get("http://192.168.10.53:5000/sfx?file=john_cena")


from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def buildHouse():
    pos = mc.player.getPos()
    mc.setBlocks(pos.x, pos.y, pos.z, pos.x, pos.y, pos.z, blockTypeID)