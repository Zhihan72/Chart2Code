import matplotlib.pyplot as plt

# New Biomass data (in arbitrary units) for Urban ecosystem over four quarters
urban_biomass = [50, 55, 60, 65, 47, 53, 58, 63, 45, 50, 55, 60, 40, 45, 50, 55]

# Updated dataset for Box Plot
biomass_data = [
    [250, 270, 300, 320, 240, 260, 290, 310, 230, 250, 280, 300, 220, 230, 240, 260], # Forest
    [150, 155, 160, 165, 140, 145, 150, 155, 135, 140, 145, 150, 130, 135, 140, 145], # Wetland
    [180, 185, 190, 195, 175, 180, 185, 190, 170, 175, 180, 185, 165, 170, 175, 180], # Grassland
    [70, 72, 75, 78, 65, 68, 70, 73, 60, 63, 65, 68, 55, 58, 60, 63], # Desert
    [200, 205, 210, 215, 195, 200, 205, 210, 190, 195, 200, 205, 185, 190, 195, 200], # Marine
    urban_biomass
]

# Updated labels for each ecosystem
ecosystems = ["Forest", "Wetland", "Grassland", "Desert", "Marine", "Urban"]

# Create Figure and Axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot
boxplots = ax.boxplot(biomass_data, patch_artist=True,
                    boxprops=dict(facecolor='lightblue', color='darkblue'),
                    whiskerprops=dict(color='darkblue'),
                    capprops=dict(color='darkblue'),
                    medianprops=dict(color='red', linewidth=2),
                    flierprops=dict(marker='o', color='red', alpha=0.5))

# Colors
colors = ['lightgreen', 'lightcoral', 'lightskyblue', 'lightgoldenrodyellow', 'lightpink', 'lightgray']
for patch, color in zip(boxplots['boxes'], colors):
    patch.set_facecolor(color)

# Labels
ax.set_xticklabels(ecosystems)
ax.set_xlabel('Ecosystems', fontsize=14)
ax.set_ylabel('Biomass (Arbitrary Units)', fontsize=14)

plt.tight_layout()
plt.show()