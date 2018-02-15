""" QRadar AQL example """
import configparser
import time
import json
import urllib3
import requests

config = configparser.ConfigParser()
config.read("../../config.ini")
IP = config.get("SIEM", "IP")
KEY = config.get("SIEM", "Key")

BASE_URL = "https://" + IP + "/api/ariel/searches"

# We need to pass our Authentication token to the post method.
# Find it at: Console -> Admin -> Authorized Services
headers = {
    'SEC': KEY
}

# format the url so we can pass the SQL statement
SQL = "Select username, count(*) as UserNameCount FROM events GROUP BY username"
url = BASE_URL +"?query_expression=" + SQL

# ignore InsecureRequestWarning (Test system)
urllib3.disable_warnings()

# This is a two step process:
# - We pass the SQL statement to the API
# - Retrieve the search_id from the initial rest call
# - We then pass the search_id back to the API to get our results
json_data = requests.post(url, headers=headers, verify=False).json()
search_id = json_data['search_id']

# might not need this timeout between calls, will research more
time.sleep(4)

# format the url so we can pass the search_id to get our results
url = BASE_URL + "/" + search_id + "/" + "results"
json_data = requests.get(url, headers=headers, verify=False).json()

# print the resulting json formated data
print(json.dumps(json_data, indent=2))
