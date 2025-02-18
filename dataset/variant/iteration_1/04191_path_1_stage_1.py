import matplotlib.pyplot as plt
import numpy as np

# Define the time points (years)
years = np.arange(2025, 2051)

# Define energy production data for each renewable source
solar_energy = np.array([50, 65, 80, 95, 112, 130, 150, 175, 200, 230, 260, 295, 330, 370, 410, 455, 500, 550, 600, 655, 710, 770, 830, 895, 960, 1030])
wind_energy = np.array([35, 42, 50, 60, 72, 85, 99, 115, 132, 152, 174, 198, 225, 254, 285, 318, 353, 390, 430, 472, 517, 565, 616, 670, 727, 787])
hydro_energy = np.array([20, 23, 28, 34, 42, 51, 61, 74, 88, 105, 123, 143, 165, 189, 215, 243, 273, 305, 339, 375, 413, 453, 495, 540, 587, 637])

fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot the line chart for each energy source
ax1.plot(years, solar_energy, marker='o', linestyle='-', linewidth=2, color='gold')
ax1.plot(years, wind_energy, marker='s', linestyle='--', linewidth=2, color='skyblue')
ax1.plot(years, hydro_energy, marker='^', linestyle='-.', linewidth=2, color='mediumseagreen')

# Add titles and labels
ax1.set_title('Growth of Renewable Energy Production in SolarCity (2025-2050)', fontsize=16, fontweight='bold', pad=15)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Energy Production (GWh)', fontsize=14)

# Set axis limits
ax1.set_xlim(2024, 2051)
ax1.set_ylim(0, 1100)

# Predict total renewable energy production
total_energy = solar_energy + wind_energy + hydro_energy

# Create a secondary y-axis
ax2 = ax1.twinx()
ax2.plot(years, total_energy, color='purple', linestyle=':', linewidth=2, marker='x')

# Add secondary y-axis label
ax2.set_ylabel('Total Renewable Energy Production (GWh)', fontsize=14)

# Display the plot
plt.show()