import matplotlib.pyplot as plt
import numpy as np

creative_hours = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
happiness_levels = np.array([30, 33, 36, 48, 52, 60, 70, 80, 85, 89, 95])
productivity_levels = np.array([25, 28, 34, 40, 50, 65, 75, 82, 88, 90, 92])

data = list(zip(creative_hours, happiness_levels, productivity_levels))
sorted_data = sorted(data, key=lambda x: x[1], reverse=False)
sorted_creative_hours, sorted_happiness_levels, sorted_productivity_levels = zip(*sorted_data)

fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.4

# Shuffle colors by swapping them
ax.bar(np.array(sorted_creative_hours) - bar_width/2, sorted_happiness_levels, bar_width,
       color='orange', alpha=0.8, edgecolor='k', label='Happiness Levels')

ax.bar(np.array(sorted_creative_hours) + bar_width/2, sorted_productivity_levels, bar_width,
       color='teal', alpha=0.8, edgecolor='k', label='Productivity Levels')

ax.set_xlim(min(creative_hours) - 1, max(creative_hours) + 1)
ax.set_ylim(20, 100)
ax.set_xticks(sorted_creative_hours)
ax.set_yticks([])

ax.legend()
fig.tight_layout()

plt.show()