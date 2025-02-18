import matplotlib.pyplot as plt
import numpy as np

# Define years
years = np.array([2017, 2018, 2019, 2020, 2021])

# Activities in the park (Number of participants), split into positive and negative for divergence
positive_activities = [np.array([200, 150, 220, 175, 180]),  # Running
                       np.array([130, 100, 140, 120, 110])]  # Cycling
negative_activities = [np.array([90, 80, 100, 85, 95]),   # Picnicking
                       np.array([60, 85, 75, 60, 80]),    # Swimming
                       np.array([50, 30, 60, 40, 45])]   # Yoga

colors_positive = ['#2ca02c', '#d62728']
colors_negative = ['#9467bd', '#1f77b4', '#ff7f0e']

fig, ax = plt.subplots(figsize=(12, 7))

bottom_positive = np.zeros(len(years))
bottom_negative = np.zeros(len(years))

for activity, color in zip(positive_activities, colors_positive):
    ax.bar(years, activity, bottom=bottom_positive, color=color, alpha=0.85, edgecolor='black', width=0.4)
    bottom_positive += activity

for activity, color in zip(negative_activities, colors_negative):
    ax.bar(years, -activity, bottom=bottom_negative, color=color, alpha=0.85, edgecolor='black', width=0.4)
    bottom_negative -= activity

# Setting zero line
ax.axhline(0, color='black', linewidth=0.8)

ax.set_xticks(years)
ax.set_yticks([])

plt.tight_layout()
plt.show()