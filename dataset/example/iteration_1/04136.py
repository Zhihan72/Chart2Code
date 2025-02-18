import matplotlib.pyplot as plt
import numpy as np

# Define the data for worldwide endangered species by category
species_categories = ['Mammals', 'Birds', 'Reptiles', 'Amphibians', 'Fish', 'Insects']
number_of_species = [550, 679, 200, 210, 1200, 345]

# Additional data for the number of species lost per year (estimated)
species_lost_per_year = [30, 40, 15, 18, 60, 25]

# Define colors for the pie chart segments
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFB266', '#FF66A3', '#FFD700']

# Create a figure with two pie charts, one for total species and one for species lost per year
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# First pie chart: Total endangered species by category
ax1.pie(
    number_of_species, 
    labels=species_categories, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=colors, 
    wedgeprops={'edgecolor': 'black'}
)

ax1.set_title('Distribution of Endangered Species by Category\nGlobally in 2023', fontsize=14, fontweight='bold')

# Second pie chart: Species lost per year by category
ax2.pie(
    species_lost_per_year, 
    labels=species_categories, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=colors, 
    wedgeprops={'edgecolor': 'black'},
    explode=[0.1 if i == max(species_lost_per_year) else 0 for i in species_lost_per_year] # Explode the segment with the highest value
)

ax2.set_title('Estimated Yearly Species Loss by Category\nGlobally in 2023', fontsize=14, fontweight='bold')

# Set the same title for both pie charts
fig.suptitle('Global Endangered Species and their Yearly Loss Estimates in 2023', fontsize=16, fontweight='bold', y=0.98)

# Improve layout to prevent overlap
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Display the plots
plt.show()