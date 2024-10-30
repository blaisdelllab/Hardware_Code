# Hardware_Code
All the under-the-hood software used for running experimental programs (including hardware tests).


## Experimental code version control w/ Github - Pushing/pulling
Brief walkthrough of adding a new Experiment:
### 1. Create an Experiments folder (if it does not currently exist)
Within Experiments folder, create another folder with the name of your experiment. This way, you can organize multiple experimental programs in the same place, and makes cloning from GitHub more simplistic.

Navigate into correct folder to clone
- cd Desktop/Experiments/
- "git clone https://github.com/blaisdelllab/P034.git" (Note that this is an example directory that will clone existing folder from GitHub)
### 2. Create a new “data” folder back into newly cloned folder
- To make all programs executable, we first need to make update_git.sh executable
- cd ..
- Go back to Desktop/Hardware_Code instead of the current path
### 3. Make experimental program executable for each program; include the Hardware_Code .py and .sh files (especially update_git.sh)
- Terminal command: "chmod +x update_git.sh"
- Check experimental has changed to green bold using ls command (means chmod worked)
### 3. - Automate update_git.sh file 
- Terminal command: crontab -e
- Hit “1”
- Don’t need to do every time, only if crontab has never been utilized
- */15 * * * * Desktop/Hardware_Code/update_git.sh
    Spaces are there for a reason
### Troubleshooting
if, at any point, a folder has been cloned into the wrong place, remove directory using this line of code: 
	rm -r Experiment_folder_name
	Hit “y”
Hit “y”
