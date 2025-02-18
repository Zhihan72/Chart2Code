import matplotlib.pyplot as plt
import numpy as np

categories = ['Renewable Energy', 'Waste Management', 'Public Transport',
              'Green Spaces', 'Air Quality', 'Water Conservation']
num_vars = len(categories)

scores = {
    'Amsterdam': [9, 8, 7, 8, 7, 9],
    'San Francisco': [7, 9, 8, 7, 8, 6],
    'Stockholm': [9, 9, 7, 9, 9, 8],
    'Sydney': [8, 6, 8, 7, 8, 7]
}

for city in scores:
    scores[city] += scores[city][:1]

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, axs = plt.subplots(1, 2, figsize=(18, 9), subplot_kw={'polar': True})

ax = axs[0]
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, color='grey', size=12)
ax.set_rlabel_position(0)
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(["2", "4", "6", "8", "10"], color="grey", size=10)
ax.set_ylim(0, 10)

colors = ['deepskyblue', 'forestgreen', 'mediumorchid', 'crimson']

for i, (city, score) in enumerate(scores.items()):
    ax.plot(angles, score, linewidth=2, linestyle='solid', label=city, color=colors[i])
    ax.fill(angles, score, color=colors[i], alpha=0.1)

ax.set_title("Urban Sustainability Performance 2023\nComparative Analysis of Major Cities", size=14, weight='bold')

ax2 = axs[1]
average_scores = {city: np.mean(scores[city][:-1]) for city in scores}
ax2.bar(average_scores.keys(), average_scores.values(), color=colors)
ax2.set_ylim(0, 10)
ax2.set_title("Average Sustainability Score per City", size=14, weight='bold')
ax2.set_ylabel('Average Score', size=12)
ax2.set_xticklabels(average_scores.keys(), rotation=45, ha='right', fontsize=12)

ax.legend(loc='upper right', bbox_to_anchor=(1.5, 1.1), fontsize=10)

plt.tight_layout()
plt.show()