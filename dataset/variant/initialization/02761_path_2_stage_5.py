import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1010, 1020)
atlantis_festivals = np.array([[5, 4, 3, 2], [6, 5, 4, 3], [7, 5, 5, 3], [8, 6, 5, 4], [6, 5, 4, 3], 
                               [5, 5, 3, 4], [6, 6, 4, 3], [7, 5, 5, 4], [8, 5, 6, 5], [9, 6, 6, 4]])
el_dorado_festivals = np.array([[6, 3, 4, 1], [7, 4, 5, 2], [8, 4, 6, 2], [9, 5, 6, 3], [7, 4, 5, 2],
                                [6, 4, 4, 3], [7, 5, 5, 2], [8, 4, 6, 3], [9, 4, 7, 4], [10, 5, 7, 3]])
avalon_festivals = np.array([[7, 6, 5, 4], [8, 7, 6, 5], [9, 7, 7, 5], [10, 8, 7, 6], [8, 7, 6, 5],
                             [7, 7, 5, 6], [8, 8, 6, 5], [9, 7, 7, 6], [10, 7, 8, 7], [11, 8, 8, 6]])

colors = ['#FF6347', '#4682B4', '#32CD32']

fig, ax1 = plt.subplots(figsize=(14, 9))

cities = ['Atl', 'Eldor', 'Ava']
width = 0.25  # width of a single bar
x_offsets = np.arange(len(years))  # base x-axis positions

# Plot each city's bars next to each other
for i, (city_festivals, color, label) in enumerate(zip([atlantis_festivals, el_dorado_festivals, avalon_festivals], colors, cities)):
    for j in range(city_festivals.shape[1]):
        ax1.bar(x_offsets + i * width, city_festivals[:, j], width=width, 
                color=color, edgecolor='gray', linewidth=1.2, label=f'{label} S{j+1}' if city_festivals[j][0] else "")

ax1.set_xticks(x_offsets + width)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left', bbox_to_anchor=(1.05, 1))
ax1.grid(True, linestyle='--', linewidth=0.5)

ax1.set_title('Festivals in Cities (1010-1019)', fontsize=14)
ax1.set_ylabel('Festivals')
ax1.set_xlabel('Year')
ax1.set_ylim(0, 15)

plt.tight_layout()
plt.show()