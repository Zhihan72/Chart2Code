import numpy as np
import matplotlib.pyplot as plt

# Title and backstory:
# A bar chart comparing the average monthly rainfall across five different continents.

# Data for the average monthly rainfall (in mm) for five continents over a year
continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

rainfall_data = np.array([
    [70, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10],  # Africa
    [80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25],  # Asia
    [60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5],   # Europe
    [90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35],  # North America
    [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45]  # South America
])

# Calculate the yearly average for each continent
yearly_avg = rainfall_data.mean(axis=0)

# Create the plot
fig, ax = plt.subplots(figsize=(15, 9))

# Define colors for each continent
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create a bar for each month and continent
width = 0.15  # the width of the bars
x = np.arange(len(months))  # label locations

for i, continent in enumerate(continents):
    ax.bar(x + width * i, rainfall_data[i], width, label=continent, color=colors[i])

# Plot the yearly average line
ax.plot(x + 2 * width, yearly_avg, marker='o', color='black', label='Yearly Average', linestyle='-')

# Set axis labels
ax.set_xlabel('Months', fontsize=14)
ax.set_ylabel('Average Rainfall (mm)', fontsize=14)
ax.set_title('Average Monthly Rainfall Across Continents', fontsize=16, fontweight='bold')

# X and Y ticks and labels
ax.set_xticks(x + width * 2)
ax.set_xticklabels(months, rotation=45, fontsize=12)
ax.yaxis.grid(True)

# Add a legend
ax.legend(loc='upper right', fontsize=12)

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the chart
plt.show()