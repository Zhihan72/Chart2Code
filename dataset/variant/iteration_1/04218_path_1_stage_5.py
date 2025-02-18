import matplotlib.pyplot as plt
import numpy as np

meal_types = ['Brunch', 'Midday Meal', 'Evening Feast']

age_groups = ['Kids', 'Young', 'Middle-Aged', 'Seniors']
calorie_data = {
    'Breakfast': [300, 350, 325, 280],
    'Lunch': [500, 650, 600, 550],
    'Dinner': [600, 700, 680, 620]
}

colors = ['#334D5C', '#45B29D', '#EFC94C', '#E27A3F']
x_positions = np.arange(len(meal_types))

fig, ax = plt.subplots(figsize=(12, 8))

bottom_values = np.zeros(len(meal_types))

# Create stacked bar chart with altered styles
for idx, age_group in enumerate(age_groups):
    age_group_data = [calorie_data[meal][idx] for meal in ['Breakfast', 'Lunch', 'Dinner']]
    ax.bar(x_positions, age_group_data, label=age_group,
           color=colors[idx], alpha=0.9, linestyle='-', edgecolor='black',
           hatch='/' if idx % 2 == 0 else '\\', bottom=bottom_values)
    bottom_values += age_group_data

ax.set_title('Daily Calorie Consumption\nPer Meal Type and Age Range', fontsize=14, fontweight='normal', pad=20)
ax.set_xlabel('Types of Meals', fontsize=12)
ax.set_ylabel('Calorie Avg (kcal)', fontsize=12)

ax.set_xticks(x_positions)
ax.set_xticklabels(meal_types)

ax.legend(title='Age Ranges', fontsize=10, title_fontsize=12, loc='upper left', edgecolor='black')

ax.grid(True, linestyle='-.', linewidth=1, alpha=0.3, axis='both')

plt.tight_layout()

plt.show()