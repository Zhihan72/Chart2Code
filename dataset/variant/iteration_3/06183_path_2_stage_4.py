import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
apple_stock_prices = [150, 50, 250, 200, 30, 250, 450, 120, 90, 400, 350]
google_stock_prices = [450, 500, 250, 700, 1000, 900, 350, 600, 300, 800, 400]
amazon_stock_prices = [1100, 1500, 250, 600, 200, 2000, 900, 1000, 400, 800, 700]

fig, ax = plt.subplots(figsize=(14, 8))

# Plots with altered styles
ax.plot(years, apple_stock_prices, marker='x', linestyle='--', linewidth=2.5, markersize=9, label='Banana', color='#FFC300')
ax.plot(years, google_stock_prices, marker='^', linestyle='-.', linewidth=2.5, markersize=9, label='Pear', color='#DAF7A6')
ax.plot(years, amazon_stock_prices, marker='v', linestyle=':', linewidth=2.5, markersize=9, label='Grapes', color='#FF33FF')

# Labels and title
ax.set_title('Market Trends (2010-2020)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14, labelpad=10)
ax.set_ylabel('Value', fontsize=14, labelpad=10)

# X-ticks and Y-ticks
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticks(np.arange(0, 2200, 200))
ax.set_ylim(0, 2200)
ax.grid(True, which='major', linestyle='-', linewidth=0.5, alpha=0.5)

# Annotations for maximum values
max_price_idx = np.argmax(apple_stock_prices)
ax.annotate(f'{apple_stock_prices[max_price_idx]} G', xy=(years[max_price_idx], apple_stock_prices[max_price_idx]), 
            xytext=(years[max_price_idx], apple_stock_prices[max_price_idx] + 50),
            arrowprops=dict(facecolor='gray', shrink=0.05))

max_price_idx = np.argmax(google_stock_prices)
ax.annotate(f'{google_stock_prices[max_price_idx]} G', xy=(years[max_price_idx], google_stock_prices[max_price_idx]), 
            xytext=(years[max_price_idx], google_stock_prices[max_price_idx] + 50),
            arrowprops=dict(facecolor='gray', shrink=0.05))

max_price_idx = np.argmax(amazon_stock_prices)
ax.annotate(f'{amazon_stock_prices[max_price_idx]} G', xy=(years[max_price_idx], amazon_stock_prices[max_price_idx]), 
            xytext=(years[max_price_idx], amazon_stock_prices[max_price_idx] + 50),
            arrowprops=dict(facecolor='gray', shrink=0.05))

ax.legend(loc='upper right', fontsize=12, frameon=False)

plt.tight_layout()
plt.show()