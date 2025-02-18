import matplotlib.pyplot as plt
import numpy as np

# Title and Backstory
# =================================================
# Fantasy Species Population in a Make-believe World by Region
# --------------------------------------------------------------
# In a make-believe fantasy world, various species inhabit different regions. The chart below shows the population distribution of Elves, Dwarves, Humans, and Orcs across different regions in the year 2023.
# =================================================

# Define regions and corresponding population data for each species
regions = ['Northern Kingdom', 'Elven Woods', 'Dwarven Mines', 'Human Empire', 'Orcish Wastes']
elves_population = [120000, 90000, 10000, 20000, 5000]
dwarves_population = [5000, 3000, 85000, 45000, 7000]
humans_population = [15000, 8000, 20000, 110000, 25000]
orcs_population = [2000, 500, 3000, 15000, 90000]

# Calculate total population for annotations
total_population = np.array(elves_population) + np.array(dwarves_population) + np.array(humans_population) + np.array(orcs_population)

# Set colors for different species
colors = ['#FFDDC1', '#D3B8AE', '#BEE3DB','#A3BABC']  # Elves, Dwarves, Humans, Orcs

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 7))

# Stack the bar segments
ax.bar(regions, elves_population, label='Elves', color=colors[0], edgecolor='black')
ax.bar(regions, dwarves_population, bottom=elves_population, label='Dwarves', color=colors[1], edgecolor='black')
ax.bar(regions, humans_population, bottom=np.array(elves_population) + np.array(dwarves_population), label='Humans', color=colors[2], edgecolor='black')
ax.bar(regions, orcs_population, bottom=np.array(elves_population) + np.array(dwarves_population) + np.array(humans_population), label='Orcs', color=colors[3], edgecolor='black')

# Set title and labels with multi-line title for better visibility
ax.set_title('Fantasy Species Population Distribution by Region\nin the Make-believe World (2023)', fontsize=16, fontweight='bold', loc='center')
ax.set_xlabel('Regions', fontsize=12)
ax.set_ylabel('Population (in Thousands)', fontsize=12)

# Add a legend and customize its position
ax.legend(title='Species', loc='upper left', bbox_to_anchor=(1, 1))

# Add grid lines for readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adding annotations for total population in each region
for i, total in enumerate(total_population):
    ax.text(i, total + 5000, f'{total // 1000}K', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Create an inset pie chart to show total population distribution by species
species = ['Elves', 'Dwarves', 'Humans', 'Orcs']
population_totals = [sum(elves_population), sum(dwarves_population), sum(humans_population), sum(orcs_population)]

inset_ax = fig.add_axes([0.75, 0.6, 0.2, 0.2], aspect=1)
inset_ax.pie(population_totals, labels=species, autopct='%1.1f%%', colors=colors)
inset_ax.set_title('Overall Population Share', fontsize=10)

# Automatically adjust layout for better fit
plt.tight_layout()

# Display the plot
plt.show()