# News-Stock-Simulation

An agent-based simulation of how news propagation among traders affects stock prices. The model places 1,000 traders on a circular network; on day 50 a news event begins spreading outward through neighbors, and each trader adjusts their perceived stock value based on their sensitivity and the news magnitude. Traders submit stochastic limit orders matched via an order book, producing realistic price dynamics with mean-reversion (Ornstein-Uhlenbeck-inspired) tendencies.

A Flask web app with Chart.js lets you run simulations in the browser and overlay multiple runs to compare outcomes.

## Key Technologies

- **Python** (NumPy, Matplotlib)
- **Flask** + **Chart.js** for interactive visualization
- Agent-based modeling with order-book price discovery and network-based news diffusion
