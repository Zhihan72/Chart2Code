import matplotlib.pyplot as plt
import numpy as np

# Define years for the data
years = np.arange(2010, 2020)

# Manually crafted stock prices for TechAdvance (in USD)
stock_prices = np.array([20, 22, 28, 25, 30, 35, 40, 38, 45, 50])

# Calculate yearly percentage changes in stock prices
price_changes = np.diff(stock_prices) / stock_prices[:-1] * 100

# Sort percentage changes in descending order and accordingly sort the years
sorted_indices = np.argsort(price_changes)[::-1]
sorted_price_changes = price_changes[sorted_indices]
sorted_years = years[1:][sorted_indices]

# Initialize the figure and the subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Plot the line chart for stock prices
ax1.plot(years, stock_prices, marker='o', linestyle='-', color='blue', linewidth=2, label='Stock Price')
ax1.set_title('TechAdvance Stock Prices: 2010-2019', fontsize=14, fontweight='bold', pad=15)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Stock Price (USD)', fontsize=12)
ax1.legend(loc='upper left', fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.annotate('Initial surge after product launch', xy=(2013, 28), xytext=(2011, 35),
             arrowprops=dict(facecolor='green', arrowstyle='->', lw=1.5), fontsize=10, color='darkgreen')
ax1.annotate('Dip due to market correction', xy=(2013, 25), xytext=(2014, 20),
             arrowprops=dict(facecolor='red', arrowstyle='->', lw=1.5), fontsize=10, color='darkred')
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

# Plotting the sorted bar chart for percentage changes in stock prices
ax2.bar(sorted_years, sorted_price_changes, color='royalblue', width=0.6, label='Yearly % Change')
ax2.set_title('Year-over-Year % Change in Stock Prices (Sorted)', fontsize=14, fontweight='bold', pad=15)
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Percentage Change (%)', fontsize=12)
ax2.legend(loc='upper right', fontsize=10)
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.set_xticks(sorted_years)
ax2.set_xticklabels(sorted_years, rotation=45)

plt.tight_layout()
plt.show()