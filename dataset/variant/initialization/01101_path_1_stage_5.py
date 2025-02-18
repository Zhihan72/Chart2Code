import matplotlib.pyplot as plt
import numpy as np

categories = ['Renewable', 'Waste', 'Transport', 'Spaces', 'Air', 'Water']
num_vars = len(categories)

scores = {
    'AMS': [9, 8, 7, 8, 7, 9],
    'SF': [7, 9, 8, 7, 8, 6],
    'STO': [9, 9, 7, 9, 9, 8],
    'SYD': [8, 6, 8, 7, 8, 7]
}

for city in scores:
    scores[city] += scores[city][:1]

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, axs = plt.subplots(1, 2, figsize=(18, 9), subplot_kw={'polar': True})

ax2 = axs[0]
average_scores = {city: np.mean(scores[city][:-1]) for city in scores}
ax2.bar(average_scores.keys(), average_scores.values(), color='limegreen', edgecolor='darkgreen', linewidth=2)
ax2.set_ylim(0, 10)
ax2.set_title("Avg Score per City", size=14, weight='bold')
ax2.set_ylabel('Avg Score', size=12)
ax2.set_xticklabels(average_scores.keys(), rotation=30, ha='right', fontsize=12)

ax = axs[1]
ax.set_theta_offset(np.pi / 3)
ax.set_theta_direction(1)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, color='gray', size=12, fontstyle='italic')
ax.set_rlabel_position(15)
ax.set_yticks([3, 6, 9])
ax.set_yticklabels(["3", "6", "9"], color="dimgray", size=9)
ax.set_ylim(0, 10)

line_styles = ['dotted', 'dashed', 'dashdot', 'solid']
markers = ['o', 'v', '^', 's']
colors = ['skyblue', 'salmon', 'lightgreen', 'plum']

for i, (city, score) in enumerate(scores.items()):
    ax.plot(angles, score, linewidth=2, linestyle=line_styles[i], label=city, color=colors[i], marker=markers[i], markerfacecolor='black')
    ax.fill(angles, score, color=colors[i], alpha=0.1)

ax.set_title("Urban Sustainability 2023", size=14, weight='bold')
ax.legend(loc='upper left', bbox_to_anchor=(1.2, 1.1), fontsize=9)

axs[0].grid(True, linestyle='--', linewidth=1)
axs[1].grid(True, linestyle='-', linewidth=0.5)

plt.tight_layout()
plt.show()