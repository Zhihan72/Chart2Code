import matplotlib.pyplot as plt
import numpy as np

creative_hours = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
happiness_levels = np.array([48, 70, 52, 60, 30, 36, 95, 33, 80, 89, 85])

sorted_indices = np.argsort(happiness_levels)
sorted_creative_hours = creative_hours[sorted_indices]
sorted_happiness_levels = happiness_levels[sorted_indices]

colors = ['skyblue', 'gray', 'lime', 'orange', 'violet', 'pink', 'brown', 'teal', 'gold', 'purple', 'coral']

fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(sorted_creative_hours, sorted_happiness_levels, color=colors, alpha=0.8)

ax.set_xlabel("Creative Hours", fontsize=12)
ax.set_ylabel("Happiness (1-100)", fontsize=12)
ax.set_xticks(np.arange(0, 11, 1))
ax.set_yticks(np.arange(20, 101, 10))
ax.set_xlim(min(creative_hours) - 1, max(creative_hours) + 1)
ax.set_ylim(20, 100)

fig.tight_layout()
plt.show()