import argparse
import sys

import requests


parser = argparse.ArgumentParser(description="Numbers!!!")
parser.add_argument('--num', type=int, help="number to find information about", default=5)

# pip3 install requests --user

API_URL = "https://api.covid19api.com/"

if __name__ == "__main__":
	args = parser.parse_args(sys.argv[1:])
	print(args)

	# url = f"http://numbersapi.com/{args.num}/math"
	url = API_URL
	r = requests.get(url)
	print(r.text)
