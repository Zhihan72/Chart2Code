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

bar_width = 0.15
index = np.arange(len(days))

bars = []
for i, group in enumerate(age_groups):
    bar = ax.bar(index + i * bar_width, step_counts[i], bar_width)
    bars.append(bar)

plt.xticks([])  
plt.yticks([])

plt.grid(True, which='both', linestyle='--', linewidth=0.5)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

for bar_group in bars:
    for bar in bar_group:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, f'{int(height)}',
                ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()