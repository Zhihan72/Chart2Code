import matplotlib.pyplot as plt
import numpy as np

languages = ["Pytherion", "Rubiark", "Celenium", "Jovian", "Quarl"]
xenon_popularity = np.array([85, 65, 90, 70, 55])
zephyr_popularity = np.array([78, 80, 70, 65, 60])
orbis_popularity = np.array([92, 72, 80, 85, 68])
nova_popularity = np.array([88, 75, 85, 80, 62])  # New data series

zephyr_deviation = zephyr_popularity - xenon_popularity
orbis_deviation = orbis_popularity - xenon_popularity
nova_deviation = nova_popularity - xenon_popularity  # Deviation for new data series

bar_width = 0.2  # Adjusting to fit more bars
positions = np.arange(len(languages))

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

ax1.barh(positions, xenon_popularity, height=bar_width, color='m', label='Xenon')
ax1.barh(positions - bar_width, zephyr_deviation, left=xenon_popularity, height=bar_width, color='b', label='Zephyr')
ax1.barh(positions - 2*bar_width, orbis_deviation, left=xenon_popularity, height=bar_width, color='g', label='Orbis')
ax1.barh(positions - 3*bar_width, nova_deviation, left=xenon_popularity, height=bar_width, color='orange', label='Nova')  # New bar

ax1.set_yticks(positions)
ax1.set_yticklabels(languages)
ax1.set_xlabel('Popularity (%)', fontweight='bold', fontsize=12)
ax1.set_title('Diverging Popularity\nof Programming Languages', fontsize=14, fontweight='bold', pad=20)
ax1.legend()

years = ["2021", "2022", "2023", "2024"]
pytherion_growth = [5, 7, 10, 12]
rubiark_growth = [6, 5, 8, 9]
celenium_growth = [4, 6, 7, 11]  # New line data series

ax2.plot(years, pytherion_growth, marker='o', color='y', label='Pytherion')
ax2.plot(years, rubiark_growth, marker='s', color='c', label='Rubiark')
ax2.plot(years, celenium_growth, marker='^', color='r', label='Celenium')  # New series

ax2.set_xlabel('Year', fontweight='bold', fontsize=12)
ax2.set_ylabel('Growth (%)', fontweight='bold', fontsize=12)
ax2.set_title('Growth of Languages\nOver the Years', fontsize=14, fontweight='bold', pad=20)
ax2.legend()

plt.tight_layout()
plt.show()