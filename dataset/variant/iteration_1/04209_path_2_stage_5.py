import numpy as np
import matplotlib.pyplot as plt
from math import pi

categories = ['Vit', 'Min', 'Prot', 'Fib', 'Sug', 'Cal']
num_vars = len(categories)

# Added additional made-up data series for new fruits
fruit_scores = {
    'Appl': [7, 6, 2, 3, 5, 4],
    'Orng': [8, 5, 2, 3, 6, 3],
    'Bnna': [6, 7, 3, 2, 4, 5],
    'Strw': [9, 6, 2, 3, 4, 2],
    'Pnp': [7, 5, 2, 3, 6, 4],
    'Kiwi': [8, 4, 5, 3, 2, 6],  # New fruit data
    'Grapes': [6, 3, 2, 5, 8, 2]  # New fruit data
}

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

colors = ['#32CD32', '#FF1493', '#FF6347', '#FFA500', '#FFD700', '#4682B4', '#9400D3']
line_styles = ['-', '--', '-.', ':', '-', '--', '-.']
markers = ['o', 's', 'D', '^', '*', 'P', 'X']

for idx, (fruit, scores) in enumerate(fruit_scores.items()):
    scores += scores[:1]  # Closing the loop for radar chart
    ax.plot(angles, scores, color=colors[idx], linestyle=line_styles[idx], marker=markers[idx], label=fruit)
    ax.fill(angles, scores, alpha=0.1, color=colors[idx])

plt.xticks(angles[:-1], categories, color='navy', size=14, weight='bold')
ax.set_rlabel_position(45)
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="darkgrey", size=12)
plt.ylim(0, 10)

plt.legend(loc='lower left', bbox_to_anchor=(-0.1, -0.1), fontsize=10, title="Fruits")
ax.grid(color='grey', linestyle=':', linewidth=0.5)
plt.title('Fruit Nutrition', size=22, color='darkgreen', ha='center', fontweight='semibold')

plt.tight_layout()
plt.show()