import numpy as np
MULTIPLIER = 3

class TraderModel:
    def __init__(self, index):
        self.index = index
        self.kt = 0 # knowledge of news
        self.st = np.random.beta(a=2, b=1) # sensitivity to news
        self.pvos = np.random.normal(100, 10) # perceived value of stock
        self.lop = 0.8 # p0, limit order probability

    def update_perceived_value(self, news_magnitude=0):
        self.pvos += self.st * self.kt * news_magnitude * MULTIPLIER
        self.pvos += np.random.normal(0, 5)

    def decide_order(self):
        # Random Bernoulli trial with self.lop probability
        return np.random.rand() < self.lop

    def place_limit_order(self):
        # This method determines the price of the limit order
        if self.decide_order():
            self.update_perceived_value()
            order_price = np.random.normal(self.pvos, 10)
            order_type = 'sell' if order_price > self.pvos else 'buy'
            return order_type, order_price
        else:
            return 'pass', None  # Return a 'pass' action when not placing an order
    def receive_news(self, news_magnitude):
        if news_magnitude != 0:
            self.kt = 1
            self.update_perceived_value(news_magnitude)
        else:
            self.kt = 0
