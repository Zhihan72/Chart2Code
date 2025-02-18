import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2010 to 2020
years = np.arange(2010, 2021)

# Data: renewable energy production in Megawatts (MW)
solar_energy = np.array([30, 45, 60, 75, 85, 95, 110, 130, 150, 160, 170])
wind_energy = np.array([25, 30, 40, 50, 65, 80, 95, 110, 125, 140, 155])
hydro_energy = np.array([20, 25, 25, 30, 35, 40, 40, 45, 50, 55, 60])

# Create the main plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot each energy source with shuffled colors
ax.plot(years, solar_energy, label="Solar Energy", color='skyblue', marker='o', linestyle='dashdot', linewidth=2)
ax.plot(years, wind_energy, label="Wind Energy", color='seagreen', marker='^', linestyle='dotted', linewidth=2)
ax.plot(years, hydro_energy, label="Hydro Energy", color='gold', marker='s', linestyle='dashed', linewidth=2)

# Set the title with two lines for clarity
ax.set_title("Renewable Energy Production in Greenvilla (2010-2020)\nFocus on Solar, Wind, and Hydro Energy", fontsize=16, fontweight='bold')

# Set the x and y axis labels
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Production (MW)', fontsize=14)

# Set the x and y axis ticks
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 201, 20))

# Add legend
ax.legend(title='Energy Source', fontsize=12)

# Add grid for better readability
ax.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Automatically adjust layout for readability
plt.tight_layout()

# Display the plot
plt.show()