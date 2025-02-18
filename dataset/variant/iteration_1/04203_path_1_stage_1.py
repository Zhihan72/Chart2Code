import matplotlib.pyplot as plt
import numpy as np

veggie_types = ['Tomatoes', 'Cucumbers', 'Carrots', 'Bell Peppers', 'Lettuce']
summer_harvest = [320, 200, 180, 150, 240]
winter_harvest = [150, 80, 120, 100, 160]
x_positions = np.arange(len(veggie_types))
bar_width = 0.35

fig, ax = plt.subplots(figsize=(12, 7))

# Shuffled color assignment
bars_summer = ax.bar(x_positions - bar_width / 2, summer_harvest, bar_width, label='Summer', color='#66B3FF', edgecolor='black')
bars_winter = ax.bar(x_positions + bar_width / 2, winter_harvest, bar_width, label='Winter', color='#FF9999', edgecolor='black')

for bar in bars_summer + bars_winter:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 5, f'{height} kg', ha='center', va='bottom', fontsize=9, weight='bold')

ax.set_xlabel('Vegetable Types', fontsize=12, weight='bold')
ax.set_ylabel('Harvest Quantity (kg)', fontsize=12, weight='bold')
ax.set_title('Comparative Vegetable Harvest at Green Valley Farms\nBetween Summer and Winter', fontsize=14, weight='bold')

ax.set_xticks(x_positions)
ax.set_xticklabels(veggie_types, rotation=15, ha='right', fontsize=11)

ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

ax.legend(loc='upper right', fontsize=11)

plt.tight_layout()

plt.show()