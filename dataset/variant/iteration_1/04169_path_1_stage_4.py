import matplotlib.pyplot as plt
import numpy as np

regions = ['Realm of Frost', 'Woodland Mist', 'Stone Whisper', 'Sunborn Lands', 'Ashen Plains']
elves_population = [110000, 95000, 15000, 18000, 10000]
dwarves_population = [6000, 2000, 80000, 46000, 9000]
humans_population = [12000, 9000, 19000, 108000, 27000]
orcs_population = [3000, 300, 3500, 14000, 95000]

total_population = np.array(elves_population) + np.array(dwarves_population) + np.array(humans_population) + np.array(orcs_population)

colors = ['#BEE3DB', '#A3BABC', '#FFDDC1', '#D3B8AE']

fig, ax = plt.subplots(figsize=(14, 7))

ax.bar(regions, elves_population, label='Fair Folk', color=colors[0], edgecolor='green', hatch='x')
ax.bar(regions, dwarves_population, bottom=elves_population, label='Mountain Born', color=colors[1], edgecolor='red', linestyle='-')
ax.bar(regions, humans_population, bottom=np.array(elves_population) + np.array(dwarves_population), label='Sky People', color=colors[2], edgecolor='purple', hatch='//')
ax.bar(regions, orcs_population, bottom=np.array(elves_population) + np.array(dwarves_population) + np.array(humans_population), label='Wild Ones', color=colors[3], edgecolor='blue', linestyle=':')

ax.set_title('Inhabitants of Fantasy Realms\n2023 Census', fontsize=16, fontweight='bold')
ax.set_xlabel('Geographical Realms', fontsize=12)
ax.set_ylabel('Population (in Thousands)', fontsize=12)

ax.legend(title='Kindred', loc='lower right')

ax.yaxis.grid(True, linestyle='-.', alpha=0.5)

for i, total in enumerate(total_population):
    ax.text(i, total + 5000, f'{total // 1000}K Souls', ha='center', va='bottom', fontsize=10, fontweight='bold')

species = ['Fair Folk', 'Mountain Born', 'Sky People', 'Wild Ones']
population_totals = [sum(elves_population), sum(dwarves_population), sum(humans_population), sum(orcs_population)]

inset_ax = fig.add_axes([0.05, 0.7, 0.2, 0.2], aspect=1)
inset_ax.pie(population_totals, labels=species, autopct='%1.1f%%', colors=colors)
inset_ax.set_title('Proportion of Kindred', fontsize=10)

plt.tight_layout()
plt.show()