import matplotlib.pyplot as plt

species_categories = ['Mammals', 'Birds', 'Reptiles', 'Amphibians', 'Fish', 'Insects']
number_of_species = [550, 679, 200, 210, 1200, 345]
species_lost_per_year = [30, 40, 15, 18, 60, 25]

colors = ['#FFB266', '#99FF99', '#66B2FF', '#FF66A3', '#FFD700', '#FF9999']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

ax1.pie(
    number_of_species,
    labels=species_categories,
    autopct='%1.1f%%',
    startangle=180,
    colors=colors,
    wedgeprops={'edgecolor': 'gray', 'width': 0.3}
)

ax1.set_title('Distribution of Endangered Species by Category\nGlobally in 2023', fontsize=14)

ax2.pie(
    species_lost_per_year,
    labels=species_categories,
    autopct='%1.1f%%',
    startangle=180,
    colors=colors,
    wedgeprops={'edgecolor': 'gray', 'width': 0.3},
    explode=[0.1 if i == max(species_lost_per_year) else 0 for i in species_lost_per_year]
)

ax2.set_title('Estimated Yearly Species Loss by Category\nGlobally in 2023', fontsize=14)

fig.patch.set_facecolor('#f2f2f2')

markers = ['o', '^', 's', 'p', 'P', '*']
legend_labels = [f'{cat} - {mark}' for cat, mark in zip(species_categories, markers)]
plt.figlegend(legend_labels, loc='lower center', ncol=3, fontsize=12)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()