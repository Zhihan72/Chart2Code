import matplotlib.pyplot as plt
import numpy as np

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

chrome_usage = [120, 130, 115, 125, 140, 180, 160]
firefox_usage = [60, 55, 70, 65, 50, 90, 85]

browser_data = [chrome_usage, firefox_usage]
new_color_list = ['#1f77b4', '#ff7f0e']  # Removing Safari color

fig, axes = plt.subplots(1, 2, figsize=(10, 5))  # Adjust number of subplots

titles = ["Firefox Fun", "Chromatic Days"]  # Update titles accordingly

for i, ax in enumerate(axes):
    ax.bar(range(len(days)), browser_data[i], color=new_color_list[i], edgecolor='black', alpha=0.7)
    ax.set_title(titles[i], fontsize=14, weight='bold')
    ax.set_ylabel("Time Utilized", fontsize=12)
    ax.set_xlabel("Weekdays", fontsize=12)
    ax.set_xticks(range(len(days)))
    ax.set_xticklabels(days, rotation=45, ha='right', fontsize=10)
    ax.grid(True, axis='y', linestyle='--', alpha=0.7)

fig.suptitle('Tech Household Browser Trends\nWeekly Exploration on Different Platforms', fontsize=16, fontweight='bold', y=0.98)

fig.tight_layout(rect=[0, 0, 1, 0.96])

plt.show()