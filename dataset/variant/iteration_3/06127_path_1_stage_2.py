import matplotlib.pyplot as plt
import numpy as np

hours_range = ['0-3', '4-5', '6-7', '8-9', '10-11', '12+']
weekday_sleepers = [5, 15, 40, 80, 30, 10]
weekend_sleepers = [2, 8, 50, 90, 35, 20]
young_adults_sleepers = [3, 12, 45, 85, 25, 15]

x_pos = np.arange(len(hours_range))

fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.25

# Randomly altered stylistic elements
bars1 = ax.bar(x_pos - bar_width, weekday_sleepers, bar_width, label='Weekdays', color='#d62728', edgecolor='purple', linestyle='--', linewidth=2)
bars2 = ax.bar(x_pos, weekend_sleepers, bar_width, label='Weekends', color='#9467bd', edgecolor='green', linestyle=':')
bars3 = ax.bar(x_pos + bar_width, young_adults_sleepers, bar_width, label='Young Adults', color='#8c564b', edgecolor='blue', linestyle='-', hatch='//')

ax.set_title('Sleep Patterns of Adults', fontsize=14, fontweight='normal', pad=10)
ax.set_xlabel('Hours of Sleep', fontsize=11)
ax.set_ylabel('Number of Individuals', fontsize=11)

ax.set_xticks(x_pos)
ax.set_xticklabels(hours_range, fontsize=9)

# Slightly modified legend
ax.legend(title='Categories', fontsize=9, loc='upper left')

# Altering y-axis grid lines
ax.yaxis.grid(True, linestyle='-', color='grey', alpha=0.3)

def add_labels(bars, counts):
    for bar, count in zip(bars, counts):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(count), ha='center', va='bottom', fontsize=8)

add_labels(bars1, weekday_sleepers)
add_labels(bars2, weekend_sleepers)
add_labels(bars3, young_adults_sleepers)

plt.tight_layout()
plt.show()