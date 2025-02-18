import matplotlib.pyplot as plt
import numpy as np

regions = ['Northern Kingdom', 'Elven Woods', 'Dwarven Mines', 'Human Empire', 'Orcish Wastes']
elves_population = [120000, 90000, 10000, 20000, 5000]
dwarves_population = [5000, 3000, 85000, 45000, 7000]
humans_population = [15000, 8000, 20000, 110000, 25000]
orcs_population = [2000, 500, 3000, 15000, 90000]

colors = ['#FFDDC1', '#D3B8AE', '#BEE3DB', '#A3BABC']

fig, ax = plt.subplots(figsize=(14, 7))

ax.bar(regions, elves_population, color=colors[0], edgecolor='black')
ax.bar(regions, dwarves_population, bottom=elves_population, color=colors[1], edgecolor='black')
ax.bar(regions, humans_population, bottom=np.array(elves_population) + np.array(dwarves_population), color=colors[2], edgecolor='black')
ax.bar(regions, orcs_population, bottom=np.array(elves_population) + np.array(dwarves_population) + np.array(humans_population), color=colors[3], edgecolor='black')

ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Remove annotations for total population

# Create an inset pie chart
species = ['Elves', 'Dwarves', 'Humans', 'Orcs']
population_totals = [sum(elves_population), sum(dwarves_population), sum(humans_population), sum(orcs_population)]

inset_ax = fig.add_axes([0.75, 0.6, 0.2, 0.2], aspect=1)
inset_ax.pie(population_totals, colors=colors)

plt.tight_layout()
plt.show()