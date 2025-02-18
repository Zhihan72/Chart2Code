import matplotlib.pyplot as plt
import numpy as np

regions = ['Sub-Sah. Afr.', 'S. Asia', 'Lat. Am.', 
           'E. Asia & Pac.', 'Eur. & Cent. Asia']
years = [1950, 1970, 1990, 2010, 2020]

literacy_rates = {
    'Sub-Sah. Afr.': [20, 10, 70, 60, 40],
    'S. Asia': [55, 70, 35, 20, 80],
    'Lat. Am.': [92, 75, 65, 50, 85],
    'E. Asia & Pac.': [90, 40, 60, 95, 75],
    'Eur. & Cent. Asia': [95, 88, 98, 70, 80]
}

fig, ax = plt.subplots(figsize=(14, 8))

# Original colors: ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF5']
# Rotated colors to shuffle without using random
colors = ['#33FFF5', '#FF5733', '#33FF57', '#3357FF', '#FF33A1']

for i, year in enumerate(years):
    rates = [literacy_rates[region][i] for region in regions]
    sorted_indices = np.argsort(rates)
    
    sorted_rates = [rates[idx] for idx in sorted_indices]
    sorted_regions = [regions[idx] for idx in sorted_indices]

    y_positions = np.arange(len(sorted_regions)) + (i * 0.15)
    bars = ax.barh(y_positions, sorted_rates, height=0.15, color=colors[i], alpha=0.8)

    for bar in bars:
        ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
                f'{bar.get_width()}%', va='center', ha='left', fontsize=10)

ax.set_yticks(np.arange(len(regions)) + 0.3)
ax.set_yticklabels(sorted_regions)
ax.set_xlabel('Literacy (%)')
ax.set_title('Literacy Rates (1950-2020)', fontsize=16, fontweight='bold', pad=20)

plt.tight_layout()
plt.show()