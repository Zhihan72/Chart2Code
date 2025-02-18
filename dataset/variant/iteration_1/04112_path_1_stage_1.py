import matplotlib.pyplot as plt
import numpy as np

# Years of observation
years = np.array([2005, 2007, 2009, 2011, 2013, 2015, 2017, 2019, 2021, 2023])

# Data for different bird species
species_a_landing_density = np.array([30, 35, 33, 37, 45, 50, 55, 60, 62, 65])
species_b_landing_density = np.array([20, 25, 27, 30, 32, 35, 38, 40, 42, 45])
species_c_landing_density = np.array([10, 15, 13, 17, 23, 25, 27, 30, 32, 35])

# Create a figure
fig, ax = plt.subplots(figsize=(14, 8))

# Create horizontal bar chart
bar_width = 0.25
indices = np.arange(len(years))
ax.barh(indices, species_a_landing_density, bar_width, color='red', alpha=0.7, label='Species A')
ax.barh(indices + bar_width, species_b_landing_density, bar_width, color='green', alpha=0.7, label='Species B')
ax.barh(indices + 2 * bar_width, species_c_landing_density, bar_width, color='blue', alpha=0.7, label='Species C')

# Titles and labels
ax.set_title('Migration Patterns of Bird Species (2005 - 2023)', fontsize=16, fontweight='bold', color='navy')
ax.set_xlabel('Landing Density (Birds per km²)', fontsize=12)
ax.set_ylabel('Year', fontsize=12)
ax.set_yticks(indices + bar_width)
ax.set_yticklabels(years)

# Adding legend
ax.legend(loc='upper right', fontsize=12)

# Grid
ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()