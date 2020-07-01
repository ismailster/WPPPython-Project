import argparse
import sys
import requests
import json

API_URL = "https://api.covid19api.com/"
if __name__ == "__main__":
	url = API_URL
	r = requests.get(url)
	json_data = json.loads(r.text)
	print(type(json_data))