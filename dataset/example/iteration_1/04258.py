import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# Renewable energy sources have been a significant focus of energy policies around the world. 
# This plot shows the progress of solar and wind energy production over a period of 10 years (2010-2020) 
# in a hypothetical country, Solaria. Additionally, we'll show the total energy production 
# from these renewable sources, combining the individual productions of solar and wind energy.

# Defining the years from 2010 to 2020
years = np.arange(2010, 2021)

# Annual production of solar energy (in Gigawatts)
solar_energy = np.array([5, 10, 15, 20, 30, 40, 55, 70, 80, 90, 100])

# Annual production of wind energy (in Gigawatts)
wind_energy = np.array([12, 18, 25, 30, 35, 45, 58, 75, 85, 95, 110])

# Total energy production from renewable sources
total_energy = solar_energy + wind_energy

# Create a new figure
plt.figure(figsize=(12, 7))

# Plotting Solar Energy Production
plt.plot(years, solar_energy, label='Solar Energy', color='goldenrod', linestyle='--', marker='o', linewidth=2)

# Plotting Wind Energy Production
plt.plot(years, wind_energy, label='Wind Energy', color='skyblue', linestyle='-.', marker='s', linewidth=2)

# Plotting Total Energy Production
plt.plot(years, total_energy, label='Total Renewable Energy', color='green', linestyle='-', marker='d', linewidth=2)

# Title and axis labels
plt.title('Rise of Renewable Energy in Solaria (2010-2020)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Energy Production (Gigawatts)', fontsize=12)

# Adding a legend
plt.legend(title='Energy Source', loc='upper left', fontsize=10, title_fontsize=11)

# Adding grid lines for better visualization
plt.grid(True, linestyle='--', alpha=0.6)

# Set tick parameters for better clarity
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 121, 10))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()