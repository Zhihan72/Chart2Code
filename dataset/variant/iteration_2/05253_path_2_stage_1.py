import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2000, 2021)
solar_energy = [0.5, 0.8, 1.2, 1.8, 2.5, 3.1, 4.0, 5.2, 6.1, 7.3, 9.0, 10.4, 12.1, 14.5, 16.8, 19.0, 21.5, 24.7, 27.9, 30.5, 34.0]
wind_energy = [2.1, 2.5, 3.0, 4.0, 5.5, 7.0, 9.2, 12.0, 14.5, 17.9, 21.2, 25.4, 30.2, 35.0, 40.5, 46.0, 52.7, 59.5, 67.3, 75.8, 84.3]
hydro_energy = [10.0, 10.5, 11.0, 11.8, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 16.0, 17.0, 17.5, 18.0, 18.5, 19.0, 19.8, 20.5, 21.0, 22.0, 23.0]

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting the data
ax.plot(years, solar_energy, color='orange', marker='o', linestyle='-', linewidth=2, label='Solar')
ax.plot(years, wind_energy, color='blue', marker='^', linestyle='-', linewidth=2, label='Wind')
ax.plot(years, hydro_energy, color='green', marker='s', linestyle='-', linewidth=2, label='Hydro')

# Shortened title and labels
ax.set_title('Renewable Energy (2000-20)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12, labelpad=10)
ax.set_ylabel('Production (GW)', fontsize=12, labelpad=10)

# Grid and ticks
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
ax.set_xticks(years, minor=False)
ax.set_xticklabels(years, rotation=45)
ax.set_yticks(np.arange(0, 101, 10))

# Legend
ax.legend(loc='upper left', fontsize=12, title='Source')

# Annotations
ax.annotate('Solar Breakthrough', xy=(2008, 6.1), xytext=(2004, 10), 
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkred')
ax.annotate('Wind Boosts', xy=(2011, 25.4), xytext=(2006, 45), 
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkblue')
ax.annotate('Hydro Expansion', xy=(2018, 21.0), xytext=(2014, 35), 
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkgreen')

# Layout
plt.tight_layout()

# Show the plot
plt.show()