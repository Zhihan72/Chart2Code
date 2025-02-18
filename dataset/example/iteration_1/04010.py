import matplotlib.pyplot as plt
import numpy as np

# Backstory: The Journey of Renewable Energy Adoption in Different Sectors Over Two Decades
# We will plot the adoption rates of renewable energy across various sectors from 2000 to 2020.

# Years for the timeline
years = np.arange(2000, 2021)

# Percentage of renewable energy usage for each sector
residential = [2, 2.5, 3, 3.8, 4.5, 5.5, 6.5, 7.8, 9, 10.5, 12, 14, 16, 18.5, 21, 24.2, 27.5, 31, 35, 39.5, 44]
commercial = [1, 1.2, 1.5, 2, 2.6, 3.2, 3.9, 4.7, 5.6, 6.6, 7.8, 9, 10.4, 12, 13.7, 15.5, 17.5, 19.7, 22, 24.5, 27]
industrial = [0.5, 0.8, 1.2, 1.6, 2.1, 2.7, 3.4, 4.1, 5, 6, 7.1, 8.3, 9.7, 11.2, 12.9, 14.7, 16.7, 18.8, 21, 23.4, 26]
transportation = [0.1, 0.15, 0.2, 0.3, 0.5, 0.8, 1.2, 1.7, 2.3, 3, 4, 5.1, 6.4, 7.8, 9.4, 11.2, 13, 15, 17, 19.2, 21.5]

# Create a stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))

# Stack the renewable energy usage data
ax.stackplot(years, residential, commercial, industrial, transportation,
             labels=['Residential', 'Commercial', 'Industrial', 'Transportation'],
             colors=['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3'], alpha=0.8)

# Title and labels
ax.set_title("The Journey of Renewable Energy Adoption: 2000-2020", fontsize=16, pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Percentage of Renewable Energy Usage", fontsize=14)

# Customize grid and ticks
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax.set_xticks(years[::2])  # Show every two years
ax.set_yticks(np.arange(0, 51, 5))

# Rotate the x-tick labels for better readability
ax.set_xticklabels(years[::2], rotation=45, ha='right')

# Adding legend outside the plot
ax.legend(loc='upper left', fontsize=12, bbox_to_anchor=(1, 1), title="Sectors")

# Adjust layout to prevent overlapping text
plt.tight_layout()

# Show the plot
plt.show()