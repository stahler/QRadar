""" QRadar Reference Sets: list example """
import configparser
import requests

config = configparser.ConfigParser()
config.read("../../config.ini")
IP = config.get("SIEM", "IP")
KEY = config.get("SIEM", "Key")

BASE_URL = "https://" + IP + "/api/reference_data/sets/DEMO_IP"

# We need to pass our Authentication token to the post method.
# Find it at: Console -> Admin -> Authorized Services '''
headers = {
    'SEC': KEY
}

json_data = requests.get(BASE_URL, headers=headers, verify=False).json()

for ip in json_data['data']:
    print(ip['value'])
