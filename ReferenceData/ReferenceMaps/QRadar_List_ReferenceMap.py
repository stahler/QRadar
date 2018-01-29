""" QRadar Reference Map: list example """
import json
import requests

BASE_URL = 'https://192.168.161.129/api/reference_data/maps/DEMO_MAP'

# We need to pass our Authentication token to the post method.
# Find it at: Console -> Admin -> Authorized Services '''
headers = {
    'SEC': '4ad878e9-5aae-4889-92fb-5dcc16ce60c0'
}

url = BASE_URL
json_data = requests.get(url, headers=headers, verify=False).json()

print(json.dumps(json_data, indent=2))

for key in json_data['data']:
    print(f"Key is {key} and value is {json_data['data'][key]['value']}")
