import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2023, 2029)
math_engagement = np.array([70, 72, 75, 78, 80, 82])
science_engagement = np.array([65, 67, 70, 73, 75, 78])
history_engagement = np.array([60, 62, 65, 68, 70, 73])

fig, ax = plt.subplots(figsize=(12, 6))

# Changed color for the Mathematics plot
ax.plot(years, math_engagement, marker='o', linestyle='-', color='#e41a1c', label='Mathematics')
# Changed color for the Science plot
ax.plot(years, science_engagement, marker='s', linestyle='--', color='#377eb8', label='Sci.')
# Changed color for the History plot
ax.plot(years, history_engagement, marker='d', linestyle=':', color='#4daf4a', label='Hist.')

ax.set_title("Student Interaction Tracking (2023-2028)\nAssessing Online Class Subjects", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Timeline (Year)", fontsize=14)
ax.set_ylabel("Engagement Rate (%)", fontsize=14)

ax.legend(title="Disciplines", loc='lower right', fontsize=12)

ax.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()