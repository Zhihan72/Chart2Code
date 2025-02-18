import matplotlib.pyplot as plt
import numpy as np

academy_mermaid_scores = [65, 67, 70, 72, 73, 75, 78, 80, 83, 85, 87, 90, 92, 95, 97, 98, 100]
academy_centaurs_scores = [35, 37, 40, 42, 45, 47, 50, 52, 55, 57, 60, 63, 65, 67, 70, 72, 75]

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
    academy_unicorn_scores,
    academy_mermaid_scores,
    academy_centaurs_scores
]

averages = [np.mean(scores) for scores in data]
academies = ['Griffin', 'Phoenix', 'Dragon', 'Sphinx', 'Unicorn', 'Mermaid', 'Centaurs']

fig, ax = plt.subplots(figsize=(14, 9))

box = ax.boxplot(data, labels=academies, patch_artist=True, notch=True, showmeans=True, vert=False)

colors = ['#FFD700', '#FF4500', '#1E90FF', '#32CD32', '#BA55D3', '#FF69B4', '#8B4513']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.setp(box['medians'], color='black', linewidth=1.5)
plt.setp(box['means'], marker='o', color='red', markersize=5)
plt.setp(box['whiskers'], linestyle='--', color='gray')
plt.setp(box['caps'], color='gray')

ax.plot(averages, range(1, len(academies) + 1), marker='s', linestyle='-', color='blue')

outliers = [
    [score for score in scores if score < np.percentile(scores, 25) - 1.5*(np.percentile(scores, 75) - np.percentile(scores, 25))
                     or score > np.percentile(scores, 75) + 1.5*(np.percentile(scores, 75) - np.percentile(scores, 25))]
    for scores in data
]

for idx, academy_outliers in enumerate(outliers):
    ax.scatter(academy_outliers, [idx + 1] * len(academy_outliers), color='black', zorder=3)

ax.set_title('Magical Performance Metrics: Score Distributions\nof Wizarding Academies in Wizaria', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Academy of Magic', fontsize=14)
ax.set_xlabel('Trial Scores', fontsize=14)

plt.tight_layout()

plt.show()