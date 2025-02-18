import numpy as np
import matplotlib.pyplot as plt

# Backstory: To understand the work-life balance of different professions, we analyze various metrics. 
# This chart specifically illustrates the distribution of weekly working hours across several professions
# and correlates it with their average job satisfaction scores.

# Data: Weekly working hours for different professions
working_hours = {
    "Software Engineers": [40, 42, 38, 45, 50, 35, 40, 38, 42, 48, 44, 46, 37, 39, 41, 43],
    "Doctors": [50, 55, 60, 52, 58, 62, 48, 54, 57, 63, 56, 59, 53, 51, 49, 47],
    "Teachers": [30, 32, 29, 35, 34, 37, 33, 28, 31, 36, 32, 30, 29, 33, 34, 35],
    "Lawyers": [45, 48, 52, 55, 50, 46, 49, 53, 47, 51, 54, 48, 50, 52, 47, 49],
    "Artists": [25, 28, 30, 32, 29, 27, 26, 31, 33, 28, 30, 25, 27, 29, 24, 32]
}

# Related data: Average job satisfaction scores for the same professions
average_satisfaction = {
    "Software Engineers": 75,
    "Doctors": 80,
    "Teachers": 85,
    "Lawyers": 65,
    "Artists": 90
}

professions = list(working_hours.keys())
data = list(working_hours.values())
satisfaction_scores = [average_satisfaction[profession] for profession in professions]

fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# Plot 1: Horizontal box plot for working hours
axes[0].boxplot(data, vert=False, patch_artist=True, labels=professions, notch=True,
                boxprops=dict(facecolor='#efefef', color='black'),
                whiskerprops=dict(color='black'),
                capprops=dict(color='black'),
                flierprops=dict(marker='o', markerfacecolor='red', markersize=8, linestyle='none'),
                medianprops=dict(color='darkred', linewidth=2))

colors = ['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99']
for patch, color in zip(axes[0].artists, colors):
    patch.set_facecolor(color)

axes[0].set_title("Distribution of Weekly Working Hours\nAcross Various Professions", fontsize=14, weight='bold')
axes[0].set_xlabel("Weekly Working Hours", fontsize=12)
axes[0].set_ylabel("Professions", fontsize=12)
axes[0].grid(axis='x', linestyle='--', alpha=0.7)

# Plot 2: Scatter plot for average job satisfaction scores
axes[1].scatter(professions, satisfaction_scores, color=colors, s=150, edgecolors='white', linewidth=2)
axes[1].set_title("Average Job Satisfaction Scores by Profession", fontsize=14, weight='bold')
axes[1].set_xlabel("Professions", fontsize=12)
axes[1].set_ylabel("Average Job Satisfaction Score", fontsize=12)
axes[1].set_ylim(60, 95)

for i, txt in enumerate(satisfaction_scores):
    axes[1].annotate(txt, (professions[i], satisfaction_scores[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=10)

fig.suptitle("Work-Life Balance Analysis of Different Professions", fontsize=16, weight='bold')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()