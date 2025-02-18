import matplotlib.pyplot as plt
import numpy as np

veggie_types = ['Carrots', 'Bell Peppers', 'Tomatoes', 'Cucumbers', 'Lettuce']
summer_harvest = [320, 200, 180, 150, 240]
winter_harvest = [150, 80, 120, 100, 160]
x_positions = np.arange(len(veggie_types))
bar_width = 0.35

fig, ax = plt.subplots(figsize=(12, 7))

# Altered color and style settings
bars_summer = ax.bar(x_positions - bar_width / 2, summer_harvest, bar_width, 
                     label='Warm Season', color='#FFCC66', edgecolor='blue', linestyle='--')
bars_winter = ax.bar(x_positions + bar_width / 2, winter_harvest, bar_width, 
                     label='Cold Season', color='#99FF99', edgecolor='magenta', linestyle='-.')

for bar in bars_summer + bars_winter:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 5, f'{height}kg Harvested', 
            ha='center', va='bottom', fontsize=10, weight='normal')

ax.set_xlabel('Types of Vegetables', fontsize=13, weight='normal', color='steelblue')
ax.set_ylabel('Quantity (kg)', fontsize=13, weight='normal', color='steelblue')
ax.set_title('Seasonal Vegetable Yield\nGreen Valley Farms', fontsize=16, weight='bold', color='darkred')

ax.set_xticks(x_positions)
ax.set_xticklabels(veggie_types, rotation=45, fontsize=12, color='darkgreen')

ax.yaxis.grid(True, linestyle='-.', color='orange', alpha=0.6)

ax.legend(loc='lower left', fontsize=12, edgecolor='gray', facecolor='lightgoldenrodyellow')

plt.tight_layout()

plt.subplots_adjust(top=0.9, bottom=0.2)

plt.show()