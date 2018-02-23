""" QRadar Reference Map of Sets: Add bulk example """
import configparser
import json
import requests

config = configparser.ConfigParser()
config.read("../../config.ini")
IP = config.get("SIEM", "IP")
KEY = config.get("SIEM", "Key")

BASE_URL = "https://" + IP + "/api/reference_data/map_of_sets/bulk_load/DEMO_MAP_OF_SETS"

# We need to pass our Authentication token to the post method.
# Find it at: Console -> Admin -> Authorized Services '''
headers = {
    'SEC': KEY
}

# Create a dict for the elements we are passing.
payload = {
    "stah06": ["stahler.2", "Wes.Stahler", "01233210"],
    "stah04": ["stahler.3", "Kris.Stahler", "02129988"],
}

url = BASE_URL
json_data = requests.post(url, data=json.dumps(payload), headers=headers, verify=False).json()
print(json.dumps(json_data, indent=2))
