#!/bin/bash

# Shell script sync Data folder to Google Drive
# using the rclone client

# Last updated: 2025-09-30
# Authors: Cyrus K.

# Run the entire script with lower CPU and I/O priority
exec nice -n 5 ionice -c 3 bash -c '
# Sync Data to Google Drive
rclone copy /home/blaisdelllab/Desktop/Data gdrive:RPiDataBackup
'
