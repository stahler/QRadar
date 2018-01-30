""" QRadar Reference Map: list example """
import configparser
import json
import requests

config = configparser.ConfigParser()
config.read("../../config.ini")
IP = config.get("SIEM", "IP")
KEY = config.get("SIEM", "Key")

BASE_URL = "https://" + IP + "/api/reference_data/maps/DEMO_MAP"

# We need to pass our Authentication token to the post method.
# Find it at: Console -> Admin -> Authorized Services '''
headers = {
    'SEC': KEY
}

json_data = requests.get(BASE_URL, headers=headers, verify=False).json()

print(json.dumps(json_data, indent=2))

for key in json_data['data']:
    print(f"Key is {key} and value is {json_data['data'][key]['value']}")
