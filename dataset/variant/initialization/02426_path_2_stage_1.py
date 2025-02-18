import matplotlib.pyplot as plt

# Data for growth rates in different climate zones (in cm/year)
growth_data = [
    [60, 65, 58, 62, 68, 61, 63, 64, 66, 60, 67, 65],  # Tropical
    [35, 40, 38, 42, 37, 39, 41, 36, 34, 43, 38, 39],  # Temperate
    [10, 12, 11, 9, 13, 14, 8, 11, 12, 15, 10, 9],     # Desert
    [5, 4, 6, 3, 4, 5, 5, 6, 3, 4, 4, 5]              # Polar
]

# Define labels for each climate zone
climate_zones = ['Tropical', 'Temperate', 'Desert', 'Polar']

# Create the vertical box plot
plt.figure(figsize=(10, 6))
plt.boxplot(growth_data, patch_artist=True, labels=climate_zones, notch=True, medianprops={'color': 'red'})

# Remove borders, legends, and grids
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)

# Add title and labels
plt.title('Growth Rates of Plantus Hypotheticus in Different Climate Zones', fontsize=14, fontweight='bold')
plt.xlabel('Climate Zones', fontsize=12)
plt.ylabel('Growth Rate (cm/year)', fontsize=12)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()