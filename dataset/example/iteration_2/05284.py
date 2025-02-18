import matplotlib.pyplot as plt
import numpy as np

# Backstory: A comparison of average time spent on various activities in a typical weekday and weekend for high school students

# Define categories of activities
activities = ['Study', 'Sports', 'Entertainment', 'Socializing', 'Sleep', 'Other']

# Data for average time spent (in hours) on each activity
weekday_hours = [6, 2, 3, 2, 8, 3]
weekend_hours = [2, 3, 4, 4, 9, 2]

# Create an array for the position of each activity
x_positions = np.arange(len(activities))

# Width of each bar
bar_width = 0.35

# Plotting the data
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the weekday hours
rects1 = ax.bar(x_positions - bar_width/2, weekday_hours, width=bar_width, label='Weekday', color='skyblue', edgecolor='black')

# Plot the weekend hours
rects2 = ax.bar(x_positions + bar_width/2, weekend_hours, width=bar_width, label='Weekend', color='salmon', edgecolor='black')

# Set the title and labels
ax.set_title('Average Time Spent on Various Activities by High School Students\nWeekday vs Weekend', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Activities', fontsize=14)
ax.set_ylabel('Average Time Spent (hours)', fontsize=14)

# Set the x-ticks and x-tick labels
ax.set_xticks(x_positions)
ax.set_xticklabels(activities, fontsize=12)

# Add a legend
ax.legend(title='Day Type', title_fontsize='13', fontsize=11, loc='upper right')

# Adding grid lines for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Adding the average time spent as text on bars
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10, fontweight='bold')

# Call the function to add text labels
add_labels(rects1)
add_labels(rects2)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()