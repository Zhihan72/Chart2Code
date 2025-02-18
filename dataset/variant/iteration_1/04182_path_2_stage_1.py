import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Renewable energy data in Megawatts (MW)
solar_energy = np.array([30, 45, 60, 75, 85, 95, 110, 130, 150, 160, 170])
wind_energy = np.array([25, 30, 40, 50, 65, 80, 95, 110, 125, 140, 155])
hydro_energy = np.array([20, 25, 25, 30, 35, 40, 40, 45, 50, 55, 60])

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot each energy source
ax.plot(years, solar_energy, label="Solar", color='gold', marker='o', linestyle='dashdot', linewidth=2)
ax.plot(years, wind_energy, label="Wind", color='skyblue', marker='^', linestyle='dotted', linewidth=2)
ax.plot(years, hydro_energy, label="Hydro", color='seagreen', marker='s', linestyle='dashed', linewidth=2)

# Set the title and axis labels
ax.set_title("Greenvilla Energy (2010-2020)", fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Production (MW)', fontsize=14)

# Set the x and y axis ticks
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 201, 20))

# Add legend
ax.legend(title='Source', fontsize=12)

# Add grid
ax.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()