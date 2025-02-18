import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2031)
solar = np.array([3, 4, 6, 8, 6, 10, 12, 15, 21, 24, 18, 28, 32, 40, 36, 45, 50, 65, 60, 70, 55])
wind = np.array([7, 5, 6, 10, 8, 12, 14, 15, 18, 16, 20, 22, 25, 28, 30, 34, 32, 36, 38, 40, 39])
hydro = np.array([10, 12, 10, 11, 13, 15, 14, 16, 18, 17, 20, 23, 22, 24, 25, 26, 25, 28, 27, 30, 29])
nuclear = np.array([18, 20, 17, 15, 16, 14, 14, 12, 13, 11, 12, 10, 10, 9, 10, 8, 8, 7, 7, 5, 6])
fossil = 100 - (solar + wind + hydro + nuclear)

fig, ax = plt.subplots(figsize=(14, 8))

# Apply different colors to each section in the stackplot
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#B3B3CC']
ax.stackplot(years, solar, wind, hydro, nuclear, fossil, 
             labels=['Solar', 'Wind', 'Hydro', 'Nuclear', 'Fossil Fuels'],
             colors=colors,
             alpha=0.8)

ax.set_title('Transition in Global Energy Consumption (2010-2030)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Percentage of Total Energy Consumption (%)', fontsize=14)

# Randomly alter legend location and size, and remove the title
ax.legend(loc='lower right', fontsize=10)

# Apply a different grid style with a different line width and alpha
ax.grid(True, linestyle=':', linewidth=1.0, alpha=0.5)

# Apply randomly chosen xticks rotation
plt.xticks(years, rotation=90)
plt.tight_layout()

plt.show()