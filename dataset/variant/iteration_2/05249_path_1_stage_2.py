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

fig, ax = plt.subplots(figsize=(12, 8))

# Altered line styles and markers
line_styles = ['-', '--', '-.', ':', '-']
markers = ['s', '^', 'X', 'D', 'P']

# Shuffle colors manually
colors = ['orange', 'blue', 'green', 'purple', 'red']  # New color order

for fruit, data, line_style, marker, color in zip(types_of_fruits, export_data, line_styles, markers, colors):
    ax.plot(years, data, linestyle=line_style, marker=marker, color=color, label=fruit)

ax.set_title('Projected Growth of Fruit Exports (2023-2033)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Export Volume (in thousands of tons)', fontsize=12)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

ax.grid(True, linestyle=':', alpha=0.5)
ax.legend(title='Types of Fruits', fontsize=9, title_fontsize=10, loc='upper left')

ax.tick_params(axis='x', which='major', length=7, width=1.5, direction='inout')

plt.tight_layout()
plt.show()