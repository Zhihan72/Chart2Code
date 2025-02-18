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
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Initialize the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Define bar width and the initial positions
bar_width = 0.1
bar_positions = np.arange(len(planets))

# Create grouped bar chart
for i, commodity in enumerate(commodities):
    ax.bar(bar_positions + i * bar_width, trade_volumes[commodity], width=bar_width, color=colors[i], edgecolor='black', label=commodity, alpha=0.85)

# Add labels above the bars
for i, planet in enumerate(planets):
    for j, commodity in enumerate(commodities):
        val = trade_volumes[commodity][i]
        if val > 15:
            ax.text(i + j * bar_width, val + 5, f'{val}M', ha='center', va='bottom', color='black', fontsize=9)

# Set axis labels and title
ax.set_xticks(bar_positions + bar_width * (len(commodities) - 1) / 2)
ax.set_xticklabels(planets)
ax.set_xlabel("Planets", fontsize=12)
ax.set_ylabel("Trade Volume (Million Galactic Credits)", fontsize=12)
ax.set_title("The Great Galactic Interstellar Trade: Commodity Exchange (Year 3050)", fontsize=14, fontweight='bold')

ax.set_frame_on(False)
ax.grid(False)
ax.legend(title='Commodities')

plt.tight_layout()
plt.show()