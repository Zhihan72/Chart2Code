import matplotlib.pyplot as plt
import numpy as np

veggie_types = ['Tomatoes', 'Cucumbers', 'Carrots', 'Bell Peppers']
summer_harvest = [320, 200, 180, 150]
winter_harvest = [150, 80, 120, 100]

combined_data = list(zip(veggie_types, summer_harvest, winter_harvest))
combined_data.sort(key=lambda x: x[1], reverse=True)

sorted_veggie_types, sorted_summer_harvest, sorted_winter_harvest = zip(*combined_data)

x_positions = np.arange(len(sorted_veggie_types))
bar_width = 0.35

fig, ax = plt.subplots(figsize=(12, 7))

# Shuffled colors for the bars
bars_summer = ax.bar(x_positions - bar_width / 2, sorted_summer_harvest, bar_width, label='Summer', color='#66B3FF', edgecolor='black')
bars_winter = ax.bar(x_positions + bar_width / 2, sorted_winter_harvest, bar_width, label='Winter', color='#FF9999', edgecolor='black')

for bar in bars_summer + bars_winter:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 5, f'{height} kg', ha='center', va='bottom', fontsize=9, weight='bold')

ax.set_xlabel('Vegetable Types', fontsize=12, weight='bold')
ax.set_ylabel('Harvest Quantity (kg)', fontsize=12, weight='bold')
ax.set_title('Comparative Vegetable Harvest at Green Valley Farms\nBetween Summer and Winter', fontsize=14, weight='bold')
ax.set_xticks(x_positions)
ax.set_xticklabels(sorted_veggie_types, rotation=15, ha='right', fontsize=11)
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)
ax.legend(loc='upper right', fontsize=11)
plt.tight_layout()
plt.show()