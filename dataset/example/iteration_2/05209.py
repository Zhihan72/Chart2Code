import matplotlib.pyplot as plt
import numpy as np

# Backstory: The chart represents the carbon emission levels across different sectors in a fictional city, Greentopia, over a span of 5 years. The city administration aims to reduce emissions and target improvements can be monitored over the years. 

# Define the sectors and the years
sectors = ['Transport', 'Industrial', 'Residential', 'Agriculture', 'Waste Management']
years = ['2017', '2018', '2019', '2020', '2021']

# Emission levels in thousand metric tons for each sector over the years
emission_levels = np.array([
    [140, 135, 130, 125, 100],  # Transport
    [200, 195, 190, 180, 170],  # Industrial
    [120, 115, 110, 108,   90],  # Residential
    [80,   75,  70,  65,   55],  # Agriculture
    [50,   47,  44,  40,   35]   # Waste Management
])

# Creating the figure and axes objects
fig, ax = plt.subplots(figsize=(14, 8))

# Calculate positions
bar_width = 0.15  # width of the bars
indices = np.arange(len(years))  # array of year index positions

# Plotting the bars for each sector
for i, sector in enumerate(sectors):
    bar_positions = indices + i * bar_width  # positions for each sector
    ax.bar(bar_positions, emission_levels[i], bar_width, label=sector)

# Adding labels and title
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Carbon Emission (Thousand Metric Tons)', fontsize=14)
ax.set_title('Carbon Emission Levels in Greentopia (2017-2021)', fontsize=16, fontweight='bold')
ax.set_xticks(indices + bar_width * len(sectors) / 2)  # placement of x-tick labels
ax.set_xticklabels(years)

# Adding legend
ax.legend(title='Sector', loc='upper right', bbox_to_anchor=(1.12, 1), fontsize='large')

# Adding grids for better readability
ax.yaxis.grid(True, linestyle='--', which='major', linewidth=0.5, alpha=0.7)

# Automatically adjust layout to avoid overlapping
plt.tight_layout()

# Display the plot
plt.show()