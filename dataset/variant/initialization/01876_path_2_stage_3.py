import matplotlib.pyplot as plt
import numpy as np

creative_hours = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
happiness_levels = np.array([30, 33, 36, 48, 52, 60, 70, 80, 85, 89, 95])

# Combine creative hours and happiness levels for sorting
data = list(zip(creative_hours, happiness_levels))
# Sort by happiness levels
sorted_data = sorted(data, key=lambda x: x[1], reverse=False)
sorted_creative_hours, sorted_happiness_levels = zip(*sorted_data)

fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(sorted_creative_hours, sorted_happiness_levels, color='teal', alpha=0.8, edgecolor='k')

ax.set_xlim(min(creative_hours) - 1, max(creative_hours) + 1)
ax.set_ylim(20, 100)
ax.set_xticks(sorted_creative_hours)
ax.set_yticks([])

fig.tight_layout()

plt.show()