import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
math_scores = np.array([70, 72, 75, 78, 80, 83, 85, 88, 90, 93, 95])
science_scores = np.array([65, 68, 70, 73, 76, 79, 81, 85, 87, 90, 93])
english_scores = np.array([60, 63, 67, 70, 73, 76, 79, 82, 84, 87, 89])
history_scores = np.array([50, 55, 60, 62, 65, 68, 70, 72, 75, 78, 80])

scores = np.array([math_scores, science_scores, english_scores, history_scores])

fig, ax = plt.subplots(figsize=(12, 7))

ax.stackplot(years, scores, labels=['Mathematics', 'Science', 'English', 'History'],
             colors=['#FF9999', '#66B2FF', '#99FF99', '#FFD700'], alpha=0.7)

ax.set_title("Techville Student Performance Evolution (2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Scores', fontsize=14)

ax.grid(axis='x', linestyle='-.', linewidth=0.7, alpha=0.8)

ax.legend(loc='lower right', title='Subjects', fontsize=10)

ax.set_xticks(years)
plt.xticks(rotation=30)

plt.tight_layout()

plt.show()