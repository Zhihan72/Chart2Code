import matplotlib.pyplot as plt
import numpy as np

academy_griffin_scores = [60, 62, 67, 70, 71, 72, 75, 78, 80, 82, 85, 87, 90, 93, 95, 97, 100]
academy_phoenix_scores = [50, 52, 55, 57, 60, 62, 65, 68, 70, 75, 78, 80, 82, 85, 87, 90, 93]
academy_dragon_scores = [40, 42, 45, 50, 53, 55, 60, 62, 65, 67, 70, 73, 75, 77, 80, 82, 85]
academy_sphinx_scores = [30, 32, 35, 37, 40, 42, 45, 47, 50, 53, 55, 57, 60, 62, 65, 67, 70]
academy_unicorn_scores = [20, 22, 25, 27, 30, 32, 35, 38, 40, 42, 45, 48, 50, 53, 55, 57, 60]

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
box = ax.boxplot(data, labels=academies, patch_artist=True, notch=False, showmeans=True)

colors = ['#FFD700', '#1E90FF', '#32CD32', '#FF4500', '#BA55D3']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.setp(box['medians'], color='navy', linewidth=2)
plt.setp(box['means'], marker='^', color='orange', markersize=7)
plt.setp(box['whiskers'], linestyle='-', color='gray')
plt.setp(box['caps'], color='purple')

ax.plot(range(1, len(academies) + 1), averages, marker='*', linestyle='--', color='green', label='Avg')

outliers = [
    [score for score in scores if score < np.percentile(scores, 25) - 1.5*(np.percentile(scores, 75) - np.percentile(scores, 25)) 
                     or score > np.percentile(scores, 75) + 1.5*(np.percentile(scores, 75) - np.percentile(scores, 25))]
    for scores in data
]

for idx, academy_outliers in enumerate(outliers):
    ax.scatter([idx + 1] * len(academy_outliers), academy_outliers, color='red', marker='x', zorder=3)

ax.set_title('Academy Score Dist.', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Academy', fontsize=14, fontweight='light')
ax.set_ylabel('Scores', fontsize=14, fontweight='light')

ax.legend(loc='lower left', fontsize=10, frameon=False)

ax.grid(axis='x', linestyle=':', alpha=0.8)

plt.tight_layout()
plt.show()