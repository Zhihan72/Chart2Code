import matplotlib.pyplot as plt
import numpy as np

years = ['2018', '2019', '2020', '2021', '2022']
tree_types = ['Oak', 'Pine', 'Maple', 'Birch', 'Cherry']
planting_data = [
    [50, 60, 45, 70, 80],  # Oak
    [80, 90, 100, 85, 95],  # Pine
    [40, 50, 55, 65, 70],  # Maple
    [30, 45, 60, 40, 50],  # Birch
    [20, 25, 30, 35, 45]   # Cherry
]

planting_data_t = np.array(planting_data).T
single_color = 'blue'

fig, ax = plt.subplots(figsize=(12, 8))

for i, tree_type in enumerate(tree_types):
    if i == 0:
        bars = ax.bar(years, planting_data_t[:, i], color=single_color, edgecolor='black')
    else:
        bars = ax.bar(years, planting_data_t[:, i], bottom=np.sum(planting_data_t[:, :i], axis=1), color=single_color, edgecolor='black')

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Trees Planted', fontsize=12)
ax.set_title('Tree Planting: 2018-2022', fontsize=16, fontweight='bold')

totals = planting_data_t.sum(axis=1)
for year, total in zip(years, totals):
    ax.text(year, total + 5, f'{total}', ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()