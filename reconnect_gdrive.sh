#!/bin/bash

# Shell script to manually refresh the 
# connection between rclone and Google
# Drive. After double-click, it should
# pull up a web browser for a manual
# re-login to the drive and refresh the 
# API token.

# Last updated: 2023-10-13
# Authors: Cyrus K.

rclone config reconnect gdrive: --auto-confirm