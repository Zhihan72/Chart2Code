import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# In the year 2100, various species on Earth are being monitored for population changes
# due to climate conditions. The following chart depicts the estimated population trends
# for some species from 2100 to 2150 based on revised ecological assessments.

# Define the years for the x-axis
years = np.arange(2100, 2151)

# Construct population data for different species over the years
mammals_population = 5000 + 80 * (years - 2100) - 0.5 * (years - 2100)**2  # starts at 5000 individuals
birds_population = 3000 + 50 * (years - 2100)  # linear growth
reptiles_population = 2000 * np.sin(0.1 * (years - 2100)) + 3000  # fluctuating population
amphibians_population = 1500 * np.exp(0.02 * (years - 2100))  # exponential growth
fish_population = 7000 - 30 * (years - 2100)  # decreasing trend

# Ensuring non-negative populations
mammals_population = np.clip(mammals_population, 0, None)
fish_population = np.clip(fish_population, 0, None)

# Create cumulative data array for stacked area chart
species_data = np.vstack([mammals_population, birds_population, reptiles_population, amphibians_population, fish_population])

# Create a figure and axis for the plot
plt.figure(figsize=(16, 10))

# Plot the stacked area chart
plt.stackplot(years, species_data, labels=['Mammals', 'Birds', 'Reptiles', 'Amphibians', 'Fish'],
              colors=['#A0522D', '#FFD700', '#32CD32', '#8A2BE2', '#1E90FF'], alpha=0.8)

# Add plot titles and axis labels
plt.title("Projected Population Trends of Various Species\n(2100-2150)", fontsize=20, fontweight='bold')
plt.xlabel("Year", fontsize=14)
plt.ylabel("Population (in thousands)", fontsize=14)

# Customize ticks and grid
plt.xticks(years[::5], rotation=45)
plt.yticks(np.arange(0, 21000, 2000))
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Add a legend
plt.legend(loc='upper left', fontsize=12, frameon=True)

# Add annotations to highlight significant points
plt.annotate('Birds Reach Critical Mass', xy=(2130, birds_population[30]), xytext=(2115, 22000),
             arrowprops=dict(arrowstyle='->', color='black'), fontsize=12, color='black')
plt.annotate('Fish Population Decline', xy=(2140, fish_population[40]), xytext=(2120, 7000),
             arrowprops=dict(arrowstyle='->', color='black'), fontsize=12, color='black')

# Automatically adjust layout for better readability
plt.tight_layout()

# Display the plot
plt.show()