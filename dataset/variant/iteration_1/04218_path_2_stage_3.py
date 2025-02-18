import matplotlib.pyplot as plt
import numpy as np

meal_types = ['Breakfast', 'Lunch', 'Dinner', 'Snacks']
age_groups = ['0-18', '19-24', '25-35', '36-50', '51+']
calorie_data = {
    'Breakfast': [300, 320, 350, 325, 280],
    'Lunch': [500, 520, 650, 600, 550],
    'Dinner': [600, 630, 700, 680, 620],
    'Snacks': [200, 210, 250, 225, 210]
}

colors = ['#FF9999', '#FFE699', '#66B3FF', '#99FF99', '#FFCC99']

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.6
x_positions = np.arange(len(meal_types))

# Calculate positive and negative data sets
pos_data = {meal: [cal for i, cal in enumerate(calorie_data[meal]) if i % 2 == 0] for meal in meal_types}
neg_data = {meal: [-cal for i, cal in enumerate(calorie_data[meal]) if i % 2 == 1] for meal in meal_types}

# Stacked bars
for idx, meal in enumerate(meal_types):
    ax.barh(x_positions[idx], pos_data[meal], bar_width, left=0, color=colors[1], edgecolor='black', label='Pos' if idx == 0 else "")
    ax.barh(x_positions[idx], neg_data[meal], bar_width, left=0, color=colors[3], edgecolor='black', label='Neg' if idx == 0 else "")

ax.set_yticks(x_positions)
ax.set_yticklabels(meal_types, rotation=0, fontsize=12, color='purple')
ax.set_xlabel('Calorie Intake (kcal)', fontsize=14, color='darkred', labelpad=10)
ax.set_title('Diverging Bar Chart of Calorie Intake for Meal Types', fontsize=16, fontweight='light', pad=25)

ax.legend(title='Data Type', fontsize=10, title_fontsize=12, loc='upper left', shadow=True)
ax.axvline(x=0, color='black', linewidth=1.2)

ax.grid(True, linestyle=':', linewidth=1, color='gray', axis='x', alpha=0.9)

plt.tight_layout()
plt.show()