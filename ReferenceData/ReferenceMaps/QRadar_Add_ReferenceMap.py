""" QRadar Reference Map: Add example """
import configparser
import urllib.parse
import json
import requests

config = configparser.ConfigParser()
config.read("../../config.ini")
IP = config.get("SIEM", "IP")
KEY = config.get("SIEM", "Key")

BASE_URL = "https://" + IP + "/api/reference_data/maps/DEMO_MAP?"

# We need to pass our Authentication token to the post method.
# Find it at: Console -> Admin -> Authorized Services '''
headers = {
    'SEC': KEY
}
# Create a dict for the elements we are passing.
# In the "create" case, we are passing the name of the reference set
# and the type (IP)
parameters = {
    'key': 'Hill01',
    'value': 'Benny Hill'
}

url = BASE_URL + urllib.parse.urlencode(parameters)

json_data = requests.post(url, headers=headers, verify=False).json()
print(json.dumps(json_data, indent=2))
