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

# Changed styles for the bars
bars_summer = ax.bar(x_positions - bar_width / 2, sorted_summer_harvest, bar_width, label='Summer Harvest', color='#FFA07A', linestyle='-', edgecolor='purple')
bars_winter = ax.bar(x_positions + bar_width / 2, sorted_winter_harvest, bar_width, label='Winter Harvest', color='#20B2AA', linestyle='-.', edgecolor='brown')

for bar in bars_summer + bars_winter:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 2, f'{height} kg', ha='right', va='bottom', fontsize=10, fontstyle='italic')

ax.set_xlabel('Types of Vegetables', fontsize=13, fontstyle='italic')
ax.set_ylabel('Harvest (in kg)', fontsize=13, fontweight='light')
ax.set_title('Green Valley Farms: Seasonal Harvest Overview', fontsize=15, fontstyle='oblique')
ax.set_xticks(x_positions)
ax.set_xticklabels(sorted_veggie_types, rotation=25, ha='right', fontsize=10, weight='bold')
ax.yaxis.grid(True, linestyle=':', which='major', color='black', alpha=0.5)
ax.legend(loc='lower center', fontsize=10, shadow=True)
plt.tight_layout()
plt.show()