import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Define the categories and regions
categories = ['Solar Power', 'Wind Power', 'Hydropower', 'Geothermal', 'Biomass']
regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa']

# Number of variables (categories)
num_vars = len(categories)

# Data for each region (percentage of renewable energy usage in each category)
data = {
    'North America': [20, 15, 30, 10, 25],
    'Europe': [25, 20, 25, 15, 15],
    'Asia': [15, 25, 35, 10, 15],
    'South America': [30, 10, 40, 10, 10],
    'Africa': [20, 10, 25, 15, 30],
}

# Calculate the angle for each category
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the circle

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Plot each region's renewable energy distribution
colors = ['#FF6347', '#4682B4', '#8A2BE2', '#3CB371', '#FFD700']
for region, color in zip(data.keys(), colors):
    values = data[region]
    values += values[:1]  # Repeat the first value to close the chart
    ax.plot(angles, values, linewidth=2, linestyle='solid', label=region, color=color)
    ax.fill(angles, values, color=color, alpha=0.25)

# Add labels for each category
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, color='gray')

# Set the chart range
ax.set_ylim(0, 40)

# Add a title and legend
plt.title("Global Renewable Energy Distribution by Region in 2025", fontsize=16, fontweight='bold', pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the radar chart
plt.show()