import matplotlib.pyplot as plt
import numpy as np

# Define the sectors, years, and emission levels
sectors = ['Transport', 'Industrial', 'Residential', 'Agriculture', 'Waste Management']
years = ['2017', '2018', '2019', '2020', '2021']
emission_levels = np.array([
    [140, 135, 130, 125, 100],  # Transport
    [200, 195, 190, 180, 170],  # Industrial
    [120, 115, 110, 108, 90],   # Residential
    [80, 75, 70, 65, 55],       # Agriculture
    [50, 47, 44, 40, 35]        # Waste Management
])

# Customized colors for sectors; shuffled manually
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']  # Original order
colors = ['#d62728', '#2ca02c', '#1f77b4', '#9467bd', '#ff7f0e']  # Shuffled

# Creating the figure and axes objects
fig, ax = plt.subplots(figsize=(14, 8))

# Calculate positions
bar_width = 0.15
indices = np.arange(len(years))

# Plotting the bars for each sector with shuffled colors
for i, sector in enumerate(sectors):
    bar_positions = indices + i * bar_width
    ax.bar(bar_positions, emission_levels[i], bar_width, color=colors[i], label=sector)

# Adding labels and title
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Carbon Emission (Thousand Metric Tons)', fontsize=14)
ax.set_title('Carbon Emission Levels in Greentopia (2017-2021)', fontsize=16, fontweight='bold')
ax.set_xticks(indices + bar_width * len(sectors) / 2)
ax.set_xticklabels(years)

# Adding legend
ax.legend(title='Sector', loc='upper right', bbox_to_anchor=(1.12, 1), fontsize='large')

# Adding grids for better readability
ax.yaxis.grid(True, linestyle='--', which='major', linewidth=0.5, alpha=0.7)

# Automatically adjust layout to avoid overlapping
plt.tight_layout()

# Display the plot
plt.show()