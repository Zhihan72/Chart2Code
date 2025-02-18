import matplotlib.pyplot as plt
import numpy as np

# Backstory: "The Great Galactic Interstellar Trade"
# This plot shows the trade volume between different planets for various commodities in the galactic year 3050.

# Data for the plot
planets = ['Earth', 'Mars', 'Venus', 'Jupiter', 'Saturn']
commodities = ['Water', 'Metals', 'Food', 'Technology', 'Energy']

# Trade volumes in million galactic credits
trade_volumes = {
    'Water': [120, 60, 30, 90, 110],
    'Metals': [85, 140, 60, 80, 95],
    'Food': [200, 95, 120, 180, 160],
    'Technology': [150, 130, 110, 140, 155],
    'Energy': [110, 85, 95, 105, 125],
}

# Colors for each commodity
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Set up subplots
fig, ax = plt.subplots(figsize=(12, 8))

# Positions for each planet
bar_positions = np.arange(len(planets))

# Initialize bottom for stacking bars
cumulative_bottom = np.zeros(len(planets))

# Plot each commodity's trade volume
for commodity, color in zip(commodities, colors):
    ax.bar(bar_positions, trade_volumes[commodity], bottom=cumulative_bottom, color=color, edgecolor='black', label=commodity, alpha=0.85)
    # Update cumulative bottom for the next stack
    cumulative_bottom += np.array(trade_volumes[commodity])

# Annotate each segment with its volume value
for i, planet in enumerate(planets):
    cumulative_value = 0
    for commodity in commodities:
        val = trade_volumes[commodity][i]
        if val > 15:  # Annotate only meaningful values to avoid clutter
            ax.text(i, cumulative_value + val/2, f'{val}M', ha='center', va='center', color='white', weight='bold', fontsize=10)
        cumulative_value += val

# Labels and title
ax.set_xticks(bar_positions)
ax.set_xticklabels(planets)
ax.set_xlabel("Planets", fontsize=12)
ax.set_ylabel("Trade Volume (Million Galactic Credits)", fontsize=12)
ax.set_title("The Great Galactic Interstellar Trade: Commodity Exchange (Year 3050)", fontsize=14, fontweight='bold')

# Add a legend
ax.legend(title="Commodities", bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10, title_fontsize='12')

# Improve layout to fit plot within the figure area
plt.tight_layout()

# Show plot
plt.show()