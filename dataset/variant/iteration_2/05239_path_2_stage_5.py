import matplotlib.pyplot as plt
import numpy as np

countries = ['Latteville', 'Espressonia', 'Brewland', 'Mocha Town', 'Cappuccinia']
economic_impact = [5.2, 2.1, 4.5, 3.1, 6.0]

# Sort the data based on economic impact
sorted_indices = np.argsort(economic_impact)
sorted_economic_impact = np.array(economic_impact)[sorted_indices]
sorted_countries = np.array(countries)[sorted_indices]

x_pos = np.arange(len(sorted_countries))
width = 0.35

fig, ax = plt.subplots(figsize=(7, 7))
fig.suptitle('Caffeine Culture: Economic Impact', fontsize=16, fontstyle='italic', y=0.92)

bars = ax.bar(x_pos, sorted_economic_impact, color='mediumseagreen', alpha=0.7, label='Revenue (Bn USD)')

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 0.1, f'{yval} B', ha='center', va='bottom', fontsize=12, fontweight='bold')

ax.set_title('Financial Footprint of Coffee', fontsize=12, color='darkgreen', loc='right')
ax.set_xlabel('Nations', fontsize=10, color='darkgreen')
ax.set_ylabel('Financial Gain (Billion USD)', fontsize=10, color='darkgreen')
ax.set_xticks(x_pos)
ax.set_xticklabels(sorted_countries, fontsize=10, rotation=15, ha='left')
ax.set_ylim(0, 7)

ax.grid(axis='y', linestyle=':', alpha=0.5)

ax.legend(loc='lower right', fontsize=11)

plt.tight_layout(pad=3.0, rect=[0, 0.03, 1, 0.90])

plt.show()