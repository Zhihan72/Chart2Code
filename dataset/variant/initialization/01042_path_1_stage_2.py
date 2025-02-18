import matplotlib.pyplot as plt
import numpy as np

regions = ['Sub-Saharan Africa', 'South Asia', 'Latin America', 
           'East Asia & Pacific', 'Europe & Central Asia']
years = [1950, 1970, 1990, 2010, 2020]

literacy_rates = {
    'Sub-Saharan Africa': [10, 20, 40, 60, 70],
    'South Asia': [20, 35, 55, 70, 80],
    'Latin America': [50, 65, 75, 85, 92],
    'East Asia & Pacific': [40, 60, 75, 90, 95],
    'Europe & Central Asia': [70, 80, 88, 95, 98]
}

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF5']

# Iterate over each year to plot sorted bar charts
for i, year in enumerate(years):
    # Extract and sort literacy rates and corresponding regions
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
# Note: Y-ticks are set dynamically for each subplot iteration but remain fixed across subplots here
ax.set_yticklabels(sorted_regions)
ax.set_xlabel('Literacy Rate (%)')
ax.set_title('Evolution of Literacy Rates (1950-2020)\nAcross Different World Regions',
             fontsize=16, fontweight='bold', pad=20)

plt.tight_layout()

plt.show()