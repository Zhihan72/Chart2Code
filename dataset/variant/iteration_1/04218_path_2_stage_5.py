import matplotlib.pyplot as plt
import numpy as np

meal_types = ['Breakfast', 'Lunch', 'Dinner', 'Snacks']
calorie_data = {
    'Breakfast': [300, 320, 350, 325, 280],
    'Lunch': [500, 520, 650, 600, 550],
    'Dinner': [600, 630, 700, 680, 620],
    'Snacks': [200, 210, 250, 225, 210]
}

# New set of colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.6
x_positions = np.arange(len(meal_types))

# Calculate positive and negative data sets
pos_data = {meal: [cal for i, cal in enumerate(calorie_data[meal]) if i % 2 == 0] for meal in meal_types}
neg_data = {meal: [-cal for i, cal in enumerate(calorie_data[meal]) if i % 2 == 1] for meal in meal_types}

# Stacked bars
for idx, meal in enumerate(meal_types):
    ax.barh(x_positions[idx], pos_data[meal], bar_width, left=0, color=colors[0], edgecolor='black', label='Pos' if idx == 0 else "")
    ax.barh(x_positions[idx], neg_data[meal], bar_width, left=0, color=colors[2], edgecolor='black', label='Neg' if idx == 0 else "")

ax.set_yticks(x_positions)
ax.set_yticklabels([''] * len(meal_types))
ax.legend(title='Data Type', fontsize=10, title_fontsize=12, loc='upper left', shadow=True)
ax.axvline(x=0, color='black', linewidth=1.2)

ax.grid(True, linestyle=':', linewidth=1, color='gray', axis='x', alpha=0.9)

plt.tight_layout()
plt.show()