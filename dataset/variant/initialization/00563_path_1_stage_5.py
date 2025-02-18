import numpy as np
import matplotlib.pyplot as plt
from math import pi

categories = ['Power', 'Velocity', 'Brains', 'Endurance', 'Flexibility']
N = len(categories)

data = {
    'Marvel': [8, 9, 6, 7, 8],
    'DC': [9, 7, 8, 6, 9],
    'Anime': [6, 8, 9, 7, 6],
    'Fantasy': [7, 5, 7, 8, 5],
    'Sci-Fi': [5, 6, 8, 9, 7]
}

angles = np.linspace(0, 2 * pi, N, endpoint=False).tolist()
angles += angles[:1]

category_averages = np.mean(list(data.values()), axis=0)

fig, ax2 = plt.subplots(1, 1, figsize=(8, 8), subplot_kw={'polar': True})

def plot_radar(ax, data, categories, angles, colors):
    for i, (universe, values) in enumerate(data.items()):
        values += values[:1]
        ax.plot(angles, values, color=colors[i], linewidth=2, linestyle='solid')
        ax.fill(angles, values, color=colors[i], alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, color='grey', size=12)
    ax.set_yticklabels(["Low", "Mid", "High", "Top", "Max"], color="grey", size=10)
    ax.set_title('Fictional Hero Analysis', size=15, fontweight='bold', pad=20)
    ax.set_ylim(0, 10)

colors = ['#FFAA33', '#AAFF33', '#33AAFF', '#FFA3FF', '#A3FFAA']

plot_radar(ax2, data, categories, angles, colors)

plt.tight_layout()
plt.show()