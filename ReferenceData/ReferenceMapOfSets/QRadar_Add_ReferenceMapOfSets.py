""" QRadar Reference Map of Sets: Add example """
import configparser
import json
import urllib.parse
import requests

config = configparser.ConfigParser()
config.read("../../config.ini")
IP = config.get("SIEM", "IP")
KEY = config.get("SIEM", "Key")

BASE_URL = "https://" + IP + "/api/reference_data/map_of_sets/DEMO_MAP_OF_SETS?"

# We need to pass our Authentication token to the post method.
# Find it at: Console -> Admin -> Authorized Services '''
headers = {
    'SEC': KEY
}

# Create a dict for the key/value pair we are passing.
parameters = {
    'key': 'stah06',
    'value': '111-222-3333'
}

url = BASE_URL + urllib.parse.urlencode(parameters)
json_data = requests.post(url, headers=headers, verify=False).json()
print(json.dumps(json_data, indent=2))
