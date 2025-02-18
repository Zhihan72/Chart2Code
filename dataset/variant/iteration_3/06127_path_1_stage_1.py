import matplotlib.pyplot as plt
import numpy as np

# Data: Number of individuals sleeping different hours
hours_range = ['0-3', '4-5', '6-7', '8-9', '10-11', '12+']
weekday_sleepers = [5, 15, 40, 80, 30, 10]
weekend_sleepers = [2, 8, 50, 90, 35, 20]
young_adults_sleepers = [3, 12, 45, 85, 25, 15]  # New data series

# Define positions for bars
x_pos = np.arange(len(hours_range))

# Initialize the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Bar width
bar_width = 0.25

# Plot histograms
bars1 = ax.bar(x_pos - bar_width, weekday_sleepers, bar_width, label='Weekdays', color='#1f77b4', edgecolor='black', alpha=0.7)
bars2 = ax.bar(x_pos, weekend_sleepers, bar_width, label='Weekends', color='#ff7f0e', edgecolor='black', alpha=0.7)
bars3 = ax.bar(x_pos + bar_width, young_adults_sleepers, bar_width, label='Young Adults', color='#2ca02c', edgecolor='black', alpha=0.7)

# Titles and labels
ax.set_title('Sleep Patterns of Adults\nComparison Between Weekdays, Weekends, and Young Adults', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Hours of Sleep', fontsize=12)
ax.set_ylabel('Number of Individuals', fontsize=12)

# Customize x-axis with hours range
ax.set_xticks(x_pos)
ax.set_xticklabels(hours_range, fontsize=10)

# Legend
ax.legend(title='Categories', fontsize=10, loc='upper right')

# Customize y-axis grid lines
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adding value labels on bars
def add_labels(bars, counts):
    for bar, count in zip(bars, counts):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, str(count), ha='center', va='bottom', fontsize=10)

add_labels(bars1, weekday_sleepers)
add_labels(bars2, weekend_sleepers)
add_labels(bars3, young_adults_sleepers)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()