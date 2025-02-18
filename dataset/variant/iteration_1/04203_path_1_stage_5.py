import matplotlib.pyplot as plt
import numpy as np

veggie_types = ['Carrots', 'Bell Peppers', 'Tomatoes', 'Cucumbers', 'Lettuce']
summer_harvest = [180, 320, 150, 240, 200]
winter_harvest = [120, 160, 100, 80, 150]
y_positions = np.arange(len(veggie_types))
bar_height = 0.35

fig, ax = plt.subplots(figsize=(12, 7))

bars_summer = ax.barh(y_positions - bar_height / 2, summer_harvest, bar_height,
                      label='Warm Season', color='#FFCC66', edgecolor='blue', linestyle='--')
bars_winter = ax.barh(y_positions + bar_height / 2, winter_harvest, bar_height,
                      label='Cold Season', color='#99FF99', edgecolor='magenta', linestyle='-.')

for bar in bars_summer + bars_winter:
    width = bar.get_width()
    ax.text(width + 5, bar.get_y() + bar.get_height() / 2, f'{width}kg', 
            va='center', ha='left', fontsize=10, weight='normal')

ax.set_ylabel('Types of Vegetables', fontsize=13, weight='normal', color='steelblue')
ax.set_xlabel('Quantity (kg)', fontsize=13, weight='normal', color='steelblue')
ax.set_title('Seasonal Vegetable Yield\nGreen Valley Farms', fontsize=16, weight='bold', color='darkred')

ax.set_yticks(y_positions)
ax.set_yticklabels(veggie_types, fontsize=12, color='darkgreen')

ax.xaxis.grid(True, linestyle='-.', color='orange', alpha=0.6)

ax.legend(loc='upper right', fontsize=12, edgecolor='gray', facecolor='lightgoldenrodyellow')

plt.tight_layout()
plt.subplots_adjust(right=0.9, left=0.2)

plt.show()