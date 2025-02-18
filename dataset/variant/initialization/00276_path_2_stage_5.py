import matplotlib.pyplot as plt
import numpy as np

languages = ["Celestial", "Quasar", "NovaScript", "Lunar", "Astrojax"]
xenon_popularity = [85, 65, 90, 70, 55]
zephyr_popularity = [78, 80, 70, 65, 60]

years = ["2021", "2022", "2023", "2024"]
pytherion_growth = [5, 7, 10, 12]
rubiark_growth = [6, 5, 8, 9]

bar_width = 0.4
r = np.arange(len(languages))

fig, (ax2, ax1) = plt.subplots(1, 2, figsize=(16, 7))

# Diverging bar plot (ax2)
ax2.barh(r, xenon_popularity, color='mediumblue', height=bar_width, edgecolor='grey', label='Xenon')
ax2.barh(r, [-z for z in zephyr_popularity], color='lightsteelblue', height=bar_width, edgecolor='grey', label='Zephyr')

for rect, x_value, z_value in zip(r, xenon_popularity, zephyr_popularity):
    ax2.text(x_value + 1, rect - bar_width/2, str(x_value), va='center', ha='right', fontsize=10, fontweight='bold')
    ax2.text(-z_value - 1, rect + bar_width/2, str(z_value), va='center', ha='left', fontsize=10, fontweight='bold')
    
ax2.set_xlabel('Pop Index (%)', fontweight='bold', fontsize=12)
ax2.set_ylabel('Tech Languages', fontweight='bold', fontsize=12)
ax2.set_title('Tech Language Popularity\nIn Cosmic Spheres', fontsize=14, fontweight='bold', pad=20)
ax2.set_yticks(r)
ax2.set_yticklabels(languages)
ax2.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)
ax2.legend(title='Galaxies', loc='upper right')

# Line plot (ax1)
ax1.plot(years, pytherion_growth, marker='o', color='mediumblue', label='Pytherion Rise')
ax1.plot(years, rubiark_growth, marker='s', color='mediumblue', label='Rubiark Rise')

ax1.set_xlabel('Timeline', fontweight='bold', fontsize=12)
ax1.set_ylabel('Ascension (%)', fontweight='bold', fontsize=12)
ax1.set_title('Ascent of Pytherion and Rubiark\nThrough Time', fontsize=14, fontweight='bold', pad=20)
ax1.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)
ax1.legend(title='Dialects', loc='upper left')

plt.tight_layout()
plt.show()