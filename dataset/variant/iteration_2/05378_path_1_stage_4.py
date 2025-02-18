import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2011, 2021)

# We will manually alter the group labels and textual elements.
green_space = {
    'Eco Haven': np.array([50, 55, 60, 70, 75, 80, 85, 90, 95, 100]),
    'Nature Nook': np.array([40, 45, 50, 55, 60, 65, 70, 75, 80, 85]),
    'Verdant Ville': np.array([30, 35, 40, 50, 55, 60, 65, 70, 75, 80]),
    'Botanic Borough': np.array([20, 25, 35, 45, 60, 65, 70, 75, 80, 85])
}

colors = ['#99ccff', '#ffa07a', '#d3d3d3', '#66cdaa']

plt.figure(figsize=(12, 8))
plt.stackplot(years, green_space.values(), labels=green_space.keys(), colors=colors, alpha=0.6)

# Altering the title and axes labels
plt.title('Greenery Expansion Over Time (2011-2020)', fontsize=18, weight='normal', pad=15)
plt.xlabel('Timeline', fontsize=13)
plt.ylabel('Vegetation Coverage (Sq Km)', fontsize=13)
plt.xticks(years, rotation=30)
plt.grid(False)
plt.tick_params(axis='both', which='major', labelsize=11)
plt.legend(title='Zones', title_fontsize=11, fontsize=9, loc='lower right', frameon=True)
plt.tight_layout()
plt.show()