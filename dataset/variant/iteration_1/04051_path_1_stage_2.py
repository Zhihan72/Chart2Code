import matplotlib.pyplot as plt
import numpy as np

# Define the data
years = np.arange(2010, 2021)
solar_energy = [5, 8, 15, 18, 25, 35, 50, 70, 90, 110, 130]
wind_energy = [10, 15, 20, 28, 35, 45, 60, 80, 100, 120, 140]
hydro_energy = [20, 22, 25, 30, 35, 40, 45, 50, 55, 60, 65]

# Setup the plotting area
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot each energy source
ax1.plot(years, solar_energy, color='orange', marker='o', markersize=8, linewidth=2)
ax1.plot(years, wind_energy, color='green', marker='^', markersize=8, linewidth=2, linestyle='--')
ax1.plot(years, hydro_energy, color='blue', marker='s', markersize=8, linewidth=2, linestyle='-.')

# Simplify title and labels
ax1.set_title('Renewable Energy (2010-2020)', fontsize=18, fontweight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Energy (GWh)', fontsize=14)

# Adjust ticks
ax1.set_xticks(years)
ax1.set_yticks(np.arange(0, 151, step=10))

# Combined energy plot
combined_energy = np.array(solar_energy) + np.array(wind_energy) + np.array(hydro_energy)
ax2 = ax1.twinx()
ax2.plot(years, combined_energy, color='purple', linewidth=2, alpha=0.6, linestyle='-')
ax2.set_ylabel('Total Energy (GWh)', fontsize=14, color='purple')
ax2.tick_params(axis='y', labelcolor='purple')

# Adjust layout
plt.tight_layout()

# Display
plt.show()