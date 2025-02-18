import matplotlib.pyplot as plt
import numpy as np

# Define years
years = np.array([2017, 2018, 2019, 2020, 2021])

# Altered activities in the park (Number of participants)
running = np.array([200, 150, 220, 175, 180])
cycling = np.array([130, 100, 140, 120, 110])
picnicking = np.array([90, 80, 100, 85, 95])
swimming = np.array([60, 85, 75, 60, 80])
yoga = np.array([50, 30, 60, 40, 45])

total_participation = running + cycling + picnicking + swimming + yoga

fig, ax1 = plt.subplots(figsize=(12, 7))

activities = [running, cycling, picnicking, swimming, yoga]
colors = ['#2ca02c', '#d62728', '#9467bd', '#1f77b4', '#ff7f0e']
bottom = np.zeros(len(years))

for activity, color in zip(activities, colors):
    ax1.bar(years, activity, bottom=bottom, color=color, alpha=0.85, edgecolor='black')
    bottom += activity

ax2 = ax1.twinx()
ax2.plot(years, total_participation, color='grey', marker='s', linestyle='--', linewidth=2)

ax1.set_xticks(years)
ax1.set_xticklabels([])
ax1.set_yticks([])
ax2.set_yticks([])

plt.tight_layout(rect=[0, 0, 1, 1])

plt.show()