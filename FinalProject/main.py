from flask import Flask, jsonify, request, Response, render_template
import yfinance as yt

app = Flask(__name__)

@app.route("/")
def home():
	return "hello HELLO!"

if __name__ == "__main__":
	app.run(debug=True)
	