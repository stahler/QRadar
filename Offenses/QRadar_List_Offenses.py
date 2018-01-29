""" QRadar List Offenses example """
import requests

BASE_URL = 'https://192.168.161.129/api/siem/offenses'

# We need to pass our Authentication token to the post method.
# Find it at: Console -> Admin -> Authorized Services '''
headers = {
    'SEC': '4ad878e9-5aae-4889-92fb-5dcc16ce60c0'
}

url = BASE_URL
json_data = requests.get(url, headers=headers, verify=False).json()

for offense in json_data:
    print(f"Status is {offense['status']} for offense {offense['description']}")
