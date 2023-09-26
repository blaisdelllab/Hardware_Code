"""
This is a script to test if we can use the servo motors for pigeon
operant boxes with a Raspberry Pi.

Cyrus Kirkman, Rob Tsai,and Ikponmwosa Pat-Osagie July 13, 2023
"""
# First, import libraries. Make sure to install libraries if not
# previously done...
# sudo apt-get install python3-rpi.gpio
# sudo pip3 install gpiozero

# Import libraries
import RPi.GPIO as GPIO
from time import sleep

# Set mode of the board
GPIO.setmode(GPIO.BOARD)
# Setup pin NOT GPIO number
servo_pin_num = 3
hopper_light_pin_num = 40
house_light_pin_num = 33

GPIO.setup(servo_pin_num,
           GPIO.OUT) # This is the servo motor
GPIO.setup(hopper_light_pin_num,
           GPIO.OUT) # This is the hopper light
GPIO.setup(house_light_pin_num,
           GPIO.OUT) # This is the house light

# # Setup the servo motor
s = GPIO.PWM(servo_pin_num, 50) # Here, 50 MhZ defines the pulse frequency
hopper_up_val = 2
hopper_down_val = 5.5
s.start(0) # Start up Servo with a value of zero (e.g., pulse off)
s.ChangeDutyCycle(hopper_down_val) # Put down

print("Waiting for 1 second")
sleep(2)


# Then turn it back...
s.ChangeDutyCycle(hopper_up_val)
print("Hopper up")
sleep(1)

s.ChangeDutyCycle(hopper_down_val)
print("Hopper down")
sleep(1)
s.ChangeDutyCycle(0) # Stop jitter
    
# Then turn on hopper light
GPIO.output(hopper_light_pin_num,
            True)
print("Hopper light ON")
sleep(2)
GPIO.output(hopper_light_pin_num,
            False)
print("Hopper light OFF")
sleep(1)

# Test house light
GPIO.output(house_light_pin_num,
            True)
print("House light ON")
sleep(30)
GPIO.output(house_light_pin_num,
            False)
print("House light OFF")
# Lastly, make sure to clean up the environment
s.stop()
GPIO.cleanup()
print("Everything is cleaned up")

