# R API through Python



#~~~~~~~~~~~~~~~~~~~~~~~~
#### Import packages ####
#~~~~~~~~~~~~~~~~~~~~~~~~

# Python libraries
import pandas as pd
from flask import Flask, request, abort, jsonify
import json
import sys
import subprocess



#~~~~~~~~~~~~~~~~~~~~~~~~~
#### Define Flask API ####
#~~~~~~~~~~~~~~~~~~~~~~~~~

app = Flask(__name__)

@app.route('/summer', methods=['POST'])
def make_dictionary():
    # all kinds of error checking should go here
    data = request.get_json(force = True)
    print('Request received, sit tight...', file=sys.stderr)


    ##################################################
    #### Pass arguments to R and receive response ####
    ##################################################
    ## Define the arguments
    filetype = 'Rscript'
    R_script_path = './R_Code/Simple_Add.R'

    ## Build the command
    command = [filetype, R_script_path] + data  # Note the appending of args to our call out to R

    ## Run the command
    r_output = subprocess.check_output(command, universal_newlines = True)
    
    ##################################################
    
    
    # Return result
    output = json.dumps(r_output)
    return jsonify(output)

if __name__ == '__main__':
    app.run(port = 9000, debug = True)