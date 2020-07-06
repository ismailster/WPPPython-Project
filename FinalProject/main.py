from flask import Flask, jsonify, request, Response, render_template
import yfinance as yt
import pandas as pd
import requests as rq
import time
from time import gmtime, strftime
from datetime import datetime, timedelta
from json2html import *

# "https://api.covid19api.com/country/south-africa/status/confirmed?from=2020-03-01T00:00:00Z&to=2020-04-01T00:00:00Z"
fb_main_title = "Python Final Project Submission"
fb_base_pg_title01 = "Welcome to the final project submission page for the WPP Python Course"
fb_base_pg_title02 = "Brought to you by Imran Ismail"
fb_intro_one = "This server uses a publiclly available Covid-19 API at https://api.covid19api.com"
fb_paragraph_1 = "for a "

main_title = "Python Final Project Submission"
base_pg_title01 = "Welcome to the final project submission page for the WPP Python Course"
base_pg_title02 = ""
intro_one = "This server uses a publiclly available Covid-19 API at https://api.covid19api.com"
paragraph_1 = "for a "

API_URL = "https://api.covid19api.com"
# Today_date = strftime("%Y%m%dT00:00:00Z", gmtime())
# lookback_days = gmtime()-30

end = gmtime()
end = strftime("%m/%d/%Y", end)
end = datetime.strptime(end, "%m/%d/%Y") #string to date
start = end - timedelta(days=10) # date - days

def Covid_API(state, date="2"):
	output = rq.get(API_URL)
	return output

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("firstbase.html", main_title=fb_main_title, title1=fb_base_pg_title01, title2=fb_base_pg_title02, intro_one=fb_intro_one)


@app.route("/summary/")
def summary():
	template = request.args.get('template')
	summary_back = rq.get(f"{API_URL}/summary")
	if template == "html":
		output = json2html.convert(json = summary_back.text)
		output_type = "html"
	else:
		output =  summary_back.json()
		output_type = "json (this is the default setting)"

	return render_template("home.html", 
		name="Imran", feeling="Great", data=output, 
		main_title=main_title, title1=base_pg_title01, title2=base_pg_title02, intro_one=intro_one, 
		output_type=output_type)

# @app.route("/summary.json")
# def summary_json():
# 	summary_back = rq.get(f"{API_URL}/summary")
# 	# output = json2html.convert(json = summary_back.text)
# 	output = summary_back.json()
# 	return render_template("home.html", 
# 		name="Imran", feeling="Great", data=output, 
# 		main_title=main_title, title1=base_pg_title01, title2=base_pg_title02, intro_one=intro_one
# 		)


@app.route("/allcountries")
def countries():
	country_list_back = rq.get(f"{API_URL}/countries")
	return Response(country_list_back.text)

# @app.route("/country/<country_name>")
# def one_country(country_name):
# 	country_list_back = rq.get(f"{API_URL}/country/{country_name}/status/confirmed?from=2020-06-30T00:00:00Z&to=2020-07-01T00:00:00Z")
# 	# user = request.args.get('user')
# 	# state = request.args.get('state')
# 	country_name =  country_name.replace("-", " ")
# 	country_name = country_name.title()
# 	state = "Yo yo"
# 	input = country_list_back.text
# 	new_input = json2html.convert(json = input)
# 	return render_template("home.html", name=country_name, feeling=state)
# 	# return new_input



if __name__ == "__main__":
	app.run(debug=True)
	