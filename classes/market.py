import numpy as np
import bisect
from classes.trader import TraderModel
from classes.news import NewsSpreadModel

#NEWS_MAGNITUDE = -1
class MarketModel:
    def __init__(self, num_traders=1000, time_steps=115):
        self.traders = [TraderModel(index=i) for i in range(num_traders)]
        self.stock_price = 100
        self.buy_orders = []
        self.sell_orders = []
        self.stock_price_history = []
        self.time_steps = time_steps
        self.news_model = NewsSpreadModel(num_traders=num_traders)

    def update_stock_price(self):
        if self.buy_orders and self.sell_orders:
            highest_buy = self.buy_orders[-1]
            lowest_sell = self.sell_orders[0]
            market_shock = np.random.normal(0,3) # include stochasticity into the price of market
            self.stock_price = (highest_buy + lowest_sell) / 2 + market_shock
        self.stock_price_history.append(self.stock_price)

    def execute_orders(self):
        while self.buy_orders and self.sell_orders and self.buy_orders[-1] >= self.sell_orders[0]:
            self.buy_orders.pop()
            self.sell_orders.pop(0)
#            self.update_stock_price()

    def get_current_price(self):
        if not self.stock_price_history:
            return 100
        else:
            return self.stock_price_history[-1]
    def simulate_market(self, news_magnitude=-1):
        for day in range(self.time_steps):
            if day == 50:
                # Start the news spread from a single random location on day 50
                self.news_model.start_news_at_random_location()
            if day >= 50:
                # From day 50 onwards, continue spreading the news
                self.news_model.spread_news()
               # news_magnitude = -1 
                for trader in self.traders:
                    trader.receive_news(
                            news_magnitude if self.news_model.news_states[trader.index]==1 else 0,
                            self.get_current_price())
            self.collect_and_execute_orders()
            self.update_stock_price()  # Ensure stock price is updated every time step

    def collect_and_execute_orders(self):
        for trader in self.traders:
            order_type, order_price = trader.place_limit_order(self.get_current_price())
            if order_type == 'buy':
                bisect.insort(self.buy_orders, order_price)
            elif order_type == 'sell':
                bisect.insort(self.sell_orders, order_price)
        self.execute_orders()
        print(self.buy_orders[-5:], 
                      self.buy_orders[:5],
                      self.sell_orders[-5:],
                      self.sell_orders[:5])

    def get_time_series(self):
        return [{'x': index, 'y': price} for index, price in enumerate(self.stock_price_history)]
