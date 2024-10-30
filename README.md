# Hardware_Code
All the under-the-hood software used for running experimental programs (including hardware tests).


## Experimental code version control w/ Github 
Pushing/pulling - GitHub cloning and data push
### 1. Create an Experiments folder
Within Experiments folder, create another folder with the name of your experiment. This way, you can organize multiple experimental programs in the same place, and makes cloning from GitHub more simplistic.

Go into correct folder to clone
- cd Desktop/Experiments/
- git clone https://github.com/blaisdelllab/P034.git
- Clone folder from GitHub
### 2. Create a new “data” folder back into newly cloned folder
- To make all programs executable, we first need to make update_git.sh executable
cd ..
- Go back to Desktop/Hardware_Code instead of the current path
chmod +x update_git.sh
### 3. Make experimental program executable for each program; include the Hardware_Code .py and .sh files (especially update_git.sh)
- Check experimental is green bold using ls command (means chmod worked)
crontab -e
- Automate update_git.sh file
- Hit “1”
- Don’t need to do every time, only if crontab has never been utilized
- */15 * * * * Desktop/Hardware_Code/update_git.sh
    Spaces are there for a reason
### Troubleshooting
if, at any point, a folder has been cloned into the wrong place, remove directory using this line of code: 
	rm -r Experiment_folder_name
	Hit “y”
Hit “y”
