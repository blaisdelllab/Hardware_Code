#!/bin/bash

# Shell script to update multiple desktop folders and pull code from 
# github. It is called automatedly via crontab every 15 minutes on 
# the quarter hour. 
# Authors: Cyrus K. & Robert T.


# Hardware_Code Repository
# cd Desktop
#git reset --hard
#git pull origin main
#chmod +x Hardware_test.py
#chmod +x hopper_slider.py
#chmod +x map_touchscreen.sh
#chmod +x run_HardwareTest.sh
#chmod +x touchscreenMappingShellScriptName

# P003e Repository
cd Desktop/Experiments/P003e
git reset --hard
git pull origin main
chmod +x P003E_ExpProgram_RP.py

# P033 Repository
cd Desktop/Experiments/P033
git reset --hard
git pull origin main


# P034 Repository
cd Desktop/Experiments/P034
git reset --hard
git pull origin main
chmod +x P034_ExpProgram_RP.py

# P035 Repository
cd Desktop/Experiments/P035
git reset --hard
git pull origin main
chmod +x P035_FOAM_ExpProgram_RPi.py