import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

# Scores by subject
math_scores = np.array([70, 72, 75, 78, 80, 83, 85, 88, 90, 93, 95])
science_scores = np.array([65, 68, 70, 73, 76, 79, 81, 85, 87, 90, 93])
english_scores = np.array([60, 63, 67, 70, 73, 76, 79, 82, 84, 87, 89])
history_scores = np.array([50, 52, 55, 58, 62, 65, 68, 70, 73, 75, 78])
art_scores = np.array([55, 57, 59, 61, 64, 67, 70, 73, 76, 79, 82])

scores = np.array([math_scores, science_scores, english_scores, history_scores, art_scores])

fig, ax = plt.subplots(figsize=(12, 7))

ax.stackplot(years, scores, labels=['Math', 'Sci', 'Lang Arts', 'Hist', 'Visual Arts'],
             colors=['#FFB6C1', '#20B2AA', '#FFD700', '#9370DB', '#FF4500'], alpha=0.8)

ax.set_title("Evolution of Scores: Techville Scholars (2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timeline', fontsize=14)
ax.set_ylabel('Performance', fontsize=14)

ax.grid(axis='y', linestyle='--', alpha=0.6)

ax.legend(loc='upper left', title='Disciplines', fontsize=10)

ax.set_xticks(years)
plt.xticks(rotation=45)

plt.tight_layout()

plt.show()