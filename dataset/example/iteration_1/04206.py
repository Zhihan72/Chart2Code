import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart shows the projected growth of various clean energy sources from 2020 to 2030.
# The data represents fictional estimates of solar, wind, hydro, and geothermal energy.
years = np.arange(2020, 2031)

# Artificial data for clean energy sources across years
solar_energy = [10, 20, 30, 45, 55, 70, 85, 100, 115, 130, 150]
wind_energy = [15, 25, 35, 45, 60, 75, 90, 105, 120, 140, 160]
hydro_energy = [20, 30, 40, 55, 65, 80, 95, 110, 130, 150, 170]
geothermal_energy = [5, 10, 15, 25, 35, 45, 60, 75, 90, 110, 130]

# Colors for the energy sources
colors = ['#FFD700', '#1E90FF', '#32CD32', '#FF6347']

# Initialize the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Create the stacked area chart
ax.stackplot(years, solar_energy, wind_energy, hydro_energy, geothermal_energy, 
             labels=['Solar Energy', 'Wind Energy', 'Hydro Energy', 'Geothermal Energy'],
             colors=colors, alpha=0.8)

# Add title and labels
ax.set_title('Projection of Clean Energy Growth (2020-2030)', fontsize=16, fontweight='bold', ha='center')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Output (Gigawatts)', fontsize=14)

# Customize x-axis
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Add legend
ax.legend(loc='upper left', fontsize=12, title='Energy Sources', frameon=False)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Highlight significant trends with annotations
ax.annotate('Rapid Growth in Solar Energy', xy=(2025, 70), xytext=(2023, 110),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=12, color='black')

ax.annotate('Increase in Geothermal Energy', xy=(2028, 85), xytext=(2026, 130),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=12, color='black')

# Adjust layout to ensure no overlap
plt.tight_layout()

# Display the plot
plt.show()