import matplotlib.pyplot as plt
import numpy as np

age_groups = ['30s', '50+', '20s', '40s']
hobbies = ['Cooking', 'Gardening', 'Exercising', 'Gaming', 'Reading']

data = {
    '30s':         [35, 35, 20, 35, 10],  # updated for shuffling
    '50+':         [30, 25, 30, 20, 20],
    '20s':         [15, 30, 25, 30, 25],
    '40s':         [45, 20, 20, 12, 15],
}

fig, ax = plt.subplots(figsize=(14, 8))
indices = np.arange(len(hobbies))
bottom_values = np.zeros(len(hobbies))
colors = ['#99FF99', '#66B3FF', '#FF6666', '#FFCC99']

marker_types = ['o', 'v', '^', '<', '>']
line_styles = ['-', '--', '-.', ':']

for i, age_group in enumerate(age_groups):
    ax.bar(indices, data[age_group], label=age_group, bottom=bottom_values, color=colors[i], edgecolor='black', hatch=marker_types[i % len(marker_types)])
    bottom_values += np.array(data[age_group])

ax.set_xlabel('Leisure Activities', fontsize=14)
ax.set_ylabel('Hours Allocated', fontsize=14)
ax.set_title('Analysis of Time Spent on Hobbies\nby Different Age Groups in Sep 2023', fontsize=16, weight='bold')
ax.set_xticks(indices)
ax.set_xticklabels(hobbies, fontsize=12)
ax.legend(title='Age Groups', loc='upper left')

for i, age_group in enumerate(age_groups):
    cumulative_values = np.zeros(len(hobbies))
    for j, value in enumerate(data[age_group]):
        cumulative_values[j] = bottom_values[j] - data[age_group][j]
        ax.text(indices[j], cumulative_values[j] + value / 2, str(value),
                ha='center', va='center', fontsize=10, color='black', fontweight='bold')

ax.yaxis.grid(True, linestyle=line_styles[1], alpha=0.7)
plt.tight_layout()
plt.show()