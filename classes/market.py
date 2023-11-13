import bisect
from trader import TraderModel
class MarketModel:
    def __init__(self, num_traders=1000):
        self.traders = [TraderModel() for _ in range(num_traders)]
        self.stock_price = 100
        self.buy_orders = []
        self.sell_orders = []
        self.stock_price_history = []  # List to record stock price changes

    def update_stock_price(self):
        if self.buy_orders and self.sell_orders:
            highest_buy = self.buy_orders[-1]  
            lowest_sell = self.sell_orders[0]
            self.stock_price = (highest_buy + lowest_sell) / 2
            self.stock_price_history.append(self.stock_price)  # Record the new stock price
    def execute_orders(self):
        while self.buy_orders and self.sell_orders and self.buy_orders[-1] >= self.sell_orders[0]:
            # Update stock price before executing each order
            self.update_stock_price()
            executed_price = self.stock_price
            self.buy_orders.pop()  # Remove the highest buy order
            self.sell_orders.pop(0)  # Remove the lowest sell order
            print(f"Executed order at stock price: {executed_price}")

    def collect_and_execute_orders(self):
        # Update stock price based on current orders before collecting new orders
        self.update_stock_price()

        # Collect orders from traders
        for trader in self.traders:
            order_type, order_price = trader.place_limit_order(self.stock_price)
            if order_type == 'buy':
                bisect.insort(self.buy_orders, order_price)
            elif order_type == 'sell':
                bisect.insort(self.sell_orders, order_price)
            # If the trader passes, do not add an order to buy or sell lists

        # Execute overlapping orders and update stock price again
        self.execute_orders()
        self.update_stock_price()

    def get_time_series(self):
        # Returns the recorded stock prices as a time series
        return [{'x': index, 'y': price} for index, price in enumerate(self.stock_price_history)]
