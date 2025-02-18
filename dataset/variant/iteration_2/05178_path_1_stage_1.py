import matplotlib.pyplot as plt
import numpy as np

# Data: Yearly energy production (in Terawatt-hours) for Solar, Wind, Hydroelectric, and Geothermal
years = np.array([1990, 1995, 2000, 2005, 2010, 2015, 2020])
solar_energy = np.array([5, 10, 25, 50, 90, 200, 350])
wind_energy = np.array([10, 20, 60, 120, 250, 400, 650])
hydro_energy = np.array([500, 520, 550, 580, 600, 630, 650])
geothermal_energy = np.array([15, 30, 45, 60, 80, 100, 120])  # Hypothetical data for Geothermal energy

fig, ax = plt.subplots(figsize=(12, 8))

# Plot all lines
ax.plot(years, solar_energy, label='Solar Energy', color='orange', linewidth=2, marker='o', markersize=6)
ax.plot(years, wind_energy, label='Wind Energy', color='blue', linewidth=2, marker='^', markersize=6)
ax.plot(years, hydro_energy, label='Hydroelectric Energy', color='green', linewidth=2, marker='s', markersize=6)
ax.plot(years, geothermal_energy, label='Geothermal Energy', color='red', linewidth=2, marker='d', markersize=6)  # New line for Geothermal energy

# Adding Chart Title and Labels
ax.set_title('Global Renewable Energy Production Over Time', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Production (Terawatt-hours)', fontsize=14)
ax.grid(True, linestyle='--', alpha=0.6)

# Adding Legend
ax.legend(loc='upper left', fontsize=12, title="Energy Source")

# Annotate critical points
for year, s, w, h, g in zip(years, solar_energy, wind_energy, hydro_energy, geothermal_energy):
    ax.annotate(f'{s}', xy=(year, s), xytext=(year, s+20), textcoords='offset points', ha='center', fontsize=10, color='orange')
    ax.annotate(f'{w}', xy=(year, w), xytext=(year, w+20), textcoords='offset points', ha='center', fontsize=10, color='blue')
    ax.annotate(f'{h}', xy=(year, h), xytext=(year, h+20), textcoords='offset points', ha='center', fontsize=10, color='green')
    ax.annotate(f'{g}', xy=(year, g), xytext=(year, g+20), textcoords='offset points', ha='center', fontsize=10, color='red')  # Annotate for Geothermal

# Automatically adjust plot to avoid overlapping elements
plt.tight_layout()

# Display the plot
plt.show()