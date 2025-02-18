import matplotlib.pyplot as plt
import numpy as np

# Data for the number of adults who sleep various ranges of hours per day.
hours_range = ['0-3', '4-5', '6-7', '8-9', '10-11', '12+']
weekday_sleepers = [5, 15, 40, 80, 30, 10]
weekend_sleepers = [2, 8, 50, 90, 35, 20]

# Define positions for bars
y_pos = np.arange(len(hours_range))

# Initialize the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Bar width
bar_height = 0.4

# New colors for the bars
new_color_weekday = '#4CAF50'  # A shade of green
new_color_weekend = '#F44336'  # A shade of red

# Plot horizontal bar charts with new colors
bars1 = ax.barh(y_pos - bar_height/2, weekday_sleepers, bar_height, label='Weekdays', color=new_color_weekday, edgecolor='black', alpha=0.7)
bars2 = ax.barh(y_pos + bar_height/2, weekend_sleepers, bar_height, label='Weekends', color=new_color_weekend, edgecolor='black', alpha=0.7)

# Titles and labels
ax.set_title('Sleep Patterns of Adults\nComparison Between Weekdays and Weekends', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Number of Adults', fontsize=12)
ax.set_ylabel('Hours of Sleep', fontsize=12)

# Customize y-axis with hours range
ax.set_yticks(y_pos)
ax.set_yticklabels(hours_range, fontsize=10)

# Legend
ax.legend(title='Days', fontsize=10, loc='lower right')

# Customize x-axis grid lines
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Adding value labels on bars
def add_labels(bars, counts):
    for bar, count in zip(bars, counts):
        ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2, str(count), ha='left', va='center', fontsize=10)

add_labels(bars1, weekday_sleepers)
add_labels(bars2, weekend_sleepers)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()