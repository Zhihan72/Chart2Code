import matplotlib.pyplot as plt
import numpy as np

# Backstory: Analysis of the growth of different renewable energy sources in Europe over the last 5 years.
# The chart will show the annual energy production (in TWh) from different renewable sources.

# Define the years and renewable energy sources
years = ['2018', '2019', '2020', '2021', '2022']
sources = ['Solar', 'Wind', 'Hydropower', 'Biomass']

# Energy production data in TWh for each year
energy_production = np.array([
    [50, 65, 80, 90, 100],   # Solar
    [70, 80, 85, 95, 110],   # Wind
    [100, 105, 110, 115, 120],  # Hydropower
    [30, 35, 40, 45, 50]     # Biomass
])

# Define position and width for the bars
positions = np.arange(len(years))
bar_width = 0.2

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Colors for each renewable energy source
colors = ['#FFD700', '#1E90FF', '#32CD32', '#8B4513']

# Plot bars for each energy source
for i, source in enumerate(sources):
    ax.bar(positions + i*bar_width, energy_production[i], bar_width, label=source, color=colors[i])

# Adding labels, title, and legend
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Production (TWh)', fontsize=12)
ax.set_title('Growth of Renewable Energy Production in Europe (2018-2022)', fontsize=14, fontweight='bold')
ax.set_xticks(positions + bar_width*1.5)
ax.set_xticklabels(years, fontsize=10)
ax.legend(title='Energy Source', fontsize=10, title_fontsize=12)

# Adding gridlines for better readability
ax.yaxis.grid(True)
ax.xaxis.grid(False)

# Automatically adjust layout to prevent overlaps
plt.tight_layout()

# Show the plot
plt.show()