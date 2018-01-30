""" QRadar Reference Sets: Bulk load example """
import configparser
import json
import requests

config = configparser.ConfigParser()
config.read("../../config.ini")
IP = config.get("SIEM", "IP")
KEY = config.get("SIEM", "Key")

BASE_URL = "https://" + IP + "/api/reference_data/sets/bulk_load/DEMO_IP?"

# We need to pass our Authentication token to the post method.
# Find it at: Console -> Admin -> Authorized Services '''
headers = {
    'SEC': KEY
}

# Create a dict for the elements we are passing.
# In the "create" case, we are passing the name of the reference set
# and the type (IP)
payload = [
    "10.10.10.11",
    "5.5.5.5"
]

url = BASE_URL
json_data = requests.post(url, data=json.dumps(payload), headers=headers, verify=False).json()
print(json.dumps(json_data, indent=2))
