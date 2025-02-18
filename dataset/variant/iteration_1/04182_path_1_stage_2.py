import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2010 to 2020
years = np.arange(2010, 2021)

# Data: renewable energy production in Megawatts (MW)
solar_energy = np.array([45, 60, 75, 85, 30, 95, 110, 130, 150, 160, 170])  # Randomly shuffled some content
wind_energy = np.array([40, 30, 40, 50, 65, 80, 95, 110, 25, 140, 155])    # Randomly shuffled some content
hydro_energy = np.array([25, 20, 25, 30, 35, 40, 40, 45, 50, 55, 60])     # Randomly shuffled some content

# Create the main plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot each energy source with shuffled colors
ax.plot(years, solar_energy, label="Solar Energy", color='skyblue', marker='o', linestyle='dashdot', linewidth=2)
ax.plot(years, wind_energy, label="Wind Energy", color='seagreen', marker='^', linestyle='dotted', linewidth=2)
ax.plot(years, hydro_energy, label="Hydro Energy", color='gold', marker='s', linestyle='dashed', linewidth=2)

# Title
ax.set_title("Renewable Energy Production in Greenvilla (2010-2020)\nFocus on Solar, Wind, and Hydro Energy", fontsize=16, fontweight='bold')

# Axis labels
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Production (MW)', fontsize=14)

# Axis ticks
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 201, 20))

# Legend
ax.legend(title='Energy Source', fontsize=12)

# Grid
ax.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()