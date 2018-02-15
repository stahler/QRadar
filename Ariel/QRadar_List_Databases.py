""" QRadar List Offenses example """
import configparser
import json
import urllib3
import requests

config = configparser.ConfigParser()
config.read("../../config.ini")
IP = config.get("SIEM", "IP")
KEY = config.get("SIEM", "Key")

BASE_URL = "https://" + IP + "/api/ariel/databases"

# We need to pass our Authentication token to the post method.
# Find it at: Console -> Admin -> Authorized Services '''
headers = {
    'SEC': KEY
}

urllib3.disable_warnings()

url = BASE_URL
json_data = requests.get(url, headers=headers, verify=False).json()

print(json.dumps(json_data, indent=2))
