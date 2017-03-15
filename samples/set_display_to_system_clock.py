#!/bin/python
# Sample script to shut down the raspberry Pi Compute Module when the Shutdown Signal from the display goes low.


import RPi.GPIO as GPIO
import time
import os


# Configure with Internal pullups enabled and to read mode.
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# Perform this when the event is triggered
def Shutdown(channel):
    print "shutdown the system..."
    #GPIO.cleanup()
    #os.system("sudo shutdown -h now")


# Add the function to execute when the Shutdown Signal is set low
GPIO.add_event_detect(23, GPIO.FALLING, callback=Shutdown, bouncetime=100)

# Wait for an event
while 1:
    time.sleep(1)
                                                                                                                                                                                                                    