import matplotlib.pyplot as plt
import numpy as np

years = np.array([2017, 2018, 2019, 2020, 2021])

positive_activities = [np.array([200, 150, 220, 175, 180]),
                       np.array([130, 100, 140, 120, 110])]
negative_activities = [np.array([90, 80, 100, 85, 95]),
                       np.array([60, 85, 75, 60, 80]),
                       np.array([50, 30, 60, 40, 45])]

# Use a single color for all activities
single_color = '#1f77b4'

fig, ax = plt.subplots(figsize=(12, 7))

bottom_positive = np.zeros(len(years))
bottom_negative = np.zeros(len(years))

for activity in positive_activities:
    ax.bar(years, activity, bottom=bottom_positive, color=single_color, alpha=0.85, edgecolor='black', width=0.4)
    bottom_positive += activity

for activity in negative_activities:
    ax.bar(years, -activity, bottom=bottom_negative, color=single_color, alpha=0.85, edgecolor='black', width=0.4)
    bottom_negative -= activity

ax.axhline(0, color='black', linewidth=0.8)
ax.set_xticks(years)
ax.set_yticks([])

plt.tight_layout()
plt.show()