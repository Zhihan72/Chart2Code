import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Backstory: Fictional Study on Bird Migration Patterns Across Various Regions
# This study focuses on the density of bird sightings in different regions at three times of the year: Spring, Summer, and Winter.

# Define the regions
regions = ['Region A', 'Region B', 'Region C', 'Region D', 'Region E']

# Bird sightings data (density per km²) for three periods
spring_density = np.array([
    [10, 15, 11, 14, 12], 
    [20, 23, 18, 21, 22], 
    [30, 35, 32, 28, 33],
    [25, 26, 28, 27, 24],
    [15, 16, 14, 13, 17]
])

summer_density = np.array([
    [12, 18, 13, 16, 14], 
    [22, 25, 20, 23, 24], 
    [32, 37, 34, 30, 35],
    [27, 28, 30, 29, 26],
    [17, 18, 16, 15, 19]
])

winter_density = np.array([
    [8, 12, 9, 11, 10], 
    [18, 21, 16, 19, 20], 
    [28, 33, 30, 26, 31],
    [23, 24, 26, 25, 22],
    [13, 14, 12, 11, 15]
])

# Create a figure with multiple subplots
fig, axs = plt.subplots(3, 1, figsize=(10, 15), tight_layout=True)

# Define the density plot function
def create_density_plot(ax, data, season):
    sns.violinplot(data=data,
                   ax=ax, linewidth=1.5)
    ax.set_title(f'Bird Sighting Density in Different Regions - {season}', fontsize=14, fontweight='bold')
    ax.set_xlabel('Region', fontsize=12)
    ax.set_ylabel('Density (sightings per km²)', fontsize=12)
    ax.set_xticklabels(regions, rotation=30, ha='right')

# Create density plots for each season
create_density_plot(axs[0], spring_density, 'Spring')
create_density_plot(axs[1], summer_density, 'Summer')
create_density_plot(axs[2], winter_density, 'Winter')

# Show the plot
plt.show()