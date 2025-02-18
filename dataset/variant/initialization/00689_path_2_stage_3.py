import numpy as np
import matplotlib.pyplot as plt

# Original data series
original_values = np.array([85, 78, 65, 90, 70, 60])
additional_values = np.array([60, 68, 75, 85, 80, 55])

# Complete the circle for the radar chart by repeating the first value
original_values = np.concatenate((original_values, [original_values[0]]))
additional_values = np.concatenate((additional_values, [additional_values[0]]))

# Creating angles for the radar chart
angles = np.linspace(0, 2 * np.pi, len(original_values) - 1, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot original data series
ax.fill(angles, original_values, color='orange', alpha=0.4)
ax.plot(angles, original_values, color='orange', linewidth=2)

# Plot additional data series
ax.fill(angles, additional_values, color='blue', alpha=0.4)
ax.plot(angles, additional_values, color='blue', linewidth=2)

ax.set_yticklabels([])
ax.set_xticks(angles)
ax.set_xticklabels([])

ax.set_ylim(0, 100)

plt.tight_layout()
plt.show()