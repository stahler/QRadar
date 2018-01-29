""" QRadar Reference Map: Bulk load example """

import json
import requests

BASE_URL = 'https://192.168.161.129/api/reference_data/maps/bulk_load/DEMO_MAP?'

# We need to pass our Authentication token to the post method.
# Find it at: Console -> Admin -> Authorized Services '''
headers = {
    'SEC': '4ad878e9-5aae-4889-92fb-5dcc16ce60c0'
}

# Create a dict for the elements we are passing.
# In the "create" case, we are passing the name of the reference set
# and the type (IP)
payload = {
    'stah06':'Wes Stahler',
    'home01':'Homer Simpson',
    'blan01':'Gern Blanston',
}

url = BASE_URL
json_data = requests.post(url, data=json.dumps(payload), headers=headers, verify=False).json()
print(json.dumps(json_data, indent=2))
