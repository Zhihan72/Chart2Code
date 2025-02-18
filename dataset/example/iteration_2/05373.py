import matplotlib.pyplot as plt
import numpy as np

# Backstory: Illustrating the impact of time spent on different tasks during a work-from-home day
tasks = ['Emails', 'Meetings', 'Coding', 'Lunch', 'Breaks', 'Project Planning']
hours_data = [2.5, 2, 4, 1, 1, 1.5]

# Incremental time spent on each task
incremental_hours = np.cumsum(hours_data)

# Define the stages of the work-from-home day and their corresponding times
day_stages = ['Start', 'Emails', 'Meetings', 'Coding', 'Lunch', 'Breaks', 'Project Planning']

# Time points for plotting
time_points = [0] + incremental_hours.tolist()

# Create the figure and subplots
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the line chart
ax.plot(day_stages, time_points, marker='o', linestyle='-', linewidth=2, color='teal', label='Time Spent')

# Annotate time points
for i, txt in enumerate(time_points[1:]):
    ax.annotate(f'{txt:.1f} hrs', (day_stages[i + 1], time_points[i + 1]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=10, color='teal')

# Add gridlines for better readability
ax.grid(True, linestyle='--', linewidth=0.5)

# Customize the plot
plt.xticks(rotation=45, ha='right')
plt.yticks(np.arange(0, 13, 1))
plt.xlabel('Work-from-Home Day Stages')
plt.ylabel('Cumulative Time Spent (Hours)')
plt.title('The Flow of a Work-from-Home Day:\nTime Spent on Various Tasks')
plt.legend(title='Tasks')

# Ensure the layout is optimal and elements do not overlap
plt.tight_layout()

# Display the plot
plt.show()