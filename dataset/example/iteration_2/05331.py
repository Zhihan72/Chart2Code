import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tracking the progress of a hypothetical company's stock prices and volume traded over the past decade.

# Years for x-axis
years = np.arange(2013, 2023, 1)

# Stock prices (fictional data)
opening_price = np.array([20, 22, 26, 30, 25, 28, 35, 40, 45, 50])
closing_price = np.array([22, 26, 28, 25, 28, 35, 40, 45, 50, 55])
highest_price = np.array([24, 28, 32, 30, 30, 37, 43, 48, 55, 60])
lowest_price = np.array([18, 20, 23, 20, 24, 27, 32, 39, 42, 47])

# Volume traded (in millions)
volume_traded = np.array([5, 7, 9, 6, 5, 8, 10, 12, 15, 18])

# Create 2x1 subplot layout
fig, axes = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

# First subplot: Line plots for stock prices
axes[0].plot(years, opening_price, marker='o', color='blue', label='Opening Price', linewidth=2)
axes[0].plot(years, closing_price, marker='o', color='green', label='Closing Price', linewidth=2)
axes[0].plot(years, highest_price, marker='o', color='red', label='Highest Price', linewidth=2)
axes[0].plot(years, lowest_price, marker='o', color='orange', label='Lowest Price', linewidth=2)

axes[0].set_title('Stock Prices of XYZ Ltd. (2013-2022)', fontsize=16, fontweight='bold')
axes[0].set_ylabel('Price (USD)', fontsize=14)
axes[0].legend(title='Price Type', fontsize=12)
axes[0].grid(True, linestyle='--', alpha=0.7)

# Second subplot: Line plot for volume traded
axes[1].bar(years, volume_traded, color='purple', alpha=0.7)
axes[1].set_title('Volume Traded of XYZ Ltd. (2013-2022)', fontsize=16, fontweight='bold')
axes[1].set_xlabel('Year', fontsize=14)
axes[1].set_ylabel('Volume Traded (Million Shares)', fontsize=14)
axes[1].grid(True, linestyle='--', alpha=0.7)

# Annotate significant years in volume traded plot
significant_years = [2016, 2022]
events = ['Market Correction', 'Record High Volume']
volume_spots = volume_traded[np.isin(years, significant_years)]

for (year, event, volume) in zip(significant_years, events, volume_spots):
    axes[1].annotate(f'{event}\n{volume}M', xy=(year, volume), xytext=(year, volume + 2),
                     arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, ha='center', bbox=dict(boxstyle="round,pad=0.3", edgecolor='none', facecolor='lightgrey', alpha=0.5))

# Rotate x-axis labels for better readability
plt.xticks(years, rotation=45)

# Adjust layout to prevent overlap
plt.tight_layout(pad=4)

# Show the plot
plt.show()