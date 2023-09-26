#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 17:07:29 2022

This program was created to ensure the different components (touchscreen,
lights, hopper) of the Touchscreen Operant Chambers are callibrated before
running pigeon experiments. By verifying each element is running properly
beforehand, we can better look after the integrity of our experiments.


Updates:
- Ibrahim Y. on October 25, 2022
- Rob T. on July 7, 2023
- Cyrus K. for RPi/1024x768p on September 9, 2023 

By Michael Nirula, Ibrahim Y., Cyrus K., Rob T.
@author: michaelnirula
"""

# Download packages
from tkinter import Canvas, Tk, BOTH
from os import popen, path as os_path
from sys import path as sys_path
import random #imports the random module
# import RPi.GPIO as GPIO
from time import sleep
from gpiozero import Servo
import pigpio
import csv

# First is declare whether we're running a version on operant boxes or our
# individual machines
operant_box_version = True

root = Tk() #This creates the root to reference
root.title("Test Hardware") # Creates the root title/title of the file

# This creates the geometry of the gui, depending on version
if operant_box_version:
    popen("sh /home/blaisdelllab/Desktop/Hardware_Code/map_touchscreen.sh") # Map touchscreen to operant box monitor
    root.geometry("1024x768+1024+0") #  needs to be changed
    root.attributes('-fullscreen',
                    True)
    canvas_1 = Canvas(root,
                      bg="black")
    canvas_1.pack(fill = BOTH,
                  expand = True)
    #set up GPIO number NOT pin (pigpio only compatible with GPIO num)
    servo_GPIO_num = 2
    hopper_light_GPIO_num = 13
    house_light_GPIO_num = 21

    # Setup use of pi()
    rpi_board = pigpio.pi()

    # set each pin to output
    rpi_board.set_mode(servo_GPIO_num, pigpio.OUTPUT)
    rpi_board.set_mode(hopper_light_GPIO_num, pigpio.OUTPUT)
    rpi_board.set_mode(house_light_GPIO_num, pigpio.OUTPUT)

    # Setup the servo motor
    rpi_board.set_PWM_frequency(servo_GPIO_num, 50) # Here, 50 MhZ defines the pulse frequency

    # Setting up the path of the csv file that holds up/down values
    hopper_vals_csv_path = str(os_path.expanduser('~')+"/Desktop/Box_Info/Hopper_vals.csv")

    # Store the proper UP/DOWN values for the hopper from csv file
    up_down_table= list(csv.reader(open(hopper_vals_csv_path)))

    # using indexing to assign up/down values to corresponding variables
    hopper_up_val = up_down_table[1][0]
    hopper_down_val = up_down_table[1][1]
else:
    root.geometry("1024x768")
    #This creates a black canvas with dimensions of height=600 and width=800
    canvas_1 = Canvas(root,
                      bg="black",
                      height=768,
                      width=1024)
    canvas_1.pack()

seconds_remaining = 3 #Sets the final timer to start at 3 seconds
#%% This section creates onscreen objects

# The following list includes all 9 coordinates of the potential shape locations
# that we will want to test in the box. During the program, two will be
# quasi-randomly selected and presented to test the touchscreen.
coordinate_list=[[150, 150, 225, 225], #TOP LEFT
                 [475, 150, 550, 225], #TOP MIDDLE
                 [775, 150, 850, 225], #TOP RIGHT
                 [150, 350, 225, 425], #MIDDLE LEFT
                 [475, 350, 550, 425], #MIDDLE MIDDLE
                 [775, 350, 850, 425], #MIDDLE RIGHT
                 [150, 600, 225, 675], #BOTTOM LEFT
                 [475, 600, 550, 675], #BOTTOM MIDDLE
                 [775, 600, 550, 675], #BOTTOM RIGHT
                 ]

a=random.sample(coordinate_list,
                k=1) #Choose one of the coordinates randomly without replacement
b=random.sample(coordinate_list,
                k=1) #Choose one of the coordinates randomly without replacement

while (a[0][0]==b[0][0] or a[0][1]==b[0][1]):
    b=random.sample(coordinate_list, k=1) #This while loop will make sure that the two sets of coordinates will not have the same x or y coordiantes.

#color is randomized for these 2 shapes.
shape_1 = canvas_1.create_rectangle(a,
                         fill="#"+("%06x"%random.randint(0,16777215)),
                         outline="white",
                         tag="shape_1")

shape_2 = canvas_1.create_rectangle(b,
                          fill="#"+("%06x"%random.randint(0,16777215)),
                          outline="white",
                          tag="shape_2")

#Links text to shape 1 using and if else statement. We have 9 total shapes in
# the list with a total of 3 x coordinates. This will center the text above the
# chosen x coordinate.
if a[0][0]==100:
    guidetext= canvas_1.create_text(a[0][0]+150,
                                    a[0][1]-25,
                                    text="Please click any shapes to test touchscreen :D",
                                    font=("Helvetica", 20, "italic"),
                                    fill="white",)
elif a[0][0]==375:
    guidetext= canvas_1.create_text(a[0][0]+40,
                                    a[0][1]-25,
                                    text="Please click any shapes to test touchscreen :D",
                                    font=("Helvetica", 20, "italic"),
                                    fill="white")
else:
    guidetext= canvas_1.create_text(a[0][0]-70,
                                    a[0][1]-25,
                                    text="Please click any shapes to test touchscreen :D",
                                    font=("Helvetica", 24, "italic"),
                                    fill="white",)

touchscreenworks = canvas_1.create_text(512, 384,
                                        text="Touch-Screen Works!",
                                        font=("Helvetica", 26),
                                        fill="white")

hopper_light_text_on = canvas_1.create_text(512, 384,
                                      text="Hopper Light ON",
                                      font=("Helvetica", 38, "italic"),
                                      fill="yellow")

hopper_light_text_off = canvas_1.create_text(512, 384,
                                       text="Hopper Light OFF",
                                       font=("Helvetica", 38, "italic"),
                                       fill="yellow")

house_light_text_on = canvas_1.create_text(512, 384,
                                      text="House Light ON",
                                      font=("Helvetica", 38, "italic"),
                                      fill="yellow")

house_light_text_off = canvas_1.create_text(512, 384,
                                       text="House Light OFF",
                                       font=("Helvetica", 38, "italic"),
                                       fill="yellow")

hopper_text_on = canvas_1.create_text(512, 384,
                                      text="Hopper UP",
                                      font=("Helvetica", 38, "italic"),
                                      fill="red")

hopper_text_off = canvas_1.create_text(512, 384,
                                       text="Hopper DOWN",
                                       font=("Helvetica", 38, "italic"),
                                       fill="red")

success_text = canvas_1.create_text(450, 300,
                                    text=f"All Systems Go! \nScreen will self-destruct in:\n    {seconds_remaining} seconds",
                                    font=("Terminal",
                                          30),
                                    fill="green")

# Hides future objects for default (beginning)
canvas_1.itemconfigure(shape_2, state='hidden')
canvas_1.itemconfigure(touchscreenworks, state='hidden')
canvas_1.itemconfigure(hopper_light_text_on, state='hidden')
canvas_1.itemconfigure(hopper_light_text_off, state='hidden')
canvas_1.itemconfigure(house_light_text_on, state='hidden')
canvas_1.itemconfigure(house_light_text_off, state='hidden')
canvas_1.itemconfigure(hopper_text_on, state='hidden')
canvas_1.itemconfigure(hopper_text_off, state='hidden')
canvas_1.itemconfigure(success_text, state='hidden')

#%% FUNCTIONS
#this creates rectangle 2 on canvas and deletes rectangle 1 thereby
#testing the touchscreen
def rectangle1_pressed():
    print("First rectangle was pressed")
    canvas_1.itemconfigure(shape_2,
                           state='normal')
    canvas_1.itemconfigure(shape_1,
                           state='hidden')
    canvas_1.itemconfigure(guidetext,
                           state='hidden')

#This hides rectangle 2 and displays text indicating the touchscreen works
# before deleting it

def rectangle2_pressed(*args):
    print("Second rectangle was pressed")
    canvas_1.itemconfigure(shape_2,
                           state='hidden')
    canvas_1.itemconfigure(touchscreenworks,
                           state='normal')
    root.after(1500,
               hopper_light_on)

def hopper_light_on():
    rpi_board.write(hopper_light_GPIO_num,
                True)
    canvas_1.itemconfigure(touchscreenworks,
                           state='hidden')
    canvas_1.itemconfigure(hopper_light_text_on,
                           state='normal')
    root.after(3000,
               hopper_light_off)

def hopper_light_off():
    rpi_board.write(hopper_light_GPIO_num,
                False)
    canvas_1.itemconfigure(hopper_light_text_on,
                           state='hidden')
    canvas_1.itemconfigure(hopper_light_text_off,
                           state='normal')
    root.after(1000,
               house_light_on)

def house_light_on():
    rpi_board.write(house_light_GPIO_num,
                True)
    canvas_1.itemconfigure(hopper_light_text_off,
                           state='hidden')
    canvas_1.itemconfigure(house_light_text_on,
                           state='normal')
    root.after(2500,
               house_light_off)

def house_light_off():
    rpi_board.write(house_light_GPIO_num,
                False)
    canvas_1.itemconfigure(house_light_text_on,
                           state='hidden')
    canvas_1.itemconfigure(house_light_text_off,
                           state='normal')
    root.after(1000,
               hopper_on)

def hopper_on():
    canvas_1.itemconfigure(house_light_text_off,
                           state='hidden')
    canvas_1.itemconfigure(hopper_text_on,
                           state='normal')
    rpi_board.set_servo_pulsewidth(servo_GPIO_num, hopper_up_val)
    root.after(3000,
               hopper_off)

def hopper_off():
    canvas_1.itemconfigure(hopper_text_on,
                           state='hidden')
    canvas_1.itemconfigure(hopper_text_off,
                           state='normal')
    rpi_board.set_servo_pulsewidth(servo_GPIO_num, hopper_down_val)
    root.after(1000,
               all_systems_go)

def all_systems_go():
    rpi_board.set_PWM_dutycycle(servo_GPIO_num, 0)
    rpi_board.set_PWM_frequency(servo_GPIO_num, 0)
    canvas_1.itemconfigure(hopper_text_off,
                           state='hidden')
    canvas_1.itemconfigure(success_text,
                           state='normal')
    root.after(1000,
               start_countdown)

def start_countdown():
    global seconds_remaining, success_text, s
    if seconds_remaining > 0:
        canvas_1.itemconfigure(success_text,
                               state='hidden')
        success_text = canvas_1.create_text(450, 300,
                                    text=f"All Systems Go! \nScreen will self-destruct in:\n    {seconds_remaining} seconds",
                                    font=("Terminal",
                                          30),
                                    fill="green")
        seconds_remaining -= 1
        root.after(1000,
                   start_countdown)
    else:
        root.destroy()
        rpi_board.set_PWM_dutycycle(servo_GPIO_num, 0)
        rpi_board.set_PWM_frequency(servo_GPIO_num, 0)
        rpi_board.stop()



#%% TAGGING FUNCTIONS
canvas_1.tag_bind("shape_1",
                  "<Button-1>",
                  lambda event: rectangle1_pressed())

canvas_1.tag_bind("shape_2",
                  "<Button-1>",
                  lambda event: rectangle2_pressed())

#%% Finally, this is the mainloop
try:
    root.mainloop()
except:
    rpi_board.set_PWM_dutycycle(servo_GPIO_num, 0)
    rpi_board.set_PWM_frequency(servo_GPIO_num, 0)
    rpi_board.stop()