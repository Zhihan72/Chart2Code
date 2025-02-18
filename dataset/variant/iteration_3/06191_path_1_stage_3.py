import numpy as np
import matplotlib.pyplot as plt
from math import pi

categories = ['Historical Buildings', 'Modern Skyscrapers', 'Parks and Open Spaces', 'Public Transportation', 'Cultural Venues']
city_scores = {
    'New York': [10, 9, 7, 9, 8],
    'Paris': [8, 8, 9, 10, 7],
    'Tokyo': [7, 9, 8, 7, 10],
    'London': [8, 9, 10, 8, 9],
    'Dubai': [5, 7, 10, 6, 8]
}

global_averages = [8, 8, 9, 8, 9]

num_vars = len(categories)
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# New set of colors
colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00']

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

def add_city_radar(city_name, color):
    scores = city_scores[city_name]
    scores += scores[:1]
    ax.fill(angles, scores, color=color, alpha=0.25, label=city_name)

for city, color in zip(city_scores.keys(), colors):
    add_city_radar(city, color)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, weight='bold')
ax.set_ylim(0, 10)
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=10)

plt.title('Cityscape Attributes Across Global Metropolises', size=15, weight='bold', ha='center', va='top', position=(0.5, 1.1))

global_averages += global_averages[:1]
ax.fill(angles, global_averages, color='grey', alpha=0.1, label='Global Average')

ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.2), fontsize=10, title='Cities')

plt.tight_layout()
plt.show()