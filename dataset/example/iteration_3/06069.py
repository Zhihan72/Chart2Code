import matplotlib.pyplot as plt
import numpy as np

# Define years from 2010 to 2030
years = np.arange(2010, 2031)

# Hypothetical data: Energy consumption percentages by source
solar = np.array([3, 4, 5, 6, 8, 10, 12, 15, 18, 21, 24, 28, 32, 36, 40, 45, 50, 55, 60, 65, 70])
wind = np.array([5, 6, 7, 8, 10, 12, 14, 15, 16, 18, 20, 22, 25, 28, 30, 32, 34, 36, 38, 39, 40])
hydro = np.array([10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 23, 24, 25, 25, 26, 27, 28, 29, 30])
nuclear = np.array([20, 18, 17, 16, 15, 14, 14, 13, 12, 12, 11, 10, 10, 10, 9, 8, 8, 7, 7, 6, 5])
fossil = 100 - (solar + wind + hydro + nuclear)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plot stacked area chart
ax.stackplot(years, solar, wind, hydro, nuclear, fossil, 
             labels=['Solar', 'Wind', 'Hydro', 'Nuclear', 'Fossil Fuels'],
             colors=['#ffcc00', '#33cc33', '#3366cc', '#cc33ff', '#ff6666'],
             alpha=0.8)

# Set titles and labels
ax.set_title('Transition in Global Energy Consumption (2010-2030)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Percentage of Total Energy Consumption (%)', fontsize=14)

# Customize the legend
ax.legend(loc='upper left', fontsize=12, title='Energy Sources', title_fontsize='13')

# Customize grid lines
ax.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Adjust x-axis labels for better readability
plt.xticks(years, rotation=45)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()