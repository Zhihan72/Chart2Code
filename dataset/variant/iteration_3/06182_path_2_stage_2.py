import numpy as np
import matplotlib.pyplot as plt

# Define years and regions
years = np.arange(2011, 2022)
regions = ["Australia", "Middle East", "Africa", "North America", "Asia", "Europe", "South America"]

# Adoption rates (%) data
adoption_rates = np.array([
    [5, 7, 9, 11, 14, 16, 19, 22, 25, 27, 30],   # North America
    [8, 10, 12, 15, 18, 21, 23, 25, 28, 30, 32], # Europe
    [10, 14, 18, 21, 25, 28, 32, 35, 39, 42, 45],# Asia
    [2, 3, 4, 5, 7, 9, 11, 13, 15, 18, 20],      # Africa
    [3, 5, 7, 9, 11, 14, 17, 19, 21, 24, 26],    # South America
    [6, 8, 11, 13, 16, 18, 21, 23, 26, 28, 31],  # Australia
    [4, 5, 7, 9, 11, 13, 15, 17, 20, 22, 25]     # Middle East
])

# Efficiency improvement data (%/year)
efficiency_improvement = np.array([
    [0.5, 0.6, 0.8, 0.9, 1.1, 1.3, 1.5, 1.7, 1.9, 2.0, 2.2],   # North America
    [0.6, 0.7, 0.9, 1.1, 1.3, 1.6, 1.8, 2.0, 2.3, 2.5, 2.7],   # Europe
    [0.7, 0.9, 1.1, 1.3, 1.6, 1.9, 2.1, 2.4, 2.6, 2.8, 3.0],   # Asia
    [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0, 1.2, 1.4, 1.5, 1.7],   # Africa
    [0.4, 0.5, 0.7, 0.8, 1.0, 1.2, 1.5, 1.8, 2.0, 2.2, 2.4],   # South America
    [0.5, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.9, 2.1, 2.3, 2.5],   # Australia
    [0.4, 0.5, 0.7, 0.8, 1.0, 1.2, 1.4, 1.6, 1.9, 2.1, 2.3]    # Middle East
])

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

# Heatmap for Efficiency Improvement
im1 = axs[0].imshow(efficiency_improvement, cmap='Oranges', aspect='auto')

# Annotate and label the heatmap
axs[0].set_title('Efficiency Enhancement of Solar Panels (% over Years)\n(2011 to 2021)', fontsize=16, weight='bold')
axs[0].set_xticks(np.arange(len(years)))
axs[0].set_yticks(np.arange(len(regions)))
axs[0].set_xticklabels(years, rotation=45, ha='right')
axs[0].set_yticklabels(['Oz', 'M.E', 'Afr', 'N.Am', 'Asia', 'Eur', 'S.Am'])
for i in range(len(regions)):
    for j in range(len(years)):
        axs[0].text(j, i, f'{efficiency_improvement[i, j]:.1f}%', ha='center', va='center', color='black')
cbar1 = plt.colorbar(im1, ax=axs[0], fraction=0.046, pad=0.04)
cbar1.set_label('Efficiency Increment (%/year)', rotation=270, labelpad=25)

# Heatmap for Adoption Rates
im2 = axs[1].imshow(adoption_rates, cmap='YlGnBu', aspect='auto')

# Annotate and label the heatmap
axs[1].set_title('Rate of Adoption of Solar Panels (%)\nFor the Period 2011-2021', fontsize=16, weight='bold')
axs[1].set_xticks(np.arange(len(years)))
axs[1].set_yticks(np.arange(len(regions)))
axs[1].set_xticklabels(years, rotation=45, ha='right')
axs[1].set_yticklabels(['Oz', 'M.E', 'Afr', 'N.Am', 'Asia', 'Eur', 'S.Am'])
for i in range(len(regions)):
    for j in range(len(years)):
        axs[1].text(j, i, f'{adoption_rates[i, j]}%', ha='center', va='center', color='black')
cbar2 = plt.colorbar(im2, ax=axs[1], fraction=0.046, pad=0.04)
cbar2.set_label('Adoption Percentage (%)', rotation=270, labelpad=25)

# Main title for the chart
plt.suptitle('Solar Panel Trends: Adoption & Efficiency\nFrom 2011 to 2021', fontsize=18, weight='bold')

# Adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Display the plot
plt.show()