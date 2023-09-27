#!/bin/bash

# This shell script maps the touchscreen to a single screen (HDMI-2). However,
# given that some touchscreens are named different things, we need to store
# that name in a text file under box info for this to work.

# Define the path to the text file
text_file="/home/blaisdelllab/Desktop/Box_Info/Touchscreen_Name.txt"

# Read the value from the text file and assign it to a variable
touchscreen_name=$(cat "$text_file")

# Check if the variable is not empty (e.g., the file exists and contains a value)
if [ -n "$touchscreen_name" ]; then
    # Use the variable in the xinput command
    /usr/bin/xinput map-to-output "$touchscreen_name" HDMI-2
else
    # Handle the case where the file is empty or does not exist
    echo "Error: The text file is empty or does not exist."
fi