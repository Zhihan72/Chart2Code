import matplotlib.pyplot as plt
import numpy as np

# Define the time points (years)
years = np.arange(2025, 2051)

# Define energy production data for selected renewable source
solar_energy = np.array([50, 65, 80, 95, 112, 130, 150, 175, 200, 230, 260, 295, 330, 370, 410, 455, 500, 550, 600, 655, 710, 770, 830, 895, 960, 1030])

fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot the line chart for solar energy
ax1.plot(years, solar_energy, marker='o', linestyle='-', linewidth=2, color='gold')

# Add titles and labels
ax1.set_title('Growth of Solar Energy Production in SolarCity (2025-2050)', fontsize=16, fontweight='bold', pad=15)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Energy Production (GWh)', fontsize=14)

# Set axis limits
ax1.set_xlim(2024, 2051)
ax1.set_ylim(0, 1100)

# Display the plot
plt.show()