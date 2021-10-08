
#Set up for buttons and leds
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering

from mcpi.minecraft import Minecraft
mc = Minecraft.create()


#Set up each ppin number
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def buildHouse():
    pos = mc.player.getPos()
    mc.setBlocks(pos.x + 1, pos.y, pos.z + 1, pos.x + 5, pos.y + 5, pos.z + 5, 1)
    mc.setBlocks(pos.x + 2, pos.y + 1, pos.z + 2, pos.x + 5, pos.y + 4, pos.z + 5, 0)
    mc.setBlocks(pos.x + 3, pos.y + 1, pos.z + 1, pos.x + 3, pos.y + 2, pos.z + 1, 64)
    

#Start an infinite loop
while True:

    #Check the 1st button
    if GPIO.input(6) == GPIO.LOW:
        print("Button 6 was pressed")
        buildHouse()



