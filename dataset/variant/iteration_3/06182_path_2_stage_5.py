import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2011, 2022)
regions = ["Europe", "South America", "Africa", "North America", "Asia", "Australia", "Middle East"]

adoption_rates = np.array([
    [8, 9, 13, 14, 18, 19, 22, 25, 27, 30, 31],
    [3, 6, 7, 8, 11, 15, 16, 18, 21, 23, 25],
    [3, 3, 4, 5, 8, 9, 10, 14, 15, 19, 20],
    [5, 8, 11, 12, 14, 16, 19, 23, 25, 27, 29],
    [10, 13, 18, 22, 24, 30, 32, 33, 40, 41, 44],
    [7, 8, 10, 13, 17, 17, 22, 22, 26, 27, 31],
    [4, 6, 8, 9, 12, 13, 16, 18, 21, 21, 24]
])

efficiency_improvement = np.array([
    [0.5, 0.8, 0.9, 1.2, 1.4, 1.5, 1.7, 1.9, 2.3, 2.4, 2.6],
    [0.5, 0.4, 0.7, 0.9, 1.1, 1.1, 1.4, 1.7, 2.1, 2.0, 2.5],
    [0.3, 0.5, 0.5, 0.6, 0.9, 0.8, 1.1, 1.3, 1.3, 1.6, 1.7],
    [0.4, 0.6, 0.9, 1.0, 1.2, 1.3, 1.4, 1.8, 1.9, 2.0, 2.1],
    [0.6, 0.9, 1.0, 1.3, 1.5, 1.7, 2.2, 2.3, 2.5, 2.9, 3.0],
    [0.4, 0.6, 0.9, 1.1, 1.3, 1.5, 1.6, 1.8, 2.0, 2.3, 2.6],
    [0.5, 0.6, 0.8, 0.9, 0.9, 1.2, 1.5, 1.7, 1.8, 2.1, 2.4]
])

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

# Change heatmap appearance
im1 = axs[0].imshow(efficiency_improvement, cmap='cool', aspect='auto')
axs[0].set_title('Efficiency Improvement (% over Years)\n(2011 to 2021)', fontsize=14, weight='normal')
axs[0].set_xticks(np.arange(len(years)))
axs[0].set_yticks(np.arange(len(regions)))
axs[0].set_xticklabels(years, rotation=30, ha='right', fontstyle='italic')
axs[0].set_yticklabels(['Europe', 'S. Amer', 'Afr', 'N. Amer', 'Asia', 'Aus', 'Mid. East'], fontstyle='italic')
for i in range(len(regions)):
    for j in range(len(years)):
        axs[0].text(j, i, f'{efficiency_improvement[i, j]:.1f}', ha='center', va='center', color='darkblue')

# Adjust colorbar position and formatting
cbar1 = plt.colorbar(im1, ax=axs[0], fraction=0.05, pad=0.02)
cbar1.set_label('Increment (%/yr)', rotation=270, labelpad=20)

# Change markers and lines
im2 = axs[1].imshow(adoption_rates, cmap='viridis', aspect='auto')
axs[1].set_title('Adoption Rates (%)\n2011 to 2021', fontsize=14, weight='normal')
axs[1].set_xticks(np.arange(len(years)))
axs[1].set_yticks(np.arange(len(regions)))
axs[1].set_xticklabels(years, rotation=30, ha='right', fontstyle='italic')
axs[1].set_yticklabels(['Europe', 'S. Amer', 'Afr', 'N. Amer', 'Asia', 'Aus', 'Mid. East'], fontstyle='italic')
for i in range(len(regions)):
    for j in range(len(years)):
        axs[1].text(j, i, f'{adoption_rates[i, j]}', ha='center', va='center', color='darkgreen')

# Change colorbar label
cbar2 = plt.colorbar(im2, ax=axs[1], fraction=0.05, pad=0.02)
cbar2.set_label('Adoption (%)', rotation=270, labelpad=20)

plt.suptitle('Trends in Solar Panel Technology and Adoption\n2011 - 2021', fontsize=16, weight='bold')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()