import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Population data for each species (in thousands)
# Randomly altered content
deer = [12, 15, 14, 15, 18, 19, 21, 23, 24, 27, 28]
foxes = [8, 10, 9, 11, 11, 13, 12, 14, 14, 15, 16]
rabbits = [30, 26, 28, 27, 28, 30, 33, 34, 34, 37, 39]
wolves = [4, 5, 4, 5, 7, 6, 7, 6, 8, 9, 8]

# Stack the population data
populations = np.vstack([deer, foxes, rabbits, wolves])

# Define colors for each species
colors = ['#8B4513', '#D2691E', '#FFD700', '#4682B4']

# Setup the figure
plt.figure(figsize=(14, 8))

# Plot the stacked area chart
plt.stackplot(years, populations, labels=['Deer', 'Foxes', 'Rabbits', 'Wolves'], colors=colors, alpha=0.8)

# Title and labels
plt.title('Biodiversity in a Forest Over a Decade\n(2010-2020)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Population (in thousands)', fontsize=12)

# Add a legend
plt.legend(loc='upper left', title='Animal Species', bbox_to_anchor=(1, 1), fontsize=10)

# Customize the plot grid
plt.grid(linestyle='--', alpha=0.5)

# Rotate x-axis labels to avoid overlap
plt.xticks(years, rotation=45)

# Annotate significant population growth
plt.annotate('Deer Population Surge', xy=(2014, deer[4]), xytext=(2015, 20),
             arrowprops=dict(facecolor='green', arrowstyle='->', lw=1.5),
             fontsize=10, color='darkgreen', fontweight='bold')
plt.annotate('Fox Population Variability', xy=(2018, foxes[8]), xytext=(2016, 14),
             arrowprops=dict(facecolor='orange', arrowstyle='->', lw=1.5),
             fontsize=10, color='darkorange', fontweight='bold')

# Adjust the layout for better presentation
plt.tight_layout()

# Show the chart
plt.show()