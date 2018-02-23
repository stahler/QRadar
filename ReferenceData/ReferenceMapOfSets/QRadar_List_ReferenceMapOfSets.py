""" QRadar Reference Map of Sets: list example """
import configparser
import json
import requests

config = configparser.ConfigParser()
config.read("../../config.ini")
IP = config.get("SIEM", "IP")
KEY = config.get("SIEM", "Key")

BASE_URL = "https://" + IP + "/api/reference_data/map_of_sets"

# We need to pass our Authentication token to the post method.
# Find it at: Console -> Admin -> Authorized Services '''
headers = {
    'SEC': KEY
}

json_data = requests.get(BASE_URL, headers=headers, verify=False).json()

print(json.dumps(json_data, indent=2))
