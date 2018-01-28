""" QRadar Reference Sets: Create example """
import requests

BASE_URL = 'https://192.168.161.129/api/reference_data/sets/DEMO_IP'

# We need to pass our Authentication token to the post method.
# Find it at: Console -> Admin -> Authorized Services '''
headers = {
    'SEC': '4ad878e9-5aae-4889-92fb-5dcc16ce60c0'
}

url = BASE_URL  # + urllib.parse.urlencode(parameters)
json_data = requests.get(url, headers=headers, verify=False).json()

for ip in json_data['data']:
    print(ip['value'])
