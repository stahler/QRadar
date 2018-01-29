""" QRadar Reference Map: Create example """

import urllib.parse
import json
import requests

BASE_URL = 'https://192.168.161.129/api/reference_data/maps?'

# We need to pass our Authentication token to the post method.
# Find it at: Console -> Admin -> Authorized Services '''
headers = {
    'SEC': '4ad878e9-5aae-4889-92fb-5dcc16ce60c0'
}

# Create a dict for the elements we are passing.
# In the "create" case, we are passing the name of the reference set
# and the type (IP)
parameters = {
    'element_type': 'ALNIC',
    'name': 'DEMO_MAP'
}

url = BASE_URL + urllib.parse.urlencode(parameters)
json_data = requests.post(url, headers=headers, verify=False).json()
print(json.dumps(json_data, indent=2))