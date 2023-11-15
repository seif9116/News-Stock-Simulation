
from flask import Flask, render_template, jsonify
from classes.trader import *  # Assuming this is your module name
from classes.market import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # HTML file to be created

@app.route('/simulate')
def simulate():
    market = MarketModel()
    market.simulate_market()
    data = market.get_time_series()  # This should return the time series data

    # Format data for Chart.js (assuming data is a list of stock prices)
    formatted_data = [{"x": day, "y": price} for day, price in enumerate(data, start=1)]

    return jsonify({"stockPrices": formatted_data})
if __name__ == '__main__':
    app.run(debug=True)
