import numpy as np

class NewsSpreadModel:
    def __init__(self, num_traders=1000, radius=5, arrival_rate=1):
        # Initialize the model with the number of traders, radius of influence, and news arrival rate.
        self.num_traders = num_traders  # Total number of traders in the model
        self.radius = radius  # The radius of influence for a trader
        self.arrival_rate = arrival_rate  # The probability of news spreading to a neighbor
        self.news_states = np.zeros(num_traders, dtype=int) # Initialize all traders with no knowledge of the news

    def start_news_at_random_location(self):
        """Start the news from a single random location among the traders."""
        #random_index = np.random.randint(self.num_traders)  # Choose a random trader to start the news
        #self.news_states[random_index] = 1  # Update the news state of the chosen trader
        self.news_states = np.random.binomial(1, 0.1, self.num_traders)
    def _get_neighbors(self, index):
        """Get neighboring indices for a trader considering a circular topology."""
        # Calculate indices of neighboring traders within the radius
        return [(index + i) % self.num_traders for i in range(-self.radius, self.radius + 1) if i != 0]

    def spread_news(self):
        """Simulate one step of news spread among the traders."""
        # Iterate over all traders
        for i in range(self.num_traders):
            # Check if the trader is aware of the news
            if self.news_states[i] == 1:
                neighbors = self._get_neighbors(i)  # Get the neighbors of the trader
                # Spread the news to each neighbor based on the arrival rate
                for neighbor in neighbors:
                    if np.random.uniform() < self.arrival_rate:
                        self.news_states[neighbor] = 1  # Update the neighbor's state to aware of the news
