from flask import Flask, jsonify, request, Response, render_template
import pandas as pd
import requests as rq
from json2html import *
import json

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
	elif template == "json":
		output =  summary_back.json()
		output_type = "json (this is the default setting)"
	elif template == "text":
		output =  summary_back.text
		output_type = "text (tis may look like json but it's text)"
	else:
		output = "ruh roh!"
		output_type = "I think you made a mistake"

	return render_template("home.html", 
		name="Imran", feeling="Great", data=output, 
		main_title=main_title, title1=base_pg_title01, title2=base_pg_title02, intro_one=intro_one, 
		output_type=output_type)



if __name__ == "__main__":
	app.run(debug=True)
	