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

# Positions of the bars on the x-axis
indices = np.arange(len(hobbies))

# Initialize the bottom array for stacking
bottom_values = np.zeros(len(hobbies))

# Colors for each age group
colors = ['#FF9999','#66B3FF','#99FF99','#FFCC99','#FF6666']

# Plotting the stacked bars for each age group
for i, age_group in enumerate(age_groups):
    ax.bar(indices, data[age_group], label=age_group, bottom=bottom_values, color=colors[i])
    bottom_values += np.array(data[age_group])

# Adding labels and title
ax.set_xlabel('Hobbies', fontsize=14)
ax.set_ylabel('Time Spent (hours)', fontsize=14)
ax.set_title('Leisure Time Distribution:\nHow Different Age Groups Spend Their Hours in September 2023', fontsize=16, weight='bold')
ax.set_xticks(indices)
ax.set_xticklabels(hobbies, fontsize=12)
ax.legend(title='Age Groups', loc='upper right')

# Adding exact data labels on each segment of the stack
for i, age_group in enumerate(age_groups):
    cumulative_values = np.zeros(len(hobbies))
    for j, value in enumerate(data[age_group]):
        cumulative_values[j] = bottom_values[j] - data[age_group][j]
        ax.text(indices[j], cumulative_values[j] + value / 2, str(value),
                ha='center', va='center', fontsize=10, color='black', fontweight='bold')

# Adding grid for clarity
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent text from being cut off
plt.tight_layout()

# Display the stacked bar chart
plt.show()