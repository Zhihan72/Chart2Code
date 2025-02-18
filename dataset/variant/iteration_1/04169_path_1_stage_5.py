import matplotlib.pyplot as plt
import numpy as np

regions = ['Realm of Frost', 'Woodland Mist', 'Stone Whisper', 'Sunborn Lands', 'Ashen Plains']
elves_population = [110000, 95000, 15000, 18000, 10000]
dwarves_population = [6000, 2000, 80000, 46000, 9000]
humans_population = [12000, 9000, 19000, 108000, 27000]
orcs_population = [3000, 300, 3500, 14000, 95000]

colors = ['#BEE3DB', '#A3BABC', '#FFDDC1', '#D3B8AE']
bar_width = 0.2
indices = np.arange(len(regions))

fig, ax = plt.subplots(figsize=(14, 7))

ax.bar(indices, elves_population, width=bar_width, label='Fair Folk', color=colors[0], edgecolor='green', hatch='x')
ax.bar(indices + bar_width, dwarves_population, width=bar_width, label='Mountain Born', color=colors[1], edgecolor='red', linestyle='-')
ax.bar(indices + bar_width * 2, humans_population, width=bar_width, label='Sky People', color=colors[2], edgecolor='purple', hatch='//')
ax.bar(indices + bar_width * 3, orcs_population, width=bar_width, label='Wild Ones', color=colors[3], edgecolor='blue', linestyle=':')

ax.set_title('Inhabitants of Fantasy Realms\n2023 Census', fontsize=16, fontweight='bold')
ax.set_xlabel('Geographical Realms', fontsize=12)
ax.set_ylabel('Population (in Thousands)', fontsize=12)
ax.set_xticks(indices + bar_width * 1.5)
ax.set_xticklabels(regions)

ax.legend(title='Kindred', loc='upper left')

ax.yaxis.grid(True, linestyle='-.', alpha=0.5)

plt.tight_layout()
plt.show()