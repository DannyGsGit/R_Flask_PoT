# Test Script

# Purpose: Test the Flask API using this script



import requests, json

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#### Step 1: Start the service!!! ####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Be sure to start the webservice with:
# $ python *app_api_name*.py



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#### Step 2: Submit a JSON request ####
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Define the API endpoint
url = "http://localhost:9000/summer"

# Sample data
data = json.dumps(['1', '1', '42'])

# POST request
r = requests.post(url, data)

print(r.json())


