# Wildlife camera Project Code
# Made by Erin and Anika
# Start Date: 8:48am 3/13/2018 End Date:
# This project is to make a camera that will take pictures of wildlife.

# Import libraies
import time
import RPi. GPIO as GPIO
from picamera import PiCamera 
#functions go here


# Button and On/off LED
# Varibles for button pins
button_pin1 = 6
LED_pin= 17
PIR_pin = 12
camera_on = False
frame = 1

#Setup GPIO for  (Button, led, PIR, Ir leds(later))
GPIO.setmode(GPIO.BCM)
GPIO.setup (button_pin1, GPIO.IN)
GPIO.setup (PIR_pin, GPIO.IN)
GPIO.setup (LED_pin, GPIO.OUT)



# Infa Red LEDs:




# Setup Camera:

camera = PiCamera()



# Setup PIR:
GPIO.setmode (GPIO.BCM)
PIR = 12
GPIO.setup(PIR, GPIO.IN)


# Main Program

# Loop Forever
while True:
    #Toggle on and of the motion-senseing using the buttonwhile True:
    if GPIO.input(button_pin1) == True:
        print ("button pressed")
        #if true, set to false, if false, set to true
        if camera_on == True:
            camera_on = False
        else:
            camera_on = True
        print ("camera on", camera_on)
            
    # If motion detected
    if camera_on == True and GPIO.input(PIR_pin):
        try:
            # Create the files (should increment, 
            # Take picture or video
            camera.capture('/home/pi/wild-cam-pics/frame%03d.jpg' %frame)
            frame +=1
        except:
            print ("failure to take a picture >:q")
    if camera_on == True:
        GPIO.output (LED_pin, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output (LED_pin, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output (LED_pin, GPIO.LOW)
        
        

    #pause

        time.sleep (0.3)
        
    
# Loop back
    
