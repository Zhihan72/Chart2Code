import matplotlib.pyplot as plt
import numpy as np

categories = ['Renewable Energy', 'Waste Management', 'Public Transport',
              'Green Spaces', 'Air Quality', 'Water Conservation']
num_vars = len(categories)

scores = {
    'Amsterdam': [9, 8, 7, 8, 7, 9],
    'San Francisco': [7, 9, 8, 7, 8, 6],
    'Singapore': [8, 7, 9, 6, 9, 8],
    'Stockholm': [9, 9, 7, 9, 9, 8],
    'Sydney': [8, 6, 8, 7, 8, 7],
    'EcoCity': [7, 8, 9, 8, 7, 9]  # New made-up data series
}

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(9, 9), subplot_kw={'polar': True})

ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, size=12)

ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(["2", "4", "6", "8", "10"], size=10)
ax.set_ylim(0, 10)
ax.spines['polar'].set_visible(False)

colors = ['cornflowerblue', 'seagreen', 'coral', 'mediumslateblue', 'tomato', 'goldenrod']

for i, (city, score) in enumerate(scores.items()):
    score += score[:1]
    ax.plot(angles, score, linewidth=2, linestyle='solid', color=colors[i])
    ax.fill(angles, score, color=colors[i], alpha=0.25)

ax.set_title("Urban Sustainability Performance 2023\nComparative Analysis of Major Cities", size=14, weight='bold')

plt.tight_layout()
plt.show()