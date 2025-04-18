import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2023, 2034)
types_of_fruits = ['Grapes', 'Peaches', 'Kiwi', 'Pineapples', 'Plums']
apples = [100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300]
bananas = [80, 85, 90, 95, 100, 110, 115, 120, 130, 140, 150]
cherries = [40, 50, 60, 70, 80, 90, 100, 110, 120, 125, 130]
dragonfruits = [10, 20, 25, 30, 35, 45, 50, 55, 60, 70, 80]
elderberries = [5, 10, 20, 25, 30, 40, 45, 50, 55, 65, 75]
export_data = [np.array(apples), np.array(bananas), np.array(cherries), np.array(dragonfruits), np.array(elderberries)]

fig, ax = plt.subplots(figsize=(12, 8))

line_styles = ['-', '--', '-.', ':', '-']
markers = ['s', '^', 'X', 'D', 'P']
colors = ['orange', 'blue', 'green', 'purple', 'red']

for fruit, data, line_style, marker, color in zip(types_of_fruits, export_data, line_styles, markers, colors):
    ax.plot(years, data, linestyle=line_style, marker=marker, color=color, label=fruit)

ax.set_title('Fruit Export Trends Over a Decade', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Time (Years)', fontsize=12)
ax.set_ylabel('Volume (Thousands of Tons)', fontsize=12)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

ax.grid(True, linestyle=':', alpha=0.5)
ax.legend(title='Fruit Varieties', fontsize=9, title_fontsize=10, loc='upper left')

ax.tick_params(axis='x', which='major', length=7, width=1.5, direction='inout')

plt.tight_layout()
plt.show()