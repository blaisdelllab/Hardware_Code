#!/bin/bash

# Shell script to update multiple desktop folders and pull code from 
# github. It is called automatedly via crontab every 15 minutes on 
# the quarter hour. 
# Additionally, the last line copies the data folder to Google Drive
# using the rclone client

# Last updated: 2023-09-28
# Authors: Cyrus K. & Robert T.


# Hardware_Code Repository
cd /home/blaisdelllab/Desktop/Hardware_Code
git reset --hard
git pull origin main
chmod +x Hardware_test.py
chmod +x hopper_slider.py
chmod +x map_touchscreen.sh
chmod +x calibrate_touchscreen.sh
chmod +x update_git.sh

# P003e Repository
cd /home/blaisdelllab/Desktop/Experiments/P003e
git reset --hard
git pull origin main
chmod +x P003E_ExpProgram_RP.py

# P033 Repository
cd /home/blaisdelllab/Desktop/Experiments/P033
git reset --hard
git pull origin main


# P034 Repository
cd /home/blaisdelllab/Desktop/Experiments/P034
git reset --hard
git pull origin main
chmod +x P034_ExpProgram_RP.py

# P035 Repository
cd /home/blaisdelllab/Desktop/Experiments/P035
git reset --hard
git pull origin main
chmod +x P035_FOAM_ExpProgram_RPi.py

# Lastly, update the Google Drive data folder. This is done using
# a rclone client–specifically the "copy" function, which scans
# both the source (local folder) and destination (remote folder)
# and uploads only the files that are new or have changed since
#the last synchronization. This means it doesn't re-upload every
# existing file and, perhaps most importantly, means it CANNOT
# DELETE EXISTING FILES.
rclone copy /home/blaisdelllab/Desktop/Data gdrive:RPiDataBackup
