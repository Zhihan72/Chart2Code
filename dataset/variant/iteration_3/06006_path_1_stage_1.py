import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
years = np.arange(2010, 2031)
solar_growth = [1, 2, 3, 5, 7, 10, 14, 19, 25, 30, 35, 40, 45, 48, 52, 56, 60, 65, 70, 75, 80]
wind_growth = [2, 3, 5, 8, 11, 15, 20, 25, 30, 36, 42, 49, 55, 61, 68, 75, 82, 90, 97, 104, 110]
hydro_growth = [5, 6, 7, 8, 10, 12, 15, 18, 22, 26, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]

plt.figure(figsize=(14, 8))

# Plot lines with manually altered labels
plt.plot(years, solar_growth, label='Sun Energy', color='#FFA500', marker='o', linewidth=2, linestyle='-')
plt.plot(years, wind_growth, label='Breeze Power', color='#1E90FF', marker='^', linewidth=2, linestyle='--')
plt.plot(years, hydro_growth, label='Water Force', color='#00FF00', marker='s', linewidth=2, linestyle='-.')

# Manually altered title and labels
plt.title('Renewable Sources Expansion (2010-2030)', fontsize=16, fontweight='bold')
plt.xlabel('Timeline', fontsize=14)
plt.ylabel('Yearly Increase (%)', fontsize=14)

# Manually altered annotations
plt.annotate('Big Jump\nin Solar', xy=(2015, 10), xytext=(2012, 15),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
plt.annotate('Gradual Rise\nin Wind Power', xy=(2020, 36), xytext=(2016, 60),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
plt.annotate('Stable Growth\nin Hydro', xy=(2025, 65), xytext=(2020, 80),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Customize legend
plt.legend(loc='upper left', title='Type of Energy', fontsize=12, frameon=True)

# Customize grid and ticks
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(years[::2], rotation=45)
plt.yticks(np.arange(0, 121, 10))

# Adjust layout to avoid overlap
plt.tight_layout()

# Show plot
plt.show()