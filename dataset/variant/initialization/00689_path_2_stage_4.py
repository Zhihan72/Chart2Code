import numpy as np
import matplotlib.pyplot as plt

# Fill-area radar chart data
original_values = np.array([85, 78, 65, 90, 70, 60])
additional_values = np.array([60, 68, 75, 85, 80, 55])

# Complete the circle by repeating the first value
original_values = np.concatenate((original_values, [original_values[0]]))
additional_values = np.concatenate((additional_values, [additional_values[0]]))

# Calculate angles for radar chart
angles = np.linspace(0, 2 * np.pi, len(original_values) - 1, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Fill area for original data series
ax.fill(angles, original_values, color='orange', alpha=0.4)

# Fill area for additional data series
ax.fill(angles, additional_values, color='blue', alpha=0.4)

# Additional configuration
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])  # Use the original angle count for labels
ax.set_xticklabels(['Metric 1', 'Metric 2', 'Metric 3', 'Metric 4', 'Metric 5', 'Metric 6'])

ax.set_ylim(0, 100)

plt.tight_layout()
plt.show()