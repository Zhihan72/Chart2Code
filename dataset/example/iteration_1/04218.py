import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The National Institute of Fitness and Nutrition (NIFN) conducted a study comparing average daily calorie intake across various meal types and age groups.
# The goal is to study nutritional trends and identify areas for improvement in dietary habits.

# Meal types
meal_types = ['Breakfast', 'Lunch', 'Dinner', 'Snacks']

# Age groups and their corresponding data on daily average calorie intake (in kcal)
age_groups = ['0-18', '19-35', '36-50', '51+']
calorie_data = {
    'Breakfast': [300, 350, 325, 280],
    'Lunch': [500, 650, 600, 550],
    'Dinner': [600, 700, 680, 620],
    'Snacks': [200, 250, 225, 210]
}

# Colors for bar segments representing different age groups
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']

# X positions for bars
x_positions = np.arange(len(meal_types))

# Width of each bar
bar_width = 0.2

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the bars for each age group
for idx, age_group in enumerate(age_groups):
    # Extract the calorie data for the current age group
    age_group_data = [calorie_data[meal][idx] for meal in meal_types]
    ax.bar(x_positions + idx * bar_width, age_group_data, bar_width, label=age_group, color=colors[idx], alpha=0.7)

# Setting up the title and labels
ax.set_title('Comparison of Average Daily Calorie Intake\nAcross Different Meal Types and Age Groups', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Meal Types', fontsize=14)
ax.set_ylabel('Average Calorie Intake (kcal)', fontsize=14)

# Setting the x-ticks
ax.set_xticks(x_positions + bar_width * 1.5)
ax.set_xticklabels(meal_types)

# Adding a legend
ax.legend(title='Age Groups', fontsize=12, title_fontsize=14)

# Adding grid lines for better readability
ax.grid(True, linestyle='--', linewidth=0.5, axis='y', alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()