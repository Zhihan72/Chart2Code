import numpy as np
import matplotlib.pyplot as plt

# Data for average monthly rainfall (in mm) for six continents over a year
continents = ['Afr', 'Asia', 'Eur', 'N. Am', 'S. Am', 'Aus']  # Added Australia
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

rainfall_data = np.array([
    [70, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10],  # Africa
    [80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25],  # Asia
    [60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5],   # Europe
    [90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35],  # North America
    [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45], # South America
    [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105] # Australia (newly added)
])

# Calculate the yearly average for each continent
yearly_avg = rainfall_data.mean(axis=0)

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Define colors for each continent
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']  # Added new color

# Create a bar for each month and continent
width = 0.12  # Adjust width for six bars
x = np.arange(len(months))  # label locations

for i, continent in enumerate(continents):
    ax.bar(x + width * i, rainfall_data[i], width, label=continent, color=colors[i])

# Plot the yearly average line
ax.plot(x + 2.5 * width, yearly_avg, marker='o', color='black', label='Avg', linestyle='-')

# Set axis labels
ax.set_xlabel('Mnths', fontsize=12)
ax.set_ylabel('Rainfall (mm)', fontsize=12)
ax.set_title('Avg Rainfall', fontsize=14, fontweight='bold')

# X and Y ticks and labels
ax.set_xticks(x + 2.5 * width)
ax.set_xticklabels(months, rotation=45, fontsize=10)
ax.yaxis.grid(True)

# Add a legend
ax.legend(loc='upper right', fontsize=10)

# Automatically adjust layout to prevent text overlap
plt.tight_layout()

# Display the chart
plt.show()