import matplotlib.pyplot as plt
import numpy as np

age_groups = ['Children (5-12)', 'Teens (13-19)', 'Adults (20-39)', 'Middle-aged (40-59)']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

step_counts = np.array([
    [12000, 15000, 13000, 14000, 14500, 20000, 18000],
    [10000, 11000, 12000, 11500, 11000, 13500, 12500],
    [8000, 8500, 9000, 9500, 9000, 10000, 9500],
    [7500, 7000, 7200, 7100, 7300, 8000, 7800]
])

fig, ax = plt.subplots(figsize=(14, 8))

index = np.arange(len(days))

# New color set
new_colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1']

# Plot stacked bar chart with new colors
bars = np.zeros(len(days))
for i, group in enumerate(age_groups):
    ax.bar(index, step_counts[i], label=group, bottom=bars, color=new_colors[i])
    bars += step_counts[i]

plt.xticks(index, days)
plt.ylabel('Step count')
plt.legend(title='Age Groups')
plt.grid(True, axis='y', linestyle='--', linewidth=0.5)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()