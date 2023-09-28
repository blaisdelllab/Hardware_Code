#!/bin/bash

# This script callibrates the touchscreens

# Check if running as root, if not, exit
if [ "$EUID" -ne 0 ]; then
    echo "Please run this script as root using sudo."
    exit 1
fi

# Install libts-bin
apt update
apt install libts-bin -y

# Set environment variables
export tslib_tsdevice=/dev/input/event0
export tslib_fbdevice=/dev/fb1

# Run ts_calibrate
ts_calibrate