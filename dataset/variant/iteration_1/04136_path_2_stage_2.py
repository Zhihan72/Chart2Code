import matplotlib.pyplot as plt
import numpy as np

# Define the data for worldwide endangered species by category
species_categories = ['Mammals', 'Birds', 'Reptiles', 'Amphibians', 'Fish']
number_of_species = [550, 679, 200, 210, 1200]
species_lost_per_year = [30, 40, 15, 18, 60]
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFB266', '#FF66A3']

# Create two pie charts
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Use different stylistic elements
ax1.pie(
    number_of_species, 
    labels=species_categories, 
    autopct='%1.1f%%', 
    startangle=45, 
    colors=colors, 
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}, # change border color and width
    explode=[0, 0.1, 0, 0, 0]  # explode second segment randomly
)
ax1.set_title('Distribution of Endangered Species\nBy Category Globally in 2023', fontsize=12, fontweight='bold')

ax2.pie(
    species_lost_per_year, 
    labels=species_categories, 
    autopct='%1.1f%%', 
    startangle=120, 
    colors=colors, 
    wedgeprops={'edgecolor': 'gray', 'linestyle': '--', 'linewidth': 1.5}, # change edge style
    explode=[0.1 if i == max(species_lost_per_year) else 0 for i in species_lost_per_year]
)
ax2.set_title('Estimated Yearly Species Loss\nBy Category Globally in 2023', fontsize=12, fontweight='bold')

plt.grid(visible=True, which='both', axis='x', color='gray', linestyle=':', linewidth=0.5)  # Add grid
fig.legend(['Mammals', 'Birds', 'Reptiles', 'Amphibians', 'Fish'], loc='upper right', fontsize=10, frameon=False) # random styling for legend

fig.suptitle('Global Endangered Species and Yearly Loss\nEstimates in 2023', fontsize=14, fontweight='bold', y=0.95)

plt.tight_layout(rect=[0, 0, 1, 0.92])
plt.show()