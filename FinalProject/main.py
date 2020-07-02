from flask import Flask, jsonify, request, Response, render_template
import yfinance as yt
import pandas as pd
import requests as rq
import time
from time import gmtime, strftime
from datetime import datetime, timedelta
from json2html import *

# "https://api.covid19api.com/country/south-africa/status/confirmed?from=2020-03-01T00:00:00Z&to=2020-04-01T00:00:00Z"

API_URL = "https://api.covid19api.com"
# Today_date = strftime("%Y%m%dT00:00:00Z", gmtime())
# lookback_days = gmtime()-30

end = gmtime()
end = strftime("%m/%d/%Y", end)
end = datetime.strptime(end, "%m/%d/%Y") #string to date
start = end - timedelta(days=10) # date - days

def Covid_API(state, date="2"):
	output = rq.get(API_URL)
	return output.text

app = Flask(__name__)

@app.route("/")
def home():
	back = rq.get(API_URL)
	return back.text


@app.route("/summary/")
def summary():
	summary_back = rq.get(f"{API_URL}/summary")
	return summary_back.text

@app.route("/allcountries")
def countries():
	country_list_back = rq.get(f"{API_URL}/countries")
	return Response(country_list_back.text)

@app.route("/country/<country_name>")
def one_country(country_name):
	country_list_back = rq.get(f"{API_URL}/country/{country_name}/status/confirmed?from=2020-06-30T00:00:00Z&to=2020-07-01T00:00:00Z")
	input = country_list_back.text
	new_input = json2html.convert(json = input)
	return new_input



if __name__ == "__main__":
	app.run(debug=True)
	