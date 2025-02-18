import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# This chart explores the fictional land of Nutrivia over the years 2010 to 2020, where different types of crops 
# have been grown to nourish the population. It showcases the annual yield of major crops - Wheat, Rice, Maize, 
# Soy, and Barley. The goal is to analyze how the agricultural trend has changed over the decade in Nutrivia.

# Define years for the x-axis
years = np.arange(2010, 2021)

# Annual yield data in million metric tons for each crop
wheat = np.array([60, 62, 65, 70, 75, 78, 80, 82, 85, 90, 95])
rice = np.array([40, 42, 43, 45, 47, 50, 53, 55, 58, 60, 62])
maize = np.array([30, 32, 34, 36, 39, 42, 45, 48, 52, 56, 60])
soy = np.array([20, 22, 23, 25, 27, 30, 32, 35, 37, 40, 45])
barley = np.array([10, 11, 12, 13, 14, 15, 16, 17, 19, 21, 23])

# Organize the data for stackplot
data = np.vstack([wheat, rice, maize, soy, barley])
crops = ['Wheat', 'Rice', 'Maize', 'Soy', 'Barley']

# Define colors for each crop
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(years, data, labels=crops, colors=colors, alpha=0.8)

# Titles and labels
ax.set_title("A Decade of Harvest in Nutrivia:\nCrop Yield Trends from 2010-2020", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Annual Yield (Million Metric Tons)", fontsize=14)

# Annotate the final year's data point for each crop
for i, crop in enumerate(crops):
    ax.text(years[-1] + 0.1, data[:, -1].cumsum()[i], f'{crop}', color=colors[i], fontsize=12, verticalalignment='center')

# Add a grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Rotating the x-axis labels for clarity
plt.xticks(years, rotation=45)

# Adding a legend outside the plot area to avoid overlapping
ax.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1, 1))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()