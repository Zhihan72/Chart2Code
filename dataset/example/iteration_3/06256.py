import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# Imagine we are analyzing the changing market share of different smartphone brands over the past decade.

# Time period: 2010 to 2020
years = np.arange(2010, 2021)

# Artificial data for market share percentage of various smartphone brands
apple = [15, 20, 20, 25, 25, 27, 32, 35, 34, 36, 38]
samsung = [25, 30, 32, 30, 28, 28, 27, 25, 26, 24, 22]
huawei = [10, 12, 15, 16, 18, 20, 22, 24, 22, 20, 19]
xiaomi = [5, 6, 8, 10, 12, 14, 15, 17, 18, 19, 20]
others = [45, 32, 25, 19, 17, 11,  8,  6,  6,  1, 1]

# Initialize the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Set the colors corresponding to each brand
colors = ['#FF5733', '#1E90FF', '#32CD32', '#FFD700', '#606060']

# Line plots for each brand's market share over the years
ax.plot(years, apple, label='Apple', color=colors[0], marker='o', linewidth=2)
ax.plot(years, samsung, label='Samsung', color=colors[1], marker='s', linewidth=2)
ax.plot(years, huawei, label='Huawei', color=colors[2], marker='D', linewidth=2)
ax.plot(years, xiaomi, label='Xiaomi', color=colors[3], marker='^', linewidth=2)
ax.plot(years, others, label='Others', color=colors[4], marker='v', linewidth=2)

# Title and labels
ax.set_title("The Dynamic Market Share of Smartphone Brands\n(2010-2020)", fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Market Share (%)', fontsize=12)

# Set the y-axis limit to better represent the data range
ax.set_ylim(0, 50)

# Adding a grid for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Adding the legend
ax.legend(title='Brands', fontsize=10, title_fontsize='12')

# Annotate data points for clarity
for year, a, s, h, x, o in zip(years, apple, samsung, huawei, xiaomi, others):
    ax.text(year, a, f'{a}%', ha='center', va='bottom', fontsize=9, color=colors[0])
    ax.text(year, s, f'{s}%', ha='center', va='bottom', fontsize=9, color=colors[1])
    ax.text(year, h, f'{h}%', ha='center', va='bottom', fontsize=9, color=colors[2])
    ax.text(year, x, f'{x}%', ha='center', va='bottom', fontsize=9, color=colors[3])
    ax.text(year, o, f'{o}%', ha='center', va='bottom', fontsize=9, color=colors[4])

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()