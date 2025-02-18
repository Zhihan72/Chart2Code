import matplotlib.pyplot as plt
import numpy as np

# Define activities and corresponding average weekly hours
activities = ['Social Media', 'Gaming', 'E-Learning', 'TV Streaming', 'Reading eBooks', 'Video Calls']
average_hours_lockdown = np.array([15, 10, 25, 30, 5, 20])
average_hours_prelockdown = np.array([5, 8, 10, 15, 3, 6])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Define the bar width and positions
bar_height = 0.35
index = np.arange(len(activities))

# Horizontal bar plot: average weekly hours spent on activities
bar1 = ax.barh(index, average_hours_lockdown, bar_height, label='During Lockdown', color='teal', edgecolor='gray')
bar2 = ax.barh(index + bar_height, average_hours_prelockdown, bar_height, label='Before Lockdown', color='orange', edgecolor='gray')

# Titles and labels
ax.set_title('Weekly Average Screen Time by Activity\nMiddle School Students During COVID-19 Lockdown', fontsize=15, fontweight='bold')
ax.set_xlabel('Average Hours per Week', fontsize=12)
ax.set_ylabel('Activity Type', fontsize=12)
ax.set_yticks(index + bar_height / 2)
ax.set_yticklabels(activities, fontsize=10, rotation=0, va='center')
ax.legend(fontsize=10)

# Add data labels to bars
for bar_group in [bar1, bar2]:
    for bar in bar_group:
        width = bar.get_width()
        ax.text(width + 0.5, bar.get_y() + bar.get_height() / 2, f'{width}', va='center', ha='left', fontsize=10)

# Enhancements
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()