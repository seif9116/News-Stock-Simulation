
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
    market.simulate_market()  # Run the market simulation for the defined number of time steps
    data = market.get_time_series()  # Get the time series data after the simulation
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
