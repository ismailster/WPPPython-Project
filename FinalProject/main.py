from flask import Flask, jsonify, request, Response, render_template
import yfinance as yt
import pandas as pd

def get_stock_data(company, period="2d"):
	company = yt.Ticker(company)
	ans = pd.DataFrame()
	ans = company.history(period=period)
	return ans.to_html()

app = Flask(__name__)

@app.route("/")
def home():
	return "hello HELLO!"

@app.route("/<name_company>")
def lookup_company(name_company):
	giveback = get_stock_data(name_company)
	return giveback




if __name__ == "__main__":
	app.run(debug=True)
	