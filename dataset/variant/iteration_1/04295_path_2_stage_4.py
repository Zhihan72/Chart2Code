import matplotlib.pyplot as plt
import numpy as np

scenarios = ['Business', 'Education', 'Entertainment', 'Health', 'Research']
categories = ['Excel', 'Python', 'Graphics', 'Statistics']

usage_data = np.array([
    [30, 50, 10, 40],
    [50, 15, 40, 25],
    [80, 25, 10, 20],
    [40, 30, 70, 10],
    [60, 90, 20, 30]
])

# Sort usage_data in ascending order across each scenario before plotting
sorted_usage_data = np.sort(usage_data, axis=0)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
bar_width = 0.2
positions = np.arange(len(scenarios))
consistent_color = '#4daf4a'

for i in range(len(categories)):
    bars = ax1.bar(positions + i * bar_width, sorted_usage_data[:, i], bar_width, color=consistent_color, edgecolor='gray', alpha=0.85)
    for bar in bars:
        height = bar.get_height()
        ax1.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10, color='black')

ax1.set_xlabel('Scenarios', fontsize=12)
ax1.set_ylabel('Usage of Tools (%)', fontsize=12)
ax1.set_title('Sorted Tool Usage Across Different Scenarios', fontsize=14, fontweight='bold', pad=15)
ax1.set_xticks(positions + 1.5 * bar_width)
ax1.set_xticklabels(scenarios, fontsize=11)

usage_growth = np.array([
    [3, 7, 2, 5],
    [6, 2, 1, 4],
    [2, 3, 9, 1],
    [5, 8, 1, 4],
    [6, 10, 2, 3]
])

# Sort cumulative_data based on growth in ascending order
cumulative_data = np.cumsum(usage_growth, axis=0)
sorted_cumulative_data = np.sort(cumulative_data, axis=0)

for i in range(len(categories)):
    ax2.barh(positions, sorted_cumulative_data[:, i], bar_width, color=consistent_color, edgecolor='gray', alpha=0.85)

ax2.set_xlabel('Cumulative Growth (%)', fontsize=12)
ax2.set_ylabel('Scenarios', fontsize=12)
ax2.set_title('Sorted Tool Usage Growth Across Different Scenarios', fontsize=14, fontweight='bold', pad=15)
ax2.set_yticks(positions)
ax2.set_yticklabels(scenarios, fontsize=11)
ax2.invert_yaxis()

plt.tight_layout()
plt.show()