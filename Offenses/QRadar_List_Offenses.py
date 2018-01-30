""" QRadar List Offenses example """
import configparser
import requests

config = configparser.ConfigParser()
config.read("../config.ini")
IP = config.get("SIEM", "IP")
KEY = config.get("SIEM", "Key")

BASE_URL = "https://" + IP + "/api/siem/offenses"

# We need to pass our Authentication token to the post method.
# Find it at: Console -> Admin -> Authorized Services '''
headers = {
    'SEC': KEY
}

url = BASE_URL
json_data = requests.get(url, headers=headers, verify=False).json()

for offense in json_data:
    print(f"Status is {offense['status']} for offense {offense['description']}")
