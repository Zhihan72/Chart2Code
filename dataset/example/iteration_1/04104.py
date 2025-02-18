import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# In the Kingdom of Wizaria, five different academies of magic are renowned for their unique curriculums.
# Every year, the students undergo various trials and the scores they achieve are noted down.
# We are plotting the distribution of scores for the five academies to understand their performance dynamics. 

# Data representing scores of students from five different magical academies
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

# Setting up the figure
fig, ax = plt.subplots(figsize=(14, 9))
box = ax.boxplot(data, labels=academies, patch_artist=True, notch=True, showmeans=True)

# Apply unique colors to boxes
colors = ['#FFD700', '#FF4500', '#1E90FF', '#32CD32', '#BA55D3']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Customizing the plot for better visualization
plt.setp(box['medians'], color='black', linewidth=1.5)
plt.setp(box['means'], marker='o', color='red', markersize=5)
plt.setp(box['whiskers'], linestyle='--', color='gray')
plt.setp(box['caps'], color='gray')

# Overlay line plot to show average scores
ax.plot(range(1, len(academies) + 1), averages, marker='s', linestyle='-', color='blue', label='Average Score')

# Adding specific data points for outliers
outliers = [
    [score for score in scores if score < np.percentile(scores, 25) - 1.5*(np.percentile(scores, 75) - np.percentile(scores, 25)) 
                     or score > np.percentile(scores, 75) + 1.5*(np.percentile(scores, 75) - np.percentile(scores, 25))]
    for scores in data
]

for idx, academy_outliers in enumerate(outliers):
    ax.scatter([idx + 1] * len(academy_outliers), academy_outliers, color='black', zorder=3)

# Title and labels with backstory theme
ax.set_title('Magical Performance Metrics: Score Distributions\nof Wizarding Academies in Wizaria', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Academy of Magic', fontsize=14)
ax.set_ylabel('Trial Scores', fontsize=14)

# Display legend
ax.legend(loc='upper right', fontsize=12)

# Grid and layout adjustments
ax.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()

# Show plot
plt.show()