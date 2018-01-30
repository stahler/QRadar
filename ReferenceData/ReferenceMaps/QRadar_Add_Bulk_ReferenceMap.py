""" QRadar Reference Map: Bulk load example """

import json
import configparser
import requests

config = configparser.ConfigParser()
config.read("../../config.ini")
IP = config.get("SIEM", "IP")
KEY = config.get("SIEM", "Key")

BASE_URL = "https://" + IP + "/api/reference_data/maps/bulk_load/DEMO_MAP?"

# We need to pass our Authentication token to the post method.
# Find it at: Console -> Admin -> Authorized Services '''
headers = {
    'SEC': KEY
}

# Create a dict for the elements we are passing.
# In the "create" case, we are passing the name of the reference set
# and the type (IP)
payload = {
    'stah06':'Wes Stahler',
    'home01':'Homer Simpson',
    'blan01':'Gern Blanston',
    'Gold01': 'Bucky Goldstein',
}

url = BASE_URL
json_data = requests.post(url, data=json.dumps(payload), headers=headers, verify=False).json()
print(json.dumps(json_data, indent=2))
