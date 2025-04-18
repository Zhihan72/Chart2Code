import matplotlib.pyplot as plt
import numpy as np

# Data for stock prices (in USD) over the years 2010 to 2020
years = np.arange(2010, 2021)
apple_prices = [30, 50, 90, 120, 150, 200, 250, 300, 350, 400, 450]
google_prices = [250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000]
amazon_prices = [200, 250, 400, 600, 700, 800, 900, 1000, 1100, 1500, 2000]

# Initialize the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot stock prices
ax.plot(years, apple_prices, marker='o', linestyle='-', linewidth=2, markersize=7, label='AAPL', color='#FF5733')
ax.plot(years, google_prices, marker='s', linestyle='-', linewidth=2, markersize=7, label='GOOGL', color='#33A1FF')
ax.plot(years, amazon_prices, marker='d', linestyle='-', linewidth=2, markersize=7, label='AMZN', color='#4CAF50')

# Titles and labels
ax.set_title('Tech Stocks 2010-2020', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14, labelpad=10)
ax.set_ylabel('Price (USD)', fontsize=14, labelpad=10)

# Customize x-axis and y-axis
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')
ax.set_yticks(np.arange(0, 2100, 200))
ax.set_ylim(0, 2100)
ax.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)

# Annotate highest price for each company
max_price_idx = np.argmax(apple_prices)
ax.annotate(f'{apple_prices[max_price_idx]}', xy=(years[max_price_idx], apple_prices[max_price_idx]), 
            xytext=(years[max_price_idx], apple_prices[max_price_idx] + 100),
            arrowprops=dict(facecolor='black', shrink=0.05))

max_price_idx = np.argmax(google_prices)
ax.annotate(f'{google_prices[max_price_idx]}', xy=(years[max_price_idx], google_prices[max_price_idx]), 
            xytext=(years[max_price_idx], google_prices[max_price_idx] + 100),
            arrowprops=dict(facecolor='black', shrink=0.05))

max_price_idx = np.argmax(amazon_prices)
ax.annotate(f'{amazon_prices[max_price_idx]}', xy=(years[max_price_idx], amazon_prices[max_price_idx]), 
            xytext=(years[max_price_idx], amazon_prices[max_price_idx] + 100),
            arrowprops=dict(facecolor='black', shrink=0.05))

# Legend
ax.legend(loc='upper left', fontsize=12)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()