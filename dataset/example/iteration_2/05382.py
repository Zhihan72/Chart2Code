import matplotlib.pyplot as plt
import numpy as np

# Backstory: Solar Power Expansion in Fictitious Town "Solarville" (2000-2020)
# Solarville has been tracking its solar energy production in three key sectors:
# Residential, Commercial, and Industrial, showing remarkable growth over 20 years.

# Define the years for the x-axis
years = np.arange(2000, 2021)

# Define solar energy production data (in GWh) for each sector over the years
residential_production = np.array([1, 1, 2, 3, 4, 5, 7, 9, 12, 15, 19, 24, 30, 37, 45, 54, 64, 75, 87, 100, 114])
commercial_production = np.array([2, 2, 3, 4, 6, 8, 11, 14, 18, 23, 29, 36, 44, 53, 63, 74, 86, 99, 113, 128, 144])
industrial_production = np.array([1, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210])

# Stack the data for the area chart
production_data = np.vstack([residential_production, commercial_production, industrial_production])

# Set up the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Define colors and labels for each sector
colors = ['#FFD700', '#FF8C00', '#CD5C5C']
labels = ['Residential', 'Commercial', 'Industrial']

# Create an area chart using stackplot
ax.stackplot(years, production_data, labels=labels, colors=colors, alpha=0.7)

# Set title and labels
ax.set_title('Solar Energy Production Growth in Solarville (2000-2020)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14, labelpad=10)
ax.set_ylabel('Energy Production (GWh)', fontsize=14, labelpad=10)

# Customizing the ticks and grid for better readability
ax.set_xticks(years[::2])
ax.set_yticks(np.arange(0, 451, 50))
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Add a legend
ax.legend(loc='upper left', fontsize=12, title='Sectors', title_fontsize='12')

# Add annotations for significant milestones
ax.annotate('First Solar Panels Installed', xy=(2000, 4), xytext=(2003, 60),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=12, color='blue', fontweight='bold')

ax.annotate('Residential Growth Surge', xy=(2010, 19), xytext=(2014, 180),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=12, color='red', fontweight='bold')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()