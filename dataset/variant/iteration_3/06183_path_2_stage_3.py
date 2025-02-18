import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
apple_stock_prices = [150, 50, 250, 200, 30, 250, 450, 120, 90, 400, 350]
google_stock_prices = [450, 500, 250, 700, 1000, 900, 350, 600, 300, 800, 400]
amazon_stock_prices = [1100, 1500, 250, 600, 200, 2000, 900, 1000, 400, 800, 700]

fig, ax = plt.subplots(figsize=(14, 8))

# Plots with the altered data
ax.plot(years, apple_stock_prices, marker='o', linestyle='-', linewidth=2, markersize=7, label='Banana', color='#4CAF50')
ax.plot(years, google_stock_prices, marker='s', linestyle='-', linewidth=2, markersize=7, label='Pear', color='#FF5733')
ax.plot(years, amazon_stock_prices, marker='d', linestyle='-', linewidth=2, markersize=7, label='Grapes', color='#33A1FF')

# Labels and title
ax.set_title('Fruit Market Dynamics (2010-2020)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Epoch', fontsize=14, labelpad=10)
ax.set_ylabel('Price in Gold', fontsize=14, labelpad=10)

# X-ticks and Y-ticks
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')
ax.set_yticks(np.arange(0, 2100, 200))
ax.set_ylim(0, 2100)
ax.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)

# Annotations for maximum values within each data group
max_price_idx = np.argmax(apple_stock_prices)
ax.annotate(f'{apple_stock_prices[max_price_idx]} Gold Coins', xy=(years[max_price_idx], apple_stock_prices[max_price_idx]), 
            xytext=(years[max_price_idx], apple_stock_prices[max_price_idx] + 100),
            arrowprops=dict(facecolor='black', shrink=0.05))

max_price_idx = np.argmax(google_stock_prices)
ax.annotate(f'{google_stock_prices[max_price_idx]} Gold Coins', xy=(years[max_price_idx], google_stock_prices[max_price_idx]), 
            xytext=(years[max_price_idx], google_stock_prices[max_price_idx] + 100),
            arrowprops=dict(facecolor='black', shrink=0.05))

max_price_idx = np.argmax(amazon_stock_prices)
ax.annotate(f'{amazon_stock_prices[max_price_idx]} Gold Coins', xy=(years[max_price_idx], amazon_stock_prices[max_price_idx]), 
            xytext=(years[max_price_idx], amazon_stock_prices[max_price_idx] + 100),
            arrowprops=dict(facecolor='black', shrink=0.05))

ax.legend(loc='upper left', fontsize=12)

plt.tight_layout()
plt.show()