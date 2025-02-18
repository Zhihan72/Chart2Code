import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# Let's create a chart comparing the annual revenue of different cafés in a city from 2015 to 2020.
# Three types of cafés are being analyzed: Coffee Shops, Tea Houses, and Mixed Beverage Cafés.
# We want to visualize the revenues with bar charts for individual years and a line chart overlay to show the trend.

# Café names
cafes = ['Coffee Shops', 'Tea Houses', 'Mixed Beverage Cafés']

# Annual revenue in thousands (data in the form of Python lists)
revenue_2015 = [250, 180, 200]
revenue_2016 = [265, 190, 210]
revenue_2017 = [300, 210, 220]
revenue_2018 = [320, 230, 250]
revenue_2019 = [340, 240, 260]
revenue_2020 = [360, 260, 270]

# Collect data into an array for easy line plotting
years = [2015, 2016, 2017, 2018, 2019, 2020]
revenue = np.array([revenue_2015, revenue_2016, revenue_2017, revenue_2018, revenue_2019, revenue_2020])

# Define plot colors for different café types
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Initialize plot
fig, ax1 = plt.subplots(figsize=(12, 6))

# Title and labels
fig.suptitle('Annual Revenue Comparison of Cafés (2015-2020)', fontsize=16, fontweight='bold', color='darkslategray')
ax1.set_title('Revenue in Thousands of Dollars', fontsize=14, color='indigo')
ax1.set_xlabel('Year', fontsize=12, labelpad=10)
ax1.set_ylabel('Revenue ($)', fontsize=12, labelpad=10)

# Plot bars for each year
width = 0.2  # Width of each bar
x = np.arange(len(years))  # Label locations

# Create bar charts for each café type
for i, cafe in enumerate(cafes):
    ax1.bar(x - width + i*width, revenue[:, i], width, label=cafe, color=colors[i], alpha=0.75, edgecolor='black')

# Overlay line plots to show trends
for i, cafe in enumerate(cafes):
    ax1.plot(x, revenue[:, i], marker='o', linestyle='-', color=colors[i], linewidth=2.5)
    for j in range(len(years)):
        ax1.text(x[j] + (i-1)*width, revenue[j, i] + 5, str(revenue[j, i]), ha='center', va='bottom', fontsize=10, fontweight='bold', color=colors[i])

# Customize ticks and legend
ax1.set_xticks(x)
ax1.set_xticklabels(years, fontsize=11)
ax1.legend(loc='upper left', fontsize=11, title='Café Types', title_fontsize='13')

# Grid for clarity
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust plot layout
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Show the plot
plt.show()