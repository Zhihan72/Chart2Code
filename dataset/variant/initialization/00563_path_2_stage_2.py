import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define skill categories
categories = ['Agility', 'Intelligence', 'Speed', 'Strength', 'Stamina']
N = len(categories)

# Superhero skill data for each universe
data = {
    'Sci-Fi': [5, 6, 8, 9, 7],
    'Fantasy': [7, 5, 7, 8, 5],
    'Anime': [6, 8, 9, 7, 6],
    'DC': [9, 7, 8, 6, 9],
    'Marvel': [8, 9, 6, 7, 8]
}

# Calculate angle for each axis
angles = np.linspace(0, 2 * pi, N, endpoint=False).tolist()
angles += angles[:1]

# Initialize single subplot for radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'polar': True})

# Radar Chart
def plot_radar(ax, data, categories, angles, colors):
    for i, (universe, values) in enumerate(data.items()):
        values += values[:1]
        ax.plot(angles, values, color=colors[i], linewidth=2, linestyle='solid', label=universe)
        ax.fill(angles, values, color=colors[i], alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, color='grey', size=12)
    ax.set_yticks([2, 4, 6, 8, 10])
    ax.set_yticklabels(["2", "4", "6", "8", "10"], color="grey", size=10)
    ax.set_title('Analysis of Heroic Skills', size=15, fontweight='bold', pad=20)
    ax.set_ylim(0, 10)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)

# Define colors for radar chart universes
colors = ['#33FFF5', '#F033FF', '#3357FF', '#33FF57', '#FF5733']

# Plot radar chart
plot_radar(ax, data, categories, angles, colors)

# Show plot
plt.show()