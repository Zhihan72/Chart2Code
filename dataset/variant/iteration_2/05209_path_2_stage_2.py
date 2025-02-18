import matplotlib.pyplot as plt
import numpy as np

# Sectors remain the same to maintain the structure
sectors = ['Transport', 'Industrial', 'Residential', 'Agriculture', 'Waste Management']
years = ['2017', '2018', '2019', '2020', '2021']

# Manually shuffled emission levels for randomness
emission_levels = np.array([
    [135, 125, 140, 100, 130],  # Transport (shuffled)
    [180, 170, 200, 190, 195],  # Industrial (shuffled)
    [108, 110, 120, 115,  90],  # Residential (shuffled)
    [65,   80,  70,  55,   75],  # Agriculture (shuffled)
    [44,   35,  47,  50,  40]   # Waste Management (shuffled)
])

fig, ax = plt.subplots(figsize=(14, 8))

bar_height = 0.15
indices = np.arange(len(sectors))

for i, year in enumerate(years):
    bar_positions = indices + i * bar_height
    ax.barh(bar_positions, emission_levels[:, i], bar_height, label=year)

ax.set_ylabel('Sector', fontsize=14)
ax.set_xlabel('Carbon Emission (Thousand Metric Tons)', fontsize=14)
ax.set_title('Carbon Emission Levels in Greentopia (2017-2021)', fontsize=16, fontweight='bold')
ax.set_yticks(indices + bar_height * len(years) / 2)
ax.set_yticklabels(sectors)

ax.legend(title='Year', loc='upper right', bbox_to_anchor=(1.12, 1), fontsize='large')
ax.xaxis.grid(True, linestyle='--', which='major', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()