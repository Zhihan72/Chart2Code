import matplotlib.pyplot as plt
import numpy as np

meal_types = ['Breakfast', 'Lunch', 'Dinner', 'Snacks']

# Update age groups with an additional group '19-24'
age_groups = ['0-18', '19-24', '25-35', '36-50', '51+']
calorie_data = {
    'Breakfast': [300, 320, 350, 325, 280],
    'Lunch': [500, 520, 650, 600, 550],
    'Dinner': [600, 630, 700, 680, 620],
    'Snacks': [200, 210, 250, 225, 210]
}

colors = ['#FF9999', '#FFE699', '#66B3FF', '#99FF99', '#FFCC99']

x_positions = np.arange(len(meal_types))
bar_width = 0.15

fig, ax = plt.subplots(figsize=(12, 8))

# Plot bars for each age group including the new '19-24' group
for idx, age_group in enumerate(age_groups):
    age_group_data = [calorie_data[meal][idx] for meal in meal_types]
    ax.bar(x_positions + idx * bar_width, age_group_data, bar_width, label=age_group, color=colors[idx], alpha=0.7, edgecolor='black', linestyle='--')

ax.set_title('Comparison of Average Daily Calorie Intake\nAcross Different Meal Types and Age Groups', fontsize=16, fontweight='light', pad=25)
ax.set_xlabel('Meal Types', fontsize=14, color='darkgreen', labelpad=10)
ax.set_ylabel('Average Calorie Intake (kcal)', fontsize=14, color='darkred', labelpad=10)

ax.set_xticks(x_positions + bar_width * (len(age_groups) - 1) / 2)
ax.set_xticklabels(meal_types, rotation=10, fontsize=12, color='purple')

ax.legend(title='Age Groups', fontsize=10, title_fontsize=12, loc='upper left', shadow=True)

ax.grid(True, linestyle=':', linewidth=1, color='gray', axis='y', alpha=0.9)

plt.tight_layout()
plt.show()