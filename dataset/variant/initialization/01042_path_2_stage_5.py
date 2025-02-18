import matplotlib.pyplot as plt
import numpy as np

regions = ['East Asia & Pacific', 'Latin America', 'South Asia', 
           'Sub-Saharan Africa', 'Europe & Central Asia']
years = [2020, 1950, 1990, 2010, 1970]

# Shuffle literacy rates within each region
literacy_rates = {
    'East Asia & Pacific': [95, 40, 75, 90, 60],  # altered order
    'Latin America': [85, 75, 92, 65, 50],        # altered order
    'South Asia': [55, 80, 70, 20, 35],           # altered order
    'Sub-Saharan Africa': [60, 40, 70, 10, 20],   # altered order
    'Europe & Central Asia': [88, 70, 95, 80, 98] # altered order
}

fig, ax = plt.subplots(figsize=(14, 8))

styles = [{'color': '#FF5733', 'linestyle': '-', 'marker': 'o'},
          {'color': '#33FF57', 'linestyle': '--', 'marker': 's'},
          {'color': '#FF33A1', 'linestyle': '-.', 'marker': 'D'},
          {'color': '#33FFF5', 'linestyle': ':', 'marker': '^'},
          {'color': '#3357FF', 'linestyle': '-', 'marker': 'x'}]

for i, year in enumerate(years):
    rates = [(region, literacy_rates[region][i]) for region in regions]
    rates.sort(key=lambda x: x[1], reverse=True)
    
    sorted_regions = [x[0] for x in rates]
    sorted_rates = [x[1] for x in rates]

    y_positions = np.arange(len(sorted_regions)) + (i * 0.15)
    ax.plot(sorted_rates, y_positions, label=f'{year}', **styles[i], linewidth=2, markersize=7)
    
    for x, y in zip(sorted_rates, y_positions):
        ax.text(x + 1, y, f'{x}%', va='center', ha='left', fontsize=10)

ax.set_yticks(np.arange(len(regions)) + 0.3)
ax.set_yticklabels(sorted_regions)
ax.set_xlabel('Rate of Literacy (%)')
ax.set_xlim(0, 105)
ax.set_title('Literacy Rate Trends\nWorldwide Regions from 1950-2020',
             fontsize=16, fontweight='bold', pad=20)

ax.grid(True, which='major', linestyle=':', linewidth=0.8, axis='x', alpha=0.6)

ax.legend(title="Survey Year", bbox_to_anchor=(1, 0.5), loc='center left', fontsize='small')

plt.tight_layout()
plt.show()