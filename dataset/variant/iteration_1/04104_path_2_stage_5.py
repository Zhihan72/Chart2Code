import matplotlib.pyplot as plt
import numpy as np

# Manually altered some scores in the lists
academy_griffin_scores = [62, 60, 75, 72, 71, 70, 67, 78, 80, 85, 82, 87, 93, 90, 97, 95, 100]
academy_phoenix_scores = [52, 50, 65, 62, 57, 60, 55, 68, 70, 78, 75, 80, 85, 87, 82, 90, 93]
academy_dragon_scores = [42, 40, 60, 55, 50, 53, 45, 65, 67, 70, 62, 73, 75, 80, 77, 82, 85]
academy_sphinx_scores = [32, 30, 45, 40, 37, 42, 35, 50, 53, 55, 47, 57, 62, 60, 65, 67, 70]
academy_unicorn_scores = [22, 20, 35, 30, 27, 32, 25, 40, 42, 45, 38, 48, 53, 50, 55, 57, 60]

data = [
    academy_griffin_scores,
    academy_phoenix_scores,
    academy_dragon_scores,
    academy_sphinx_scores,
    academy_unicorn_scores
]

averages = [np.mean(scores) for scores in data]
academies = ['Griffin', 'Phoenix', 'Dragon', 'Sphinx', 'Unicorn']

fig, ax = plt.subplots(figsize=(14, 9))
box = ax.boxplot(data, labels=academies, patch_artist=True, notch=False, showmeans=True, vert=False)

colors = ['#FFD700', '#1E90FF', '#32CD32', '#FF4500', '#BA55D3']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.setp(box['medians'], color='navy', linewidth=2)
plt.setp(box['means'], marker='^', color='orange', markersize=7)
plt.setp(box['whiskers'], linestyle='-', color='gray')
plt.setp(box['caps'], color='purple')

ax.plot(averages, range(1, len(academies) + 1), marker='*', linestyle='--', color='green', label='Avg')

outliers = [
    [score for score in scores if score < np.percentile(scores, 25) - 1.5*(np.percentile(scores, 75) - np.percentile(scores, 25)) 
                     or score > np.percentile(scores, 75) + 1.5*(np.percentile(scores, 75) - np.percentile(scores, 25))]
    for scores in data
]

for idx, academy_outliers in enumerate(outliers):
    ax.scatter(academy_outliers, [idx + 1] * len(academy_outliers), color='red', marker='x', zorder=3)

ax.set_title('Academy Score Distribution', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Scores', fontsize=14, fontweight='light')
ax.set_ylabel('Academy', fontsize=14, fontweight='light')

ax.legend(loc='lower right', fontsize=10, frameon=False)

ax.grid(axis='y', linestyle=':', alpha=0.8)

plt.tight_layout()
plt.show()