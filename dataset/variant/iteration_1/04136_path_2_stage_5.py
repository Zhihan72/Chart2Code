import matplotlib.pyplot as plt
import numpy as np

species_categories = ['Mammals', 'Birds', 'Rept.', 'Amphib.', 'Fish']
number_of_species = [550, 679, 200, 210, 1200]
species_lost_per_year = [30, 40, 15, 18, 60]
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFB266', '#FF66A3']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Draw a donut chart for Annual Loss
ax1.pie(
    species_lost_per_year, 
    labels=species_categories, 
    autopct='%1.1f%%', 
    startangle=120, 
    colors=colors, 
    wedgeprops={'edgecolor': 'gray', 'linestyle': '--', 'linewidth': 1.5, 'width': 0.3}, 
    explode=[0.1 if i == max(species_lost_per_year) else 0 for i in species_lost_per_year]
)
ax1.set_title('Annual Loss', fontsize=12, fontweight='bold')

# Draw a donut chart for Endangered Species
ax2.pie(
    number_of_species, 
    labels=species_categories, 
    autopct='%1.1f%%', 
    startangle=45, 
    colors=colors, 
    wedgeprops={'edgecolor': 'white', 'linewidth': 2, 'width': 0.3}, 
    explode=[0, 0.1, 0, 0, 0]
)
ax2.set_title('Endangered Species', fontsize=12, fontweight='bold')

fig.suptitle('Species Data 2023', fontsize=14, fontweight='bold', y=0.95)

plt.tight_layout(rect=[0, 0, 1, 0.92])
plt.show()