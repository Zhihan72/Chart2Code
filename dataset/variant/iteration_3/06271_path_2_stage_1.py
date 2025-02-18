import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2010, 2031)

# Data representing GWh production for each renewable energy source over the years
solar_energy = [10, 15, 20, 28, 40, 55, 72, 90, 112, 140, 175, 215, 260, 310, 365, 430, 500, 580, 670, 770, 880]
wind_energy = [30, 40, 50, 65, 85, 110, 140, 175, 215, 260, 310, 370, 430, 500, 580, 670, 770, 880, 1000, 1140, 1300]
hydro_energy = [220, 230, 240, 250, 260, 270, 280, 290, 295, 300, 305, 310, 315, 320, 323, 325, 328, 330, 335, 340, 345]
geothermal_energy = [15, 17, 20, 24, 29, 35, 42, 50, 60, 72, 86, 102, 120, 140, 162, 185, 210, 240, 270, 305, 340]

# Stack the data for area plotting
data = np.array([solar_energy, wind_energy, hydro_energy, geothermal_energy])

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, data, labels=['Sunny', 'Breezy', 'Wet', 'Hot Earth'],
             colors=['#ffcc00', '#66c2a5', '#8da0cb', '#fc8d62'], alpha=0.8)

# Title and axis labels
ax.set_title('Eco-Power Surge (2010-2030)', fontsize=16, fontweight='bold')
ax.set_xlabel('Timeline', fontsize=14)
ax.set_ylabel('Output (GWh)', fontsize=14)

# Add legend
ax.legend(title='Source of Power', loc='upper left', fontsize=12)

# Configure x and y ticks
ax.set_xticks(np.arange(2010, 2031, 2))
ax.set_yticks(np.arange(0, 1401, 200))
ax.set_xlim(2010, 2030)
ax.set_ylim(0, 1400)

# Add gridlines for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Add a secondary line plot indicating the total renewable energy production
total_production = np.sum(data, axis=0)
ax2 = ax.twinx()
ax2.plot(years, total_production, 'o--', color='#2c3e50', label='Overall Output')
ax2.set_ylabel('Total Output (GWh)', fontsize=12, color='#2c3e50')
ax2.tick_params(axis='y', colors='#2c3e50')

# Consolidate legends
lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines + lines2, labels + labels2, loc='upper left', title='Power Statistics')

# Enhance layout to avoid overlapping elements
plt.tight_layout()

# Show plot
plt.show()