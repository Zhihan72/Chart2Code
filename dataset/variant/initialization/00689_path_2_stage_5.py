import numpy as np
import matplotlib.pyplot as plt

original_values = np.array([85, 78, 65, 90, 70, 60])
additional_values = np.array([60, 68, 75, 85, 80, 55])

original_values = np.concatenate((original_values, [original_values[0]]))
additional_values = np.concatenate((additional_values, [additional_values[0]]))

angles = np.linspace(0, 2 * np.pi, len(original_values) - 1, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))

# Fill area for original data series with a different hatch pattern and marker type
ax.plot(angles, original_values, color='orange', marker='o', linestyle='--')
ax.fill(angles, original_values, color='orange', alpha=0.25, hatch='/')

# Fill area for additional data series with a different hatch and thicker line style
ax.plot(angles, additional_values, color='green', marker='s', linestyle='-', linewidth=2)
ax.fill(angles, additional_values, color='green', alpha=0.25, hatch='\\')

# Change grid color and line style, add border to the plot
ax.grid(color='gray', linestyle='-.', linewidth=0.5)
ax.spines['polar'].set_visible(True)
ax.spines['polar'].set_color('black')

# Add a legend
ax.legend(['Original Data', 'Additional Data'], loc='upper right', fontsize='small')

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])  
ax.set_xticklabels(['Metric A', 'Metric B', 'Metric C', 'Metric D', 'Metric E', 'Metric F'])

ax.set_ylim(0, 100)

plt.tight_layout()
plt.show()