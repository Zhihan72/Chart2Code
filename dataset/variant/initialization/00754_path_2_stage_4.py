import numpy as np
import matplotlib.pyplot as plt

cities = ['NY', 'LDN', 'TYO', 'SYD']
plant_types = ['Tree', 'Shrub', 'Flower']
years = np.array(['2018', '2019', '2020', '2021', '2022'])

data = np.array([
    [[30, 25, 40, 35], [35, 28, 38, 36], [38, 30, 35, 34], [40, 32, 32, 33], [42, 34, 30, 32]],
    [[20, 18, 22, 21], [22, 20, 24, 23], [24, 22, 26, 25], [26, 24, 28, 27], [28, 26, 30, 29]],
    [[15, 10, 12, 11], [16, 11, 14, 12], [18, 13, 16, 15], [20, 15, 18, 17], [22, 17, 20, 19]],
])

data_pos = data[:2]
data_neg = data[2:]

fig, ax = plt.subplots(figsize=(12, 8))

single_color = '#3498db'

for i, city in enumerate(cities):
    for plant_idx in range(len(data) - 1):
        ax.barh(-np.arange(len(years)) + i*len(years), data_pos[plant_idx, :, i],
                left=np.sum(data_pos[:plant_idx, :, i], axis=0), color=single_color,
                label=plant_types[plant_idx] if i == 0 else "")
    
    ax.barh(-np.arange(len(years)) + i*len(years), -data_neg[0, :, i], color=single_color,
            label=plant_types[2] if i == 0 else "")

ytick_labels = [f"{year} - {city}" for city in cities for year in years]
ytick_positions = -np.arange(len(ytick_labels))

ax.set_yticks(ytick_positions)
ax.set_yticklabels(ytick_labels, fontsize=10)
ax.set_xticks(np.arange(-100, 101, 20))
ax.set_xlabel('Number of Plants')
ax.set_ylabel('Year - City')
ax.legend(title='Plants', loc='upper right', bbox_to_anchor=(1.2, 1))

ax.set_title('Urban Greenery \nDiverging Plant Analysis', pad=20, fontsize=14, weight='bold')

plt.tight_layout()
plt.show()