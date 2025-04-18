import matplotlib.pyplot as plt
import numpy as np

# Years from 2000 to 2020
years = np.arange(2000, 2021)

# Data for each plant type (in acres)
trees_area = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 110, 120])
shrubs_area = np.array([5, 6, 8, 10, 12, 15, 18, 21, 25, 29, 34, 38, 43, 47, 50, 55, 60, 65, 70, 76, 80])
flowers_area = np.array([2, 4, 8, 12, 15, 18, 22, 25, 29, 32, 35, 38, 40, 45, 48, 52, 55, 58, 62, 65, 68])
herbs_area = np.array([1, 2, 3, 5, 8, 12, 15, 18, 21, 24, 28, 31, 35, 38, 42, 45, 48, 50, 55, 58, 60])
grasses_area = np.array([3, 5, 6, 8, 10, 12, 14, 16, 18, 21, 23, 26, 28, 30, 32, 35, 37, 40, 42, 44, 46])

# Create the stacked area plot
fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, trees_area, shrubs_area, flowers_area, herbs_area, grasses_area,
             colors=['#228B22', '#32CD32', '#FF69B4', '#BA55D3', '#ADFF2F'],
             alpha=0.8)

# Customize x-ticks to show only year numbers
ax.set_xticks(years[::2])
ax.set_xticklabels([str(year) for year in years[::2]], rotation=45, ha='right', fontsize=12)
ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))

# Adding grid lines for readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()