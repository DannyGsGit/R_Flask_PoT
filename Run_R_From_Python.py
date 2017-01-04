## Start an R subprocess from Python

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#### Import dependencies ####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import subprocess



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#### Run the hello world R script ####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Define the arguments
filetype = 'Rscript'
R_script_path = './Hello_World.R'

command = [filetype, R_script_path]

# Run the command
x = subprocess.check_output(command, universal_newlines = True)




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#### Pass arguments into an R script ####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





#~~~~~~~~~~~~~~~
#### Sample ####
#~~~~~~~~~~~~~~~
# http://www.mango-solutions.com/wp/2015/10/integrating-python-and-r-part-ii-executing-r-from-python-and-vice-versa/

# run_max.py
# import subprocess

# Define command and arguments
# command = 'Rscript'
# path2script = 'path/to your script/max.R'

# Variable number of args in a list
# args = ['11', '3', '9', '42']

# Build subprocess command
# cmd = [command, path2script] + args

# check_output will run the command and store to result
# x = subprocess.check_output(cmd, universal_newlines=True)

# print('The maximum of the numbers is:', x)