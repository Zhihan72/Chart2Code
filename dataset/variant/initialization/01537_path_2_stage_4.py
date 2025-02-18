import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2010, 2020)
strawberries_yield = np.array([1.0, 1.2, 1.5, 2.0, 2.2, 2.4, 2.8, 3.0, 3.5, 3.8])
tomatoes_yield = np.array([1.5, 1.7, 1.8, 2.1, 2.4, 2.6, 3.0, 3.2, 3.4, 3.9])

price_strawberries = 1000
price_tomatoes = 900

revenue_strawberries = strawberries_yield * price_strawberries
revenue_tomatoes = tomatoes_yield * price_tomatoes

total_revenue = revenue_strawberries + revenue_tomatoes

cumulative_tomatoes = strawberries_yield + tomatoes_yield

fig, ax1 = plt.subplots(figsize=(12, 7))

ax1.fill_between(years, strawberries_yield, color='#228B22', alpha=0.6)
ax1.fill_between(years, cumulative_tomatoes, strawberries_yield, color='#FF6347', alpha=0.6)

ax2 = ax1.twinx()
ax2.plot(years, total_revenue, color='blue', linewidth=2.5, linestyle='-', marker='o')

ax1.set_xticks(years)
ax1.set_yticks(np.arange(0, 12, 1))
ax2.set_yticks(np.arange(0, 25000, 5000))

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()