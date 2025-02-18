import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)
# Manually altered stock prices while preserving the original structure
stock_prices = np.array([21, 27, 24, 22, 34, 32, 38, 36, 43, 48])
price_changes = np.diff(stock_prices) / stock_prices[:-1] * 100

sorted_indices = np.argsort(price_changes)
sorted_years = years[1:][sorted_indices]
sorted_price_changes = price_changes[sorted_indices]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

ax1.plot(years, stock_prices, marker='o', linestyle='-', color='royalblue', linewidth=2)
ax1.set_xticks(years)
ax1.set_xticklabels([])

ax2.bar(sorted_years, sorted_price_changes, color='royalblue', width=0.6)
ax2.set_xticks(sorted_years)
ax2.set_xticklabels([])

plt.tight_layout()
plt.show()