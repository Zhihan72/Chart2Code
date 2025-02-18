import matplotlib.pyplot as plt
import numpy as np

# Data for the plot
planets = ['Zorg', 'Marzipan', 'Venusian', 'Jovian', 'Saturnine', 'Neptunic', 'Plutonian']
commodities = ['H2O', 'Alloys', 'Cuisine', 'Tech', 'Power', 'Transit']
trade_volumes = {
    'H2O': [120, 60, 30, 90, 110, 50, 70],
    'Alloys': [85, 140, 60, 80, 95, 40, 65],
    'Cuisine': [200, 95, 120, 180, 160, 85, 100],
    'Tech': [150, 130, 110, 140, 155, 90, 125],
    'Power': [110, 85, 95, 105, 125, 60, 95],
    'Transit': [95, 120, 105, 110, 100, 55, 80],
}
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.1
bar_positions = np.arange(len(planets))

for i, commodity in enumerate(commodities):
    ax.bar(bar_positions + i * bar_width, trade_volumes[commodity], width=bar_width, color=colors[i], edgecolor='black', label=commodity, alpha=0.85)

for i, planet in enumerate(planets):
    for j, commodity in enumerate(commodities):
        val = trade_volumes[commodity][i]
        if val > 15:
            ax.text(i + j * bar_width, val + 5, f'{val}M', ha='center', va='bottom', color='black', fontsize=9)

ax.set_xticks(bar_positions + bar_width * (len(commodities) - 1) / 2)
ax.set_xticklabels(planets)
ax.set_xlabel("Celestial Bodies", fontsize=12)
ax.set_ylabel("Trade Value (Mega Credits)", fontsize=12)
ax.set_title("Galactic Trade Expo: Item Transactions (Galactic Year 3050)", fontsize=14, fontweight='bold')

ax.set_frame_on(False)
ax.grid(False)
ax.legend(title='Goods')

plt.tight_layout()
plt.show()