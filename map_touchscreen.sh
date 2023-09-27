#!/bin/bash

# Define the path to the text file
text_file="/home/blaisdelllab/Desktop/Box_Info/Box_number.txt"

# Read the value from the text file and assign it to a variable
box_number=$(cat "$text_file")

# Check if the variable is not empty (e.g., the file exists and contains a value)
if [ -n "$box_number" ]; then
    # Use the variable in the xinput command
    /usr/bin/xinput map-to-output "$box_number" HDMI-2
else
    # Handle the case where the file is empty or does not exist
    echo "Error: The text file is empty or does not exist."
fi