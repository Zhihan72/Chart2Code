import matplotlib.pyplot as plt
import numpy as np

planets = ['Earth', 'Mars', 'Venus', 'Jupiter', 'Saturn']
commodities = ['Water', 'Metals', 'Food', 'Tech', 'Energy']

trade_volumes = {
    'Water': [120, 60, 30, 90, 110],
    'Metals': [85, 140, 60, 80, 95],
    'Food': [200, 95, 120, 180, 160],
    'Tech': [150, 130, 110, 140, 155],
    'Energy': [110, 85, 95, 105, 125],
}

single_color = '#1f77b4'  # Consistent single color for all commodities

fig, ax = plt.subplots(figsize=(12, 8))
bar_positions = np.arange(len(planets))

left_commodities = ['Water', 'Metals']
right_commodities = ['Food', 'Tech', 'Energy']

for commodity in left_commodities:
    ax.bar(bar_positions, -np.array(trade_volumes[commodity]), color=single_color, edgecolor='grey', label=commodity, alpha=0.75)

for commodity in right_commodities:
    ax.bar(bar_positions, trade_volumes[commodity], color=single_color, edgecolor='grey', label=commodity, alpha=0.75)

for i, planet in enumerate(planets):
    cumulative_value_left = 0
    for commodity in left_commodities:
        val = -trade_volumes[commodity][i]
        if abs(val) > 15:
            ax.text(i, cumulative_value_left + val/2, f'{-val}M', ha='center', va='center', color='white', weight='bold', fontsize=10)
        cumulative_value_left += val

    cumulative_value_right = 0
    for commodity in right_commodities:
        val = trade_volumes[commodity][i]
        if val > 15:
            ax.text(i, cumulative_value_right + val/2, f'{val}M', ha='center', va='center', color='white', weight='bold', fontsize=10)
        cumulative_value_right += val

ax.axhline(0, color='black',linewidth=0.8)
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
ax.set_xticks(bar_positions)
ax.set_xticklabels(planets)
ax.set_xlabel("Planets", fontsize=14, fontweight='bold')
ax.set_ylabel("Volume (M Credits)", fontsize=14, fontweight='bold')
ax.set_title("Galactic Trade (3050)", fontsize=16, fontweight='heavy')
ax.legend(title="Items", bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=11, title_fontsize='13', frameon=False)

plt.tight_layout()
plt.show()