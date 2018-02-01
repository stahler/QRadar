""" QRadar List Offenses example """
import configparser
import time
import json
import requests

config = configparser.ConfigParser()
config.read("../../config.ini")
IP = config.get("SIEM", "IP")
KEY = config.get("SIEM", "Key")
