import matplotlib.pyplot as plt
import numpy as np

# Define the years of interest with a higher resolution (quarterly)
years = np.arange(2000, 2041, 0.25)

# Artificial data for different energy sources (in gigawatts) with more complexity
solar_energy = np.interp(years, np.arange(2000, 2041), np.linspace(2, 650, 41)) + 10 * np.sin(np.linspace(0, 8 * np.pi, len(years)))
wind_energy = solar_energy + np.interp(years, np.arange(2000, 2041), np.linspace(1, 490, 41)) + 15 * np.cos(np.linspace(0, 6 * np.pi, len(years)))
hydro_energy = wind_energy + np.interp(years, np.arange(2000, 2041), np.linspace(15, 600, 41)) + 20 * np.sin(np.linspace(0, 4 * np.pi, len(years)))

# Plot the stacked area chart
fig, ax = plt.subplots(figsize=(16, 10))

ax.fill_between(years, solar_energy, label='Solar Energy', color='gold', alpha=0.8)
ax.fill_between(years, solar_energy, wind_energy, label='Wind Energy', color='skyblue', alpha=0.8)
ax.fill_between(years, wind_energy, hydro_energy, label='Hydro Energy', color='lightgreen', alpha=0.8)

# Title and labels
ax.set_title('Global Renewable Energy Production (2000-2040):\nA Simplified Look at Energy Transition', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Production (Gigawatts)', fontsize=12)

# Customize x-axis ticks
ax.set_xticks(years[::8])  # Show every second year
ax.set_xticklabels([str(int(year)) if i % 4 == 0 else '' for i, year in enumerate(years[::8])], rotation=45, ha='right')

# Grid for readability
ax.grid(linestyle='--', alpha=0.5)

# Legend
ax.legend(loc='upper left', fontsize=10)

# Cumulative Total Line Plot
ax.plot(years, hydro_energy, label='Total Energy Production', color='black', linestyle='--', linewidth=2)

# Layout adjustment
plt.tight_layout()

# Display the plot
plt.show()