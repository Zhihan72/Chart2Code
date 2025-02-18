import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2023, 2034)
types_of_fruits = ['Apples', 'Bananas', 'Cherries', 'Dragonfruits', 'Elderberries']

apples = [100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300]
bananas = [80, 85, 90, 95, 100, 110, 115, 120, 130, 140, 150]
cherries = [40, 50, 60, 70, 80, 90, 100, 110, 120, 125, 130]
dragonfruits = [10, 20, 25, 30, 35, 45, 50, 55, 60, 70, 80]
elderberries = [5, 10, 20, 25, 30, 40, 45, 50, 55, 65, 75]

export_data = [np.array(apples), np.array(bananas), np.array(cherries), np.array(dragonfruits), np.array(elderberries)]

# New set of colors for each fruit type
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF']

fig, ax = plt.subplots(figsize=(12, 8))

# Plot with new color scheme
for fruit, data, color in zip(types_of_fruits, export_data, colors):
    ax.plot(years, data, marker='o', label=fruit, color=color)

ax.set_title('Projected Growth of Fruit Exports (2023-2033)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Export Volume (in thousands of tons)', fontsize=12)
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(title='Types of Fruits', fontsize=10, title_fontsize=11)

plt.tight_layout()
plt.show()