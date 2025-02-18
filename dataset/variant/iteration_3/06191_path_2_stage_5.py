import numpy as np
import matplotlib.pyplot as plt
from math import pi

categories = ['Historic Sights', 'Skyscrapers', 'Open Areas', 'Transit Systems', 'Cultural Hubs']
city_scores = {
    'NYC': [8, 9, 10, 7, 9],
    'Parisian': [7, 8, 10, 9, 8],
    'Tokyo': [9, 7, 8, 7, 10],
    'London Town': [8, 9, 10, 8, 9],
    'Dubai City': [10, 5, 7, 6, 8]
}

num_vars = len(categories)
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Single color removed; unique colors for each city
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Updated function to add filled radar chart
def add_city_radar(city_name, color):
    scores = city_scores[city_name]
    scores += scores[:1]
    ax.plot(angles, scores, linewidth=2, linestyle='solid', label=city_name, color=color)
    ax.fill(angles, scores, color=color, alpha=0.25)  # Alpha changed for better visibility

for city, color in zip(city_scores.keys(), colors):
    add_city_radar(city, color)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=15, weight='bold', color='darkred')

ax.set_ylim(0, 10)
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="blue", size=8)

plt.title('Attributes of Global Cities', size=20, weight='heavy', color='purple')

ax.legend(loc='lower left', bbox_to_anchor=(-0.1, -0.1), fontsize=9, title='City Names', title_fontsize='10')

ax.grid(color='gray', linestyle='-', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()