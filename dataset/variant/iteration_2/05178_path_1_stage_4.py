import matplotlib.pyplot as plt
import numpy as np

years = np.array([1990, 1995, 2000, 2005, 2010, 2015, 2020])
solar_energy = np.array([5, 10, 25, 50, 90, 200, 350])
wind_energy = np.array([10, 20, 60, 120, 250, 400, 650])
hydro_energy = np.array([500, 520, 550, 580, 600, 630, 650])
geothermal_energy = np.array([15, 30, 45, 60, 80, 100, 120])

fig, ax = plt.subplots(figsize=(12, 8))

# Alter styles among different energy types
ax.plot(years, solar_energy, label='Solar', color='purple', linestyle='-.', linewidth=1.5, marker='v', markersize=8)
ax.plot(years, wind_energy, label='Wind', color='blue', linestyle='-', linewidth=1, marker='x', markersize=10)
ax.plot(years, hydro_energy, label='Hydro', color='green', linestyle='--', linewidth=2.5, marker='o', markersize=6)
ax.plot(years, geothermal_energy, label='Geothermal', color='black', linestyle=':', linewidth=1.2, marker='*', markersize=9)

ax.set_title('Renewable Energy (1990-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy (TWh)', fontsize=14)
ax.grid(True, linestyle='-', alpha=0.4)  # Changed grid style

ax.legend(loc='lower right', fontsize=10, title="Energy Type")  # Adjusted legend

# Update annotations with new colors
for year, s, w, h, g in zip(years, solar_energy, wind_energy, hydro_energy, geothermal_energy):
    ax.annotate(f'{s}', xy=(year, s), xytext=(year, s+20), textcoords='offset points', ha='center', fontsize=9, color='purple')
    ax.annotate(f'{w}', xy=(year, w), xytext=(year, w+20), textcoords='offset points', ha='center', fontsize=9, color='blue')
    ax.annotate(f'{h}', xy=(year, h), xytext=(year, h+20), textcoords='offset points', ha='center', fontsize=9, color='green')
    ax.annotate(f'{g}', xy=(year, g), xytext=(year, g+20), textcoords='offset points', ha='center', fontsize=9, color='black')

plt.tight_layout()
plt.show()