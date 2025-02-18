import matplotlib.pyplot as plt
import numpy as np

regions = ['Northern Kingdom', 'Elven Woods', 'Dwarven Mines', 'Human Empire', 'Orcish Wastes']
elves_population = [110000, 95000, 15000, 18000, 10000]
dwarves_population = [6000, 2000, 80000, 46000, 9000]
humans_population = [12000, 9000, 19000, 108000, 27000]
orcs_population = [3000, 300, 3500, 14000, 95000]

total_population = np.array(elves_population) + np.array(dwarves_population) + np.array(humans_population) + np.array(orcs_population)

# Manually shuffled colors
colors = ['#BEE3DB', '#A3BABC', '#FFDDC1', '#D3B8AE']

fig, ax = plt.subplots(figsize=(14, 7))

ax.bar(regions, elves_population, label='Elves', color=colors[0], edgecolor='green', hatch='x')
ax.bar(regions, dwarves_population, bottom=elves_population, label='Dwarves', color=colors[1], edgecolor='red', linestyle='-')
ax.bar(regions, humans_population, bottom=np.array(elves_population) + np.array(dwarves_population), label='Humans', color=colors[2], edgecolor='purple', hatch='//')
ax.bar(regions, orcs_population, bottom=np.array(elves_population) + np.array(dwarves_population) + np.array(humans_population), label='Orcs', color=colors[3], edgecolor='blue', linestyle=':')

ax.set_title('Fantasy Species Population Distribution by Region\nin the Make-believe World (2023)', fontsize=16, fontweight='bold')
ax.set_xlabel('Regions', fontsize=12)
ax.set_ylabel('Population (in Thousands)', fontsize=12)

ax.legend(title='Species', loc='lower right')

ax.yaxis.grid(True, linestyle='-.', alpha=0.5)

for i, total in enumerate(total_population):
    ax.text(i, total + 5000, f'{total // 1000}K', ha='center', va='bottom', fontsize=10, fontweight='bold')

species = ['Elves', 'Dwarves', 'Humans', 'Orcs']
population_totals = [sum(elves_population), sum(dwarves_population), sum(humans_population), sum(orcs_population)]

inset_ax = fig.add_axes([0.05, 0.7, 0.2, 0.2], aspect=1)
inset_ax.pie(population_totals, labels=species, autopct='%1.1f%%', colors=colors)
inset_ax.set_title('Overall Population Share', fontsize=10)

plt.tight_layout()
plt.show()