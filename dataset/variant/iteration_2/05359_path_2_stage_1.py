import matplotlib.pyplot as plt
import numpy as np

# Define activities and corresponding average weekly hours
activities = ['Social Media', 'Gaming', 'E-Learning', 'TV Streaming', 'Reading eBooks', 'Video Calls']
average_hours_lockdown = np.array([15, 10, 25, 30, 5, 20])
average_hours_prelockdown = np.array([5, 8, 10, 15, 3, 6])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 7))

# Define the bar width and positions
bar_width = 0.35
index = np.arange(len(activities))

# Reassign colors for each data group
lockdown_colors = ['orange', 'teal', 'skyblue', 'lightgreen', 'yellow', 'coral']
prelockdown_colors = ['purple', 'red', 'cyan', 'pink', 'grey', 'blue']

# Bar plot: average weekly hours spent on activities
bar1 = ax.bar(index, average_hours_lockdown, bar_width, label='During Lockdown', color=lockdown_colors, edgecolor='gray')
bar2 = ax.bar(index + bar_width, average_hours_prelockdown, bar_width, label='Before Lockdown', color=prelockdown_colors, edgecolor='gray')

# Titles and labels
ax.set_title('Weekly Average Screen Time by Activity\nMiddle School Students During COVID-19 Lockdown', fontsize=15, fontweight='bold')
ax.set_xlabel('Activity Type', fontsize=12)
ax.set_ylabel('Average Hours per Week', fontsize=12)
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(activities, fontsize=10, rotation=30, ha='right')
ax.legend(fontsize=10)

# Add data labels to bars
for bar_group in [bar1, bar2]:
    for bar in bar_group:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 0.5, f'{height}', ha='center', va='bottom', fontsize=10)

# Enhancements
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()