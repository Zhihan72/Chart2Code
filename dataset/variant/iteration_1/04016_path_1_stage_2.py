import matplotlib.pyplot as plt
import numpy as np

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

chrome_usage = [120, 130, 115, 125, 140, 180, 160]
firefox_usage = [60, 55, 70, 65, 50, 90, 85]
safari_usage = [30, 25, 20, 35, 40, 50, 45]
edge_usage = [20, 15, 10, 25, 30, 35, 20]

browser_data = [chrome_usage, firefox_usage, safari_usage, edge_usage]
color_list = ['#FF5733', '#FFC300', '#DAF7A6', '#C70039']

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

titles = ["Firefox Fun", "Explore with Safari", "Experience Edge", "Chromatic Days"]  # Randomly reordered and altered titles

for i, ax in enumerate(axes):
    ax.bar(range(len(days)), browser_data[i], color=color_list[i], edgecolor='black', alpha=0.7)
    ax.set_title(titles[i], fontsize=14, weight='bold')
    ax.set_ylabel("Time Utilized", fontsize=12)  # Altered text
    ax.set_xlabel("Weekdays", fontsize=12)  # Altered text
    ax.set_xticks(range(len(days)))
    ax.set_xticklabels(days, rotation=45, ha='right', fontsize=10)
    ax.grid(True, axis='y', linestyle='--', alpha=0.7)

fig.suptitle('Tech Household Browser Trends\nWeekly Exploration on Different Platforms', fontsize=16, fontweight='bold', y=0.98)

fig.tight_layout(rect=[0, 0, 1, 0.96])

plt.show()