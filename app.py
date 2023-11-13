
from flask import Flask, render_template, jsonify
from trader import *  # Assuming this is your module name

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # HTML file to be created

@app.route('/simulate')
def simulate():
    market = MarketModel()
    market.collect_and_execute_orders()
    data = market.get_time_series()  # This will now work as expected
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
