import numpy as np
import matplotlib.pyplot as plt
from math import pi

categories = ['Historic Sights', 'Skyscrapers', 'Open Areas', 'Transit Systems', 'Cultural Hubs']
city_scores = {
    'NYC': [9, 10, 8, 9, 7],
    'Parisian': [10, 7, 8, 8, 9],
    'Tokyo': [8, 9, 7, 10, 7],
    'London Town': [9, 8, 9, 8, 10],
    'Dubai City': [6, 10, 7, 8, 5]
}

global_averages = [8, 9, 8, 9, 8]

num_vars = len(categories)
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Updated colors and markers for variation and style diversity
colors = ['#d62728', '#1f77b4', '#2ca02c', '#ff7f0e', '#9467bd']
markers = ['o', '^', 's', 'D', 'v']

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

def add_city_radar(city_name, color, marker):
    scores = city_scores[city_name]
    scores += scores[:1]
    ax.plot(angles, scores, linewidth=2, linestyle='dashdot', marker=marker, label=city_name, color=color)
    ax.fill(angles, scores, color=color, alpha=0.1)

for city, color, marker in zip(city_scores.keys(), colors, markers):
    add_city_radar(city, color, marker)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=15, weight='bold', color='darkred')

ax.set_ylim(0, 10)
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="blue", size=8)

plt.title('Attributes of Global Cities', size=20, weight='heavy', color='purple')

global_averages += global_averages[:1]
ax.plot(angles, global_averages, linewidth=2, linestyle='dotted', color='black', marker='x', label='Avg Worldwide')

# Legend and grid adjustments for added randomness and functionality
ax.legend(loc='lower left', bbox_to_anchor=(-0.1, -0.1), fontsize=9, title='City Names', title_fontsize='10')

ax.grid(color='gray', linestyle='-', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()