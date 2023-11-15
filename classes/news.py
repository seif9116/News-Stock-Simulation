import numpy as np

class NewsSpreadModel:
    def __init__(self, num_traders=1000, radius=5, arrival_rate=1):
        self.num_traders = num_traders
        self.radius = radius
        self.arrival_rate = arrival_rate 
        self.news_states = np.zeros(num_traders, dtype=int) # All traders start with no knowledge

    def start_news_at_random_location(self):
        '''Start the news from a single random location'''
        random_index = np.random.randint(self.num_traders) 
        self.news_states[random_index] = 1

    def _get_neighbors(self, index):
        """Get neighboring indices for circular topology."""
        return [(index + i) % self.num_traders for i in range(-self.radius, self.radius + 1) if i != 0]

    def spread_news(self):
        """Simulate one step of news spread."""
        for i in range(self.num_traders):
            if self.news_states[i] == 1:
                neighbors = self._get_neighbors(i)
                for neighbor in neighbors:
                    if np.random.uniform() < self.arrival_rate:
                        self.news_states[neighbor] = 1

