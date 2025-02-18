import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# SolarPower Inc. has multiple divisions that contribute to overall solar energy production. 
# We want to visualize the contribution of each division to the total production over several years. 

# Data: Division names and their annual production in Gigawatts (GW) from 2018 to 2022
divisions = ['North America', 'Europe', 'Asia', 'Africa', 'Australia', 'South America']
years = [2018, 2019, 2020, 2021, 2022]

# Production values for each division in each year (rows: divisions, cols: years)
production = np.array([
    [20, 21, 23, 24, 26],  # North America
    [18, 19, 22, 23, 25],  # Europe
    [15, 17, 20, 21, 23],  # Asia
    [12, 14, 16, 18, 19],  # Africa
    [10, 13, 15, 17, 18],  # Australia
    [8, 10, 12, 13, 14],   # South America
])

# Create subplots
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting data
bar_width = 0.15
bars = []
for i, year in enumerate(years):
    bar_positions = np.arange(len(divisions)) + i * bar_width
    bars.append(ax.bar(bar_positions, production[:, i], bar_width, label=f'{year}'))

# Set titles and labels
ax.set_title("SolarPower Inc. Annual Production per Division (2018-2022)\nContributions by Various Regions", fontsize=16, fontweight='bold')
ax.set_xlabel("Divisions", fontsize=14)
ax.set_ylabel("Annual Production (GW)", fontsize=14)

# Add legend
ax.legend(title='Year', fontsize=12)

# Add custom X-axis labels
ax.set_xticks(np.arange(len(divisions)) + 2 * bar_width)
ax.set_xticklabels(divisions, rotation=45, ha='right', fontsize=12)

# Adding gridlines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Add annotation for total production increase
total_production_start = production.sum(axis=0)[0]
total_production_end = production.sum(axis=0)[-1]
ax.annotate(f'Total Increase: {total_production_end - total_production_start} GW', 
             xy=(2.5, total_production_end), xytext=(3, total_production_end + 10),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=13, color='black', fontweight='bold')

# Improve layout
plt.tight_layout()

# Show plot
plt.show()