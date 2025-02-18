import matplotlib.pyplot as plt
import numpy as np

# Define the age groups and hobbies
age_groups = ['Teens', '20s', '30s', '40s', '50+']
hobbies = ['Reading', 'Gardening', 'Gaming', 'Cooking', 'Exercising']

# Amount of time spent on each hobby for each age group
data = {
    'Teens':       [12,  8, 50, 10, 15],
    '20s':         [15, 12, 45, 20, 20],
    '30s':         [20, 20, 30, 25, 30],
    '40s':         [25, 30, 15, 30, 25],
    '50+':         [30, 35, 10, 35, 20]
}

# Create a figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Setting the width of the bars
bar_width = 0.15

# Positions of the bars on the x-axis
indices = np.arange(len(hobbies))

# Use a single color for all age groups
single_color = '#3375FF'

# Plotting the bars for each age group
for i, age_group in enumerate(age_groups):
    offset = i * bar_width
    ax.bar(indices + offset, data[age_group], width=bar_width, label=age_group, color=single_color)

# Adding labels and title
ax.set_xlabel('Hobbies', fontsize=14)
ax.set_ylabel('Time Spent (hours)', fontsize=14)
ax.set_title('Leisure Time Distribution:\nHow Different Age Groups Spend Their Hours in September 2023', fontsize=16, weight='bold')
ax.set_xticks(indices + bar_width*2)
ax.set_xticklabels(hobbies, fontsize=12)
ax.legend(title='Age Groups', loc='upper right')

# Adding exact data labels on top of each bar
for i, age_group in enumerate(age_groups):
    for j, value in enumerate(data[age_group]):
        ax.text(j + i * bar_width, value + 0.5, str(value),
                ha='center', va='bottom', fontsize=10, color=single_color, fontweight='bold')

# Adding grid for clarity
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent text from being cut off
plt.tight_layout()

# Display the bar chart
plt.show()