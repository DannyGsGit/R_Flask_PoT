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

# Build the command
command = [filetype, R_script_path]

# Run the command
x = subprocess.check_output(command, universal_newlines = True)




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#### Pass arguments into an R script ####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Define the arguments
filetype = 'Rscript'
R_script_path = './Simple_Add.R'
args = ['1', '1', '40']  # These are the args we want to pass into R

# Build the command
command = [filetype, R_script_path] + args  # Note the appending of args to our call out to R

# Run the command
x_args = subprocess.check_output(command, universal_newlines = True)









#~~~~~~~~~~~~~~~~~~~
#### References ####
#~~~~~~~~~~~~~~~~~~~
# http://www.mango-solutions.com/wp/2015/10/integrating-python-and-r-part-ii-executing-r-from-python-and-vice-versa/
