import matplotlib.pyplot as plt
import numpy as np

# Data for the plot
planets = ['Earth', 'Mars', 'Venus', 'Jupiter', 'Saturn', 'Neptune', 'Pluto']
commodities = ['Water', 'Metals', 'Food', 'Technology', 'Energy', 'Transport']
trade_volumes = {
    'Water': [120, 60, 30, 90, 110, 50, 70],
    'Metals': [85, 140, 60, 80, 95, 40, 65],
    'Food': [200, 95, 120, 180, 160, 85, 100],
    'Technology': [150, 130, 110, 140, 155, 90, 125],
    'Energy': [110, 85, 95, 105, 125, 60, 95],
    'Transport': [95, 120, 105, 110, 100, 55, 80],
}
single_color = '#1f77b4'

fig, ax = plt.subplots(figsize=(14, 8))

bar_positions = np.arange(len(planets))
cumulative_bottom = np.zeros(len(planets))

for commodity in commodities:
    ax.bar(bar_positions, trade_volumes[commodity], bottom=cumulative_bottom, color=single_color, edgecolor='black', alpha=0.85)
    cumulative_bottom += np.array(trade_volumes[commodity])

for i, planet in enumerate(planets):
    cumulative_value = 0
    for commodity in commodities:
        val = trade_volumes[commodity][i]
        if val > 15:
            ax.text(i, cumulative_value + val / 2, f'{val}M', ha='center', va='center', color='white', weight='bold', fontsize=10)
        cumulative_value += val

ax.set_xticks(bar_positions)
ax.set_xticklabels(planets)
ax.set_xlabel("Planets", fontsize=12)
ax.set_ylabel("Trade Volume (Million Galactic Credits)", fontsize=12)
ax.set_title("The Great Galactic Interstellar Trade: Commodity Exchange (Year 3050)", fontsize=14, fontweight='bold')

ax.set_frame_on(False)
ax.grid(False)

plt.tight_layout()
plt.show()