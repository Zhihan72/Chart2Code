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

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

def add_city_radar(city_name, color):
    scores = city_scores[city_name]
    scores += scores[:1]
    ax.plot(angles, scores, linewidth=2, linestyle='solid', label=city_name, color=color)
    ax.fill(angles, scores, color=color, alpha=0.25)

for city, color in zip(city_scores.keys(), colors):
    add_city_radar(city, color)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, weight='bold')

ax.set_ylim(0, 10)
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=10)

plt.title('Attributes of Global Cities', size=15, weight='bold', ha='center', va='top', position=(0.5, 1.1))

global_averages += global_averages[:1]
ax.plot(angles, global_averages, linewidth=2, linestyle='dashed', color='grey', label='Avg Worldwide')

ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.2), fontsize=10, title='City Names')

plt.tight_layout()
plt.show()