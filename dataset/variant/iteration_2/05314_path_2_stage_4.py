import numpy as np
import matplotlib.pyplot as plt

working_hours = {
    "SWE": [40, 42, 38, 45, 50, 35, 40, 38, 42, 48, 44, 46, 37, 39, 41, 43],
    "Docs": [50, 55, 60, 52, 58, 62, 48, 54, 57, 63, 56, 59, 53, 51, 49, 47],
    "Tchrs": [30, 32, 29, 35, 34, 37, 33, 28, 31, 36, 32, 30, 29, 33, 34, 35],
    "Law": [45, 48, 52, 55, 50, 46, 49, 53, 47, 51, 54, 48, 50, 52, 47, 49],
    "Arts": [25, 28, 30, 32, 29, 27, 26, 31, 33, 28, 30, 25, 27, 29, 24, 32],
    "Marketing": [35, 38, 40, 42, 39, 36, 33, 37, 41, 34, 39, 38, 42, 36, 37, 34],
    "Finance": [45, 47, 50, 53, 49, 46, 48, 52, 50, 51, 50, 49, 48, 47, 46, 45]
}

professions = list(working_hours.keys())
data = list(working_hours.values())

fig, axes = plt.subplots(1, 2, figsize=(16, 8))

axes[0].boxplot(
    data, vert=True, patch_artist=True, labels=professions, notch=False,
    boxprops=dict(facecolor='#efefef', color='black'),
    whiskerprops=dict(color='black'),
    capprops=dict(color='black'),
    flierprops=dict(marker='o', markerfacecolor='red', markersize=8, linestyle='none'),
    medianprops=dict(color='darkred', linewidth=2)
)

new_colors = ['#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#ff7f0e', '#1f77b4']
for patch, color in zip(axes[0].artists, new_colors):
    patch.set_facecolor(color)

axes[0].set_title("Weekly Hours Distribution", fontsize=14, weight='bold')
axes[0].set_xlabel("Jobs", fontsize=12)
axes[0].set_ylabel("Hours", fontsize=12)
axes[0].grid(axis='y', linestyle='--', alpha=0.7)

average_satisfaction = {
    "SWE": 75,
    "Docs": 80,
    "Tchrs": 85,
    "Law": 65,
    "Arts": 90,
    "Marketing": 70,
    "Finance": 72
}

satisfaction_scores = [average_satisfaction[profession] for profession in professions]

axes[1].scatter(professions, satisfaction_scores, color=new_colors, s=150, edgecolors='white', linewidth=2)
axes[1].set_title("Avg Satisfaction Scores", fontsize=14, weight='bold')
axes[1].set_xlabel("Jobs", fontsize=12)
axes[1].set_ylabel("Avg Score", fontsize=12)
axes[1].set_ylim(60, 95)

for i, txt in enumerate(satisfaction_scores):
    axes[1].annotate(txt, (professions[i], satisfaction_scores[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=10)

fig.suptitle("Work-Life Balance by Profession", fontsize=16, weight='bold')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()