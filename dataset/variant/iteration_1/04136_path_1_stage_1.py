import matplotlib.pyplot as plt
import numpy as np

species_categories = ['Mammals', 'Birds', 'Reptiles', 'Amphibians', 'Fish', 'Insects']
number_of_species = [550, 679, 200, 210, 1200, 345]
species_lost_per_year = [30, 40, 15, 18, 60, 25]

colors = ['#66B2FF', '#FFD700', '#99FF99', '#FF9999', '#FFB266', '#FF66A3']  # Changed the color order

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

ax1.pie(
    number_of_species, 
    labels=species_categories, 
    autopct='%1.1f%%', 
    startangle=180,  # Changed start angle
    colors=colors, 
    wedgeprops={'edgecolor': 'gray'}  # Changed border color
)

ax1.set_title('Distribution of Endangered Species by Category\nGlobally in 2023', fontsize=14)

ax2.pie(
    species_lost_per_year, 
    labels=species_categories, 
    autopct='%1.1f%%', 
    startangle=180,  # Changed start angle
    colors=colors, 
    wedgeprops={'edgecolor': 'gray'},  # Changed border color
    explode=[0.1 if i == max(species_lost_per_year) else 0 for i in species_lost_per_year]
)

ax2.set_title('Estimated Yearly Species Loss by Category\nGlobally in 2023', fontsize=14)

# Added grid effect by changing the face color of the figure
fig.patch.set_facecolor('#f2f2f2')  

# Changed the marker styles and added legend
markers = ['o', '^', 's', 'p', 'P', '*']  # Defined marker styles
legend_labels = [f'{cat} - {mark}' for cat, mark in zip(species_categories, markers)]
plt.figlegend(legend_labels, loc='lower center', ncol=3, fontsize=12)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()