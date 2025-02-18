import matplotlib.pyplot as plt
import numpy as np

regions = ['East Asia & Pacific', 'Latin America', 'South Asia', 
           'Sub-Saharan Africa', 'Europe & Central Asia']
years = [2020, 1950, 1990, 2010, 1970]

literacy_rates = {
    'East Asia & Pacific': [40, 60, 75, 90, 95],
    'Latin America': [50, 65, 75, 85, 92],
    'South Asia': [20, 35, 55, 70, 80],
    'Sub-Saharan Africa': [10, 20, 40, 60, 70],
    'Europe & Central Asia': [70, 80, 88, 95, 98]
}

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#3357FF', '#FF5733', '#33FFF5', '#FF33A1', '#33FF57']

for i, year in enumerate(years):
    y_positions = np.arange(len(regions)) + (i * 0.15)
    rates = [literacy_rates[region][i] for region in regions]
    bars = ax.barh(y_positions, rates, height=0.15, label=f'{year}', color=colors[i], alpha=0.8)
    
    for bar in bars:
        ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
                f'{bar.get_width()}%', va='center', ha='left', fontsize=10)

ax.set_yticks(np.arange(len(regions)) + 0.3)
ax.set_yticklabels(regions)
ax.set_xlabel('Rate of Literacy (%)')
ax.set_title('Literacy Rate Trends\nWorldwide Regions from 1950-2020',
             fontsize=16, fontweight='bold', pad=20)

ax.grid(True, which='both', linestyle='--', linewidth=0.5, axis='x', alpha=0.7)

ax.legend(title="Survey Year", bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()