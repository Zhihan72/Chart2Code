import matplotlib.pyplot as plt
import numpy as np

# Decades from 1980 to 2020
decades = np.array([1980, 1990, 2000, 2010, 2020])

# Population data for each bird species
species_a_population = np.array([50, 150, 300, 350, 400])
species_b_population = np.array([30, 70, 120, 170, 220])
species_c_population = np.array([80, 130, 180, 240, 310])

# Setting up the scatter plot
plt.figure(figsize=(12, 8))

# Shuffle the colors assigned to each species
plt.scatter(decades, species_a_population, color='green', label='Species A', edgecolor='k', s=100, alpha=0.7)
plt.scatter(decades, species_b_population, color='red', label='Species B', edgecolor='k', s=100, alpha=0.7)
plt.scatter(decades, species_c_population, color='blue', label='Species C', edgecolor='k', s=100, alpha=0.7)

# Adding title and labels
plt.title('Population Growth of Bird Species Over Time (1980-2020)', fontsize=16, fontweight='bold', loc='center')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Birds', fontsize=12)

# Adding a legend to differentiate between the species
plt.legend(title='Bird Species', loc='upper left')

# Adding grid for clarity
plt.grid(visible=True, linestyle='--', alpha=0.7)

# Automatically adjusting the layout for better readability
plt.tight_layout()

# Display the scatter plot
plt.show()