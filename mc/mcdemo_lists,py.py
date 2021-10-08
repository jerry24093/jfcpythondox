#JFC
#Places a randomly colored wool block

'''
Set up program for MC and two buttons
Create a 'counter' variable that starts at 0
Create a list of blockdata numbers for different color wool
Define a function called placeNext
     - it takes one argument called direction
     - it changes the counter by adding the direction argument
     - place a wool block of the color from the list where the index matches the counter variable
     - if the counter is out of bounds of the index, reset it
in a forever loop:
     - if the first button was pressed, placeNext(1)
     - if the second button was pressed, placeNext(-1)
     '''
#Set up for buttons and leds
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
#Set up each ppin number
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
counter = 0
woolColors = [6, 5, 10]
def placeNext(direction):
    global counter
    counter += direction
    if counter > 2:
        counter = 0
    elif counter < 0:
        counter = 2
    mc.setBlock(72, 0, 124, 35, woolColors[counter])
#Start an infinite loop
while True:

    #Check the 1st button
    if GPIO.input(6) == GPIO.LOW:
        placeNext(1)
    if GPIO.input(13) == GPIO.LOW:
        placeNext(-1)