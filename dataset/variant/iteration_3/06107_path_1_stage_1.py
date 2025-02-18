import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)
stock_prices = np.array([20, 22, 28, 25, 30, 35, 40, 38, 45, 50])
price_changes = np.diff(stock_prices) / stock_prices[:-1] * 100

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Plotting the line chart without textual elements
ax1.plot(years, stock_prices, marker='o', linestyle='-', color='blue', linewidth=2)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.set_xticks(years)
ax1.set_xticklabels([])

# Plotting the bar chart without textual elements
ax2.bar(years[1:], price_changes, color='royalblue', width=0.6)
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.set_xticks(years[1:])
ax2.set_xticklabels([])

plt.tight_layout()
plt.show()