import numpy as np
import matplotlib.pyplot as plt

# Define continents and renewable energy types
continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']
energy_types = ['Solar', 'Wind', 'Hydro', 'Bioenergy']

# Projections of renewable energy percentages for each continent in 2050
energy_percentages = np.array([
    [30, 25, 35, 10],  # Africa
    [40, 20, 25, 15],  # Asia
    [25, 40, 20, 15],  # Europe
    [35, 30, 25, 10],  # North America
    [20, 35, 30, 15],  # South America
    [50, 20, 20, 10]   # Oceania
])

# Define colors for each type of renewable energy
colors = ['#FFD700', '#1E90FF', '#32CD32', '#FF6347']  # Gold, Dodger Blue, Lime Green, Tomato

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot horizontal bar segment for each continent and energy type
for i, continent in enumerate(continents):
    bottom = 0
    for j, energy_type in enumerate(energy_types):
        ax.barh(continent, energy_percentages[i][j], left=bottom, color=colors[j], label=energy_type if i == 0 else "")
        bottom += energy_percentages[i][j]

# Set axis labels and title
ax.set_xlabel('Percentage')
ax.set_title('Mapping the Future:\nRenewable Energy Adoption Across the Continents (2050 Projections)', fontsize=14, fontweight='bold')

# Add a legend for the colors
ax.legend(title="Energy Types")

# Adjust layout for better fit
plt.tight_layout()

# Show the plot
plt.show()