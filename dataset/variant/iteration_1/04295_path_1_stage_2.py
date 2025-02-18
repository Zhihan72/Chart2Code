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

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 6))  # Changed to a 1x2 subplot layout

bar_width = 0.2
positions = np.arange(len(scenarios))
colors = ['#4daf4a', '#377eb8', '#ff7f00', '#984ea3']

# Bar chart on the first axis
for i, (category, color) in enumerate(zip(categories, colors)):
    bars = ax1.bar(positions + i * bar_width, usage_data[:, i], bar_width, color=color, edgecolor='gray', alpha=0.85)
    for bar in bars:
        height = bar.get_height()
        ax1.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10, color='black')

ax1.set_xlabel('Scenarios', fontsize=12)
ax1.set_ylabel('Usage of Tools (%)', fontsize=12)
ax1.set_xticks(positions + 1.5 * bar_width)
ax1.set_xticklabels(scenarios, fontsize=11)

usage_growth = np.array([
    [5, 3, 2, 7],
    [2, 4, 1, 6],
    [1, 2, 9, 3],
    [4, 5, 1, 8],
    [3, 6, 2, 10]
])

cumulative_data = np.cumsum(usage_growth, axis=0)
for i, (category, color) in enumerate(zip(categories, colors)):
    ax2.barh(positions, cumulative_data[:, i], bar_width, color=color, edgecolor='gray', alpha=0.85)

ax2.set_xlabel('Cumulative Growth (%)', fontsize=12)
ax2.set_ylabel('Scenarios', fontsize=12)
ax2.set_yticks(positions)
ax2.set_yticklabels(scenarios, fontsize=11)
ax2.invert_yaxis()

plt.tight_layout()
plt.show()