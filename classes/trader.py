import numpy as np
import bisect


class TraderModel:
    def __init__(self):
        self.kt = 0 # knowledge of news
        self.st = np.random.uniform(0,1) # sensitivity to news 
        self.pvos = np.random.normal(100,4) # perceived value of stock
        self.lop = 0.2 #p0, limit order probability

    def update_percieved_valued(self, news_magnitude):
        self.pvos -= self.st * self.kt * news_magnitude

    def decide_order(self):
        # Random bernoulli trial with self.lop probability
        decision = np.random.uniform(0, 1)
        return decision < self.lop  # True or False

    def place_limit_order(self, current_stock_price):
        # This method determines the price of the limit order
        if self.decide_order():
            order_price = np.random.normal(self.pvos, 2)
            if order_price < self.pvos:
                return ('buy', order_price)
            else:
                return ('sell', order_price)
        else:
            return ('pass', None)  # Return a 'pass' action when not placing an order


# Example usage
#market = MarketModel()
#market.collect_and_execute_orders()
#print(f"Current Stock Price: {market.stock_price}")
