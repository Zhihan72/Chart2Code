import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Sales data (in thousands of units)
apple_sales = [15, 18, 20, 24, 27, 30, 34, 38, 42, 45, 50]
orange_sales = [10, 12, 14, 15, 17, 20, 22, 25, 27, 29, 32]
banana_sales = [8, 9, 10, 11, 14, 17, 21, 24, 27, 30, 34]

# Create figure and axis
fig, ax = plt.subplots(figsize=(14, 7))

# Plot sales data with shuffled colors
ax.plot(years, apple_sales, marker='o', linestyle='-', color='yellow', linewidth=2, markersize=6, label='Apples')
ax.plot(years, orange_sales, marker='s', linestyle='--', color='r', linewidth=2, markersize=6, label='Oranges')
ax.plot(years, banana_sales, marker='^', linestyle='-.', color='orange', linewidth=2, markersize=6, label='Bananas')

# Add annotations for key data points
for year, sales in zip(years, apple_sales):
    ax.annotate(f'{sales}K', xy=(year, sales), xytext=(0, 8), textcoords='offset points', fontsize=9, ha='center', color='darkgoldenrod')

for year, sales in zip(years, orange_sales):
    ax.annotate(f'{sales}K', xy=(year, sales), xytext=(0, 8), textcoords='offset points', fontsize=9, ha='center', color='darkred')

for year, sales in zip(years, banana_sales):
    ax.annotate(f'{sales}K', xy=(year, sales), xytext=(0, 8), textcoords='offset points', fontsize=9, ha='center', color='darkorange')

# Set the title and labels
ax.set_title('Decade of Fruit Sales Growth (2010-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Sales (Thousands of Units)', fontsize=14)

# Add grid lines for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Add a legend
ax.legend(loc='upper left', fontsize=12)

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the plot
plt.show()