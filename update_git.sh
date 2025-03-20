#!/bin/bash

# Shell script to update multiple desktop folders and pull code from 
# github. It is called automatedly via crontab every 15 minutes on 
# the quarter hour. 
# Additionally, the last line copies the data folder to Google Drive
# using the rclone client

# Last updated: 2025-03-13
# Authors: Cyrus K.

# Run the entire script with lower CPU and I/O priority
exec nice -n 5 ionice -c 3 bash -c '

# Function to update a repository if it exists
for repo in \
    "/home/blaisdelllab/Desktop/Hardware_Code" \
    "/home/blaisdelllab/Desktop/Experiments/P003e" \
    "/home/blaisdelllab/Desktop/Experiments/P033" \
    "/home/blaisdelllab/Desktop/Experiments/P034" \
    "/home/blaisdelllab/Desktop/Experiments/P035" \
    "/home/blaisdelllab/Desktop/Experiments/P039" 
do
    if [ -d "$repo/.git" ]; then
        echo "Updating $repo..."
        git -C "$repo" reset --hard
        git -C "$repo" pull origin main
    else
        echo "Skipping $repo (not found)."
    fi
done

# Make all .sh and .py scripts in Desktop and its subdirectories executable
find /home/blaisdelllab/Desktop -type f \( -name "*.sh" -o -name "*.py" \) -exec chmod +x {} \;

# Sync Data to Google Drive
rclone copy /home/blaisdelllab/Desktop/Data gdrive:RPiDataBackup
'
