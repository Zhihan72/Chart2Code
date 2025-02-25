import matplotlib.pyplot as plt
import numpy as np

years = np.array([1990, 1995, 2000, 2005, 2010, 2015, 2020])
solar_energy = np.array([5, 10, 25, 50, 90, 200, 350])
wind_energy = np.array([10, 20, 60, 120, 250, 400, 650])
hydro_energy = np.array([500, 520, 550, 580, 600, 630, 650])

fig, ax = plt.subplots(figsize=(12, 8))

# Randomly altering line and marker styles
ax.plot(years, solar_energy, label='Solar', color='orange', linewidth=2.5, linestyle='-', marker='>', markersize=8)
ax.plot(years, wind_energy, label='Wind', color='purple', linewidth=1.5, linestyle='--', marker='*', markersize=10)
ax.plot(years, hydro_energy, label='Hydroelectric', color='green', linewidth=2, linestyle='-.', marker='D', markersize=7)

# Adjusting title and labels
ax.set_title('Renewable Energy Production Trends', fontsize=15, fontweight='bold', pad=15)
ax.set_xlabel('Year', fontsize=13)
ax.set_ylabel('Production (TWh)', fontsize=13)
ax.grid(True, linestyle=':', alpha=0.4)  # Altered grid style
ax.legend(loc='lower right', fontsize=11, title="Source")  # Changed legend location

# Annotate critical points
for year, s, w, h in zip(years, solar_energy, wind_energy, hydro_energy):
    ax.annotate(f'{s}', xy=(year, s), xytext=(year, s+15), textcoords='offset points', ha='center', fontsize=9, color='orange')
    ax.annotate(f'{w}', xy=(year, w), xytext=(year, w+15), textcoords='offset points', ha='center', fontsize=9, color='purple')
    ax.annotate(f'{h}', xy=(year, h), xytext=(year, h+15), textcoords='offset points', ha='center', fontsize=9, color='green')

plt.tight_layout()
plt.show()