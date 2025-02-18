import matplotlib.pyplot as plt
import numpy as np

years = np.array([2017, 2018, 2019, 2020, 2021])

# Separate activities into two groups for diverging effect
recreational = np.array([60, 75, 80, 60, 85])  # Swimming - expand upwards
meditation = np.array([30, 40, 50, 45, 60])    # Yoga - expand upwards
hiking = np.array([70, 90, 100, 110, 130])     # Hiking - expand upwards

active = np.array([150, 175, 200, 180, 220])   # Running - expand downwards
biking = np.array([100, 120, 130, 110, 140])   # Cycling - expand downwards
leisure = np.array([80, 85, 95, 90, 100])      # Picnicking - expand downwards
surfing = np.array([40, 55, 60, 65, 70])       # Surfing - expand downwards

fig, ax = plt.subplots(figsize=(12, 7))

# Plot upward expanding bars
top_bottom = np.zeros(len(years))
for activity, color in zip([recreational, meditation, hiking], ['#1f77b4', '#9467bd', '#8c564b']):
    ax.bar(years, activity, bottom=top_bottom, label=activity, color=color, alpha=0.7, edgecolor='black', hatch='/')
    top_bottom += activity

# Plot downward expanding bars as negative values
bottom_top = np.zeros(len(years))
for activity, color in zip([active, biking, leisure, surfing], ['#d62728', '#2ca02c', '#ff7f0e', '#e377c2']):
    ax.bar(years, -activity, bottom=bottom_top, label=activity, color=color, alpha=0.7, edgecolor='black', hatch='/')
    bottom_top -= activity

ax.set_title("Diverging Outdoor Activity Participation\n(2017-2021)", fontsize=18, weight='bold', pad=20)
ax.set_xlabel('Calendar Year', fontsize=14)
ax.set_ylabel('Participant Change', fontsize=14)
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
ax.grid(axis='y', linestyle=':', alpha=0.4)

ax.legend(loc='upper left', fontsize=11, bbox_to_anchor=(1, 1.05), shadow=True)

plt.tight_layout(rect=[0, 0, 0.9, 1])

plt.show()