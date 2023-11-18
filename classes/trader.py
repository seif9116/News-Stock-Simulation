import numpy as np
MULTIPLIER = 13

class TraderModel:
    def __init__(self, index):
        self.index = index
        self.kt = 0 # knowledge of news
        self.st = np.random.beta(a=2, b=1) # sensitivity to news
        self.pvos = np.random.normal(100, 15) # perceived value of stock
        self.lop = 0.8 # p0, limit order probability

    def update_perceived_value(self, current_price, news_magnitude=0):
        self.pvos += self.st * self.kt * news_magnitude * MULTIPLIER
        # inspired from Ohrnstein Uhnbleck Process, include mean reversion 
        # tendencies for pvos 
        self.pvos += np.random.normal((current_price - self.pvos)*0.09, 10)

    def decide_order(self):
        # Random Bernoulli trial with self.lop probability
        return np.random.rand() < self.lop

    def place_limit_order(self, current_price):
        # This method determines the price of the limit order
        if self.decide_order():
            self.update_perceived_value(current_price=current_price)
            order_price = np.random.normal(self.pvos, 10)
            order_type = 'sell' if order_price > self.pvos else 'buy'
            return order_type, order_price
        else:
            return 'pass', None  # Return a 'pass' action when not placing an order
    def receive_news(self, news_magnitude, current_price):
        if news_magnitude != 0:
            self.kt = 1
            self.update_perceived_value(news_magnitude=news_magnitude, current_price=current_price)
        else:
            self.kt = 0
