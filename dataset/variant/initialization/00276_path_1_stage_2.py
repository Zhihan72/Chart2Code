import matplotlib.pyplot as plt
import numpy as np

languages = ["Pytherion", "Rubiark", "Celenium", "Jovian", "Quarl"]
xenon_popularity = np.array([85, 65, 90, 70, 55])
zephyr_popularity = np.array([78, 80, 70, 65, 60])
orbis_popularity = np.array([92, 72, 80, 85, 68])

zephyr_deviation = zephyr_popularity - xenon_popularity
orbis_deviation = orbis_popularity - xenon_popularity

bar_width = 0.4
positions = np.arange(len(languages))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# Diverging bar chart with shuffled colors
ax1.barh(positions, xenon_popularity, edgecolor='grey', label='Xenon', height=bar_width, color='m')
ax1.barh(positions, zephyr_deviation, left=xenon_popularity, edgecolor='grey', label='Zephyr', height=bar_width, color='b')
ax1.barh(positions, orbis_deviation, left=xenon_popularity, edgecolor='grey', label='Orbis', height=bar_width, color='g')

ax1.set_yticks(positions)
ax1.set_yticklabels(languages)
ax1.set_xlabel('Popularity (%)', fontweight='bold', fontsize=12)
ax1.set_title('Diverging Popularity\nof Programming Languages', fontsize=14, fontweight='bold', pad=20)
ax1.legend(title='Planets', loc='lower right')
ax1.axvline(x=0, color='black', linewidth=0.8)
ax1.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Line chart with shuffled colors
years = ["2021", "2022", "2023", "2024"]
pytherion_growth = [5, 7, 10, 12]
rubiark_growth = [6, 5, 8, 9]

ax2.plot(years, pytherion_growth, marker='o', color='y', label='Pytherion Growth')
ax2.plot(years, rubiark_growth, marker='s', color='c', label='Rubiark Growth')
ax2.set_xlabel('Year', fontweight='bold', fontsize=12)
ax2.set_ylabel('Growth (%)', fontweight='bold', fontsize=12)
ax2.set_title('Growth of Pytherion and Rubiark\nOver the Years', fontsize=14, fontweight='bold', pad=20)
ax2.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)
ax2.legend(title='Languages', loc='upper left')

plt.tight_layout()
plt.show()