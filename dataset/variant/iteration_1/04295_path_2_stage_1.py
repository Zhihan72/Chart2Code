import matplotlib.pyplot as plt
import numpy as np

scenarios = ['Business', 'Education', 'Entertainment', 'Health', 'Research']
categories = ['Excel', 'Python', 'Graphics', 'Statistics']

usage_data = np.array([
    [40, 30, 20, 50],
    [25, 50, 15, 40],
    [10, 20, 80, 25],
    [30, 40, 10, 70],
    [20, 60, 30, 90]
])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))

bar_width = 0.2
positions = np.arange(len(scenarios))
consistent_color = '#4daf4a'  # Choosing a single consistent color

for i in range(len(categories)):
    bars = ax1.bar(positions + i * bar_width, usage_data[:, i], bar_width, label=categories[i], color=consistent_color, edgecolor='gray', alpha=0.85)
    for bar in bars:
        height = bar.get_height()
        ax1.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10, color='black')

ax1.set_xlabel('Scenarios', fontsize=12)
ax1.set_ylabel('Usage of Tools (%)', fontsize=12)
ax1.set_title('Tool Usage Across Different Scenarios', fontsize=14, fontweight='bold', pad=15)
ax1.set_xticks(positions + 1.5 * bar_width)
ax1.set_xticklabels(scenarios, fontsize=11)
ax1.legend(title="Tools", fontsize=10, loc='upper right')
ax1.yaxis.grid(True, linestyle='--', alpha=0.6)

usage_growth = np.array([
    [5, 3, 2, 7],
    [2, 4, 1, 6],
    [1, 2, 9, 3],
    [4, 5, 1, 8],
    [3, 6, 2, 10]
])

cumulative_data = np.cumsum(usage_growth, axis=0)
for i in range(len(categories)):
    ax2.barh(positions, cumulative_data[:, i], bar_width, label=categories[i], color=consistent_color, edgecolor='gray', alpha=0.85)

ax2.set_xlabel('Cumulative Growth (%)', fontsize=12)
ax2.set_ylabel('Scenarios', fontsize=12)
ax2.set_title('Tool Usage Growth Across Different Scenarios', fontsize=14, fontweight='bold', pad=15)
ax2.set_yticks(positions)
ax2.set_yticklabels(scenarios, fontsize=11)
ax2.legend(title="Tools", fontsize=10, loc='lower right')
ax2.xaxis.grid(True, linestyle='--', alpha=0.6)
ax2.invert_yaxis()

plt.tight_layout()
plt.show()