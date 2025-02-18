import matplotlib.pyplot as plt
import numpy as np

# Backstory: This plot showcases the migration patterns of different species of birds over a decade as observed at a key sanctuary, highlighting key changes and trends in bird population.

# Define the years for the x-axis and the observed bird population in different species
years = np.arange(2010, 2021)
species_a = [50, 60, 70, 80, 85, 90, 95, 100, 110, 120, 130]
species_b = [30, 32, 34, 35, 38, 40, 45, 47, 50, 55, 58]
species_c = [20, 18, 15, 17, 16, 19, 22, 25, 27, 29, 30]
species_d = [10, 12, 14, 13, 11, 10, 12, 15, 20, 18, 15]
species_e = [5, 7, 9, 12, 14, 16, 18, 20, 21, 23, 25]

# Aggregate data for stacking
data = np.array([species_a, species_b, species_c, species_d, species_e])

# Colors for each bird species
colors = ['#ffa07a', '#20b2aa', '#778899', '#ff6347', '#4682b4']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 9))

# Plot the stacked area chart
ax.stackplot(years, data, labels=['Species A', 'Species B', 'Species C', 'Species D', 'Species E'],
             colors=colors, alpha=0.7)

# Set the title and axis labels
ax.set_title('Bird Migration Patterns at Sanctuary (2010-2020)', fontsize=18, fontweight='bold', loc='center')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Bird Population', fontsize=14)

# Add legend outside the plot area
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=12, title='Bird Species')

# Annotate significant changes or insights directly on the plot
ax.annotate('Notable increase in Population of Species A', xy=(2015, 320), xytext=(2012, 350),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12, ha='center')

# Annotate significant drop in Species D
ax.annotate('Decline in Species D', xy=(2018, 50), xytext=(2015, 80),
            arrowprops=dict(facecolor='red', arrowstyle='->'), fontsize=12, color='red', ha='center')

# Add grid lines for improved readability
ax.grid(axis='y', linestyle='--', alpha=0.6)

# Customize the x-ticks, including a minor grid for better readability
ax.set_xticks(years)
ax.minorticks_on()
ax.grid(which='minor', linestyle=':', linewidth='0.5', color='gray', alpha=0.7)

# Automatically adjust the layout to fit all elements
plt.tight_layout(rect=[0, 0, 0.85, 1])  # Adjust right side to make space for legend

# Display the plot
plt.show()