import matplotlib.pyplot as plt
import numpy as np

languages = ["Celestial", "Quasar", "NovaScript", "Lunar", "Astrojax"]
xenon_popularity = [85, 65, 90, 70, 55]
zephyr_popularity = [78, 80, 70, 65, 60]

years = ["2021", "2022", "2023", "2024"]
pytherion_growth = [5, 7, 10, 12]
rubiark_growth = [6, 5, 8, 9]

bar_width = 0.25
r1 = np.arange(len(languages))
r2 = [x + bar_width for x in r1]

fig, (ax2, ax1) = plt.subplots(1, 2, figsize=(16, 7))

# Bar plot (ax2)
ax2.bar(r1, xenon_popularity, color='mediumblue', width=bar_width, edgecolor='grey', label='Xenon')
ax2.bar(r2, zephyr_popularity, color='mediumblue', width=bar_width, edgecolor='grey', label='Zephyr')

for rects, data in zip([r1, r2], [xenon_popularity, zephyr_popularity]):
    for rect, value in zip(rects, data):
        ax2.text(rect, value + 1, str(value), ha='center', va='bottom', fontsize=10, fontweight='bold')

ax2.set_xlabel('Tech Languages', fontweight='bold', fontsize=12)
ax2.set_ylabel('Pop Index (%)', fontweight='bold', fontsize=12)
ax2.set_title('Tech Language Popularity\nIn Cosmic Spheres', fontsize=14, fontweight='bold', pad=20)
ax2.set_xticks([r + bar_width/2 for r in range(len(languages))])
ax2.set_xticklabels(languages, rotation=30, ha='right')
ax2.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)
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