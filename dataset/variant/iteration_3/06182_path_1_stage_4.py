import numpy as np
import matplotlib.pyplot as plt

# Define years and regions
years = np.arange(2011, 2022)
regions = ["South America", "North America", "Australia", "Europe", "Africa", "Asia", "Middle East", "Antarctica"]

# Adoption rates (%) data
adoption_rates = np.array([
    [3, 5, 7, 9, 11, 14, 17, 19, 21, 24, 26],    # South America
    [5, 7, 9, 11, 14, 16, 19, 22, 25, 27, 30],    # North America
    [6, 8, 11, 13, 16, 18, 21, 23, 26, 28, 31],   # Australia
    [8, 10, 12, 15, 18, 21, 23, 25, 28, 30, 32],  # Europe
    [2, 3, 4, 5, 7, 9, 11, 13, 15, 18, 20],       # Africa
    [10, 14, 18, 21, 25, 28, 32, 35, 39, 42, 45], # Asia
    [4, 5, 7, 9, 11, 13, 15, 17, 20, 22, 25],     # Middle East
    [1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8]             # Antarctica
])

# Create a mask for the upper triangle
mask = np.triu(np.ones_like(adoption_rates, dtype=bool))

fig, ax = plt.subplots(figsize=(8, 8))

# Create lower triangle heatmap for Adoption Rates
adoption_masked = np.ma.masked_array(adoption_rates, mask)
im = ax.imshow(adoption_masked, cmap='YlGnBu', aspect='auto')
ax.set_title('Global Clean Energy Rise (%)\n(2011-2021)', fontsize=16, weight='bold')
ax.set_xticks(np.arange(len(years)))
ax.set_yticks(np.arange(len(regions)))
ax.set_xticklabels(years, rotation=45, ha='right')
ax.set_yticklabels(regions)
for i in range(len(regions)):
    for j in range(len(years)):
        if i >= j:
            ax.text(j, i, f'{adoption_rates[i, j]}%', ha='center', va='center', color='black')
cbar = plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label('Growth Rate (%)', rotation=270, labelpad=20)

plt.suptitle('Renewable Energy Adoption (%)\n(2011-2021)', fontsize=18, weight='bold')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.show()