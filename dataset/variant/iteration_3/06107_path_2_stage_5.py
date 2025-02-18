import matplotlib.pyplot as plt
import numpy as np

# Data remains same, but I'll shuffle the order manually
years = np.array([2015, 2010, 2017, 2014, 2019, 2013, 2016, 2012, 2018, 2011])
stock_prices = np.array([35, 20, 40, 25, 50, 28, 38, 22, 45, 30])
price_changes = np.diff(stock_prices) / stock_prices[:-1] * 100
sorted_indices = np.argsort(price_changes)[::-1]
sorted_price_changes = price_changes[sorted_indices]
sorted_years = years[1:][sorted_indices]

fig, (ax2, ax1) = plt.subplots(1, 2, figsize=(14, 7))

ax2.bar(sorted_years, sorted_price_changes, color='midnightblue', width=0.6)
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.set_xticks(sorted_years)
ax2.set_xticklabels(sorted_years, rotation=45)

ax1.plot(years, stock_prices, marker='o', linestyle='-', color='midnightblue', linewidth=2)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

plt.tight_layout()
plt.show()