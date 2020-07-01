from flask import Flask, jsonify, request, Response, render_template
import yfinance as yt
import pandas as pd
import requests as rq

API_URL = "https://api.covid19api.com/"

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
	back = rq.get(f"{API_URL}/summary")
	return back.text



if __name__ == "__main__":
	app.run(debug=True)
	