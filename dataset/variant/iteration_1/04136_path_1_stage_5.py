import matplotlib.pyplot as plt

species_categories = ['Birds', 'Fish', 'Mammals', 'Insects', 'Amphibians', 'Reptiles']
number_of_species = [679, 1200, 550, 345, 210, 200]
species_lost_per_year = [40, 60, 30, 25, 18, 15]

colors = ['#99FF99', '#FFD700', '#FFB266', '#FF9999', '#FF66A3', '#66B2FF']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

ax2.pie(
    number_of_species,
    labels=species_categories,
    autopct='%1.1f%%',
    startangle=180,
    colors=colors,
    wedgeprops={'edgecolor': 'gray', 'width': 0.3}
)

ax2.set_title('Categorical Spread of Endangered Animals Worldwide\n2023', fontsize=14)

ax1.pie(
    species_lost_per_year,
    labels=species_categories,
    autopct='%1.1f%%',
    startangle=180,
    colors=colors,
    wedgeprops={'edgecolor': 'gray', 'width': 0.3},
    explode=[0.1 if i == max(species_lost_per_year) else 0 for i in species_lost_per_year]
)

ax1.set_title('Annual Reduction in Species by Groups\n2023', fontsize=14)

fig.patch.set_facecolor('#f2f2f2')

markers = ['^', '*', 'o', 'P', 'p', 's']
legend_labels = [f'{cat} - {mark}' for cat, mark in zip(species_categories, markers)]
plt.figlegend(legend_labels, loc='lower center', ncol=3, fontsize=12)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()