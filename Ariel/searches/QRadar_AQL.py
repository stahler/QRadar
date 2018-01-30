""" QRadar List Offenses example """
import configparser
import time
import json
import requests

config = configparser.ConfigParser()
config.read("../../config.ini")
IP = config.get("SIEM", "IP")
KEY = config.get("SIEM", "Key")

BASE_URL = "https://" + IP + "/api/ariel/searches"

# We need to pass our Authentication token to the post method.
# Find it at: Console -> Admin -> Authorized Services '''
headers = {
    'SEC': KEY
}

# format the url so we can pass the SQL statement
SQL = "Select username, count(*) as UserNameCount FROM events GROUP BY username"
url = BASE_URL +"?query_expression=" + SQL

# retrieve the search_id so we can use it to get the results
json_data = requests.post(url, headers=headers, verify=False).json()
search_id = json_data['search_id']

# might not need this timeout, will research more
time.sleep(4)

# format the url so we can pass the search_id to get our results
url = BASE_URL + "/" + search_id + "/" + "results"
json_data = requests.get(url, headers=headers, verify=False).json()

# print the resulting json formated data
print(json.dumps(json_data, indent=2))
