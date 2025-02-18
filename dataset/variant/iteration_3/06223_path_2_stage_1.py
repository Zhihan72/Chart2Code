import matplotlib.pyplot as plt
import numpy as np

# Data for the plot
planets = ['Earth', 'Mars', 'Venus', 'Jupiter', 'Saturn']
commodities = ['Water', 'Metals', 'Food', 'Tech', 'Energy']

# Trade volumes in million galactic credits
trade_volumes = {
    'Water': [120, 60, 30, 90, 110],
    'Metals': [85, 140, 60, 80, 95],
    'Food': [200, 95, 120, 180, 160],
    'Tech': [150, 130, 110, 140, 155],
    'Energy': [110, 85, 95, 105, 125],
}

# Colors for each commodity
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

fig, ax = plt.subplots(figsize=(12, 8))
bar_positions = np.arange(len(planets))
cumulative_bottom = np.zeros(len(planets))

# Plot each commodity's trade volume
for commodity, color in zip(commodities, colors):
    ax.bar(bar_positions, trade_volumes[commodity], bottom=cumulative_bottom, color=color, edgecolor='black', label=commodity, alpha=0.85)
    cumulative_bottom += np.array(trade_volumes[commodity])

# Annotate each segment
for i, planet in enumerate(planets):
    cumulative_value = 0
    for commodity in commodities:
        val = trade_volumes[commodity][i]
        if val > 15: 
            ax.text(i, cumulative_value + val/2, f'{val}M', ha='center', va='center', color='white', weight='bold', fontsize=10)
        cumulative_value += val

ax.set_xticks(bar_positions)
ax.set_xticklabels(planets)
ax.set_xlabel("Planets", fontsize=12)
ax.set_ylabel("Volume (M Credits)", fontsize=12)
ax.set_title("Galactic Trade (3050)", fontsize=14, fontweight='bold')
ax.legend(title="Items", bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10, title_fontsize='12')

plt.tight_layout()
plt.show()