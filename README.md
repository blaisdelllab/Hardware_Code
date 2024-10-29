# Hardware_Code
All the under-the-hood software used for running experimental programs (including hardware tests).


## Experimental code version control w/ Github 
Pushing/pulling - GitHub cloning and data push
### Create an Experiments folder
Within Experiments folder, create another folder with the name of your experiment. This way, you can organize multiple experimental programs in the same place, and makes cloning from GitHub more simplistic
  cd Desktop/Experiments/
Go into correct folder to clone
  git clone https://github.com/blaisdelllab/P034.git
- Clone folder from GitHub
Create a new “data” folder back into newly cloned folder
To make all programs executable, we first need to make update_git.sh executable
cd ..
Go back to Desktop/Hardware_Code instead of the current path
chmod +x update_git.sh
Make experimental program executable for each program; include the Hardware_Code .py and .sh files (especially update_git.sh)
ls
Check experimental is green bold (means chmod worked)
crontab -e
Automate update_git.sh file
Hit “1”
Don’t need to do every time, only if crontab has never been utilized
Comment: “Below are the crontab commands to automate updating code. Make sure to clone folder first and make the update_git.sh file executable.”
*/15 * * * * Desktop/Hardware_Code/update_git.sh
    Spaces are there for a reason
if, at any point, a folder has been cloned into the wrong place, remove directory using this line of code: 
	rm -r Experiment_folder_name
	Hit “y”
Hit “y”
