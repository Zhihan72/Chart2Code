import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)
stock_prices = np.array([20, 22, 28, 25, 30, 35, 40, 38, 45, 50])
price_changes = np.diff(stock_prices) / stock_prices[:-1] * 100

sorted_indices = np.argsort(price_changes)
sorted_years = years[1:][sorted_indices]
sorted_price_changes = price_changes[sorted_indices]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Changed the color of the line in ax1 to use the same color 'royalblue'
ax1.plot(years, stock_prices, marker='o', linestyle='-', color='royalblue', linewidth=2)
ax1.set_xticks(years)
ax1.set_xticklabels([])

# The bar chart already uses 'royalblue', no change needed for ax2
ax2.bar(sorted_years, sorted_price_changes, color='royalblue', width=0.6)
ax2.set_xticks(sorted_years)
ax2.set_xticklabels([])

plt.tight_layout()
plt.show()