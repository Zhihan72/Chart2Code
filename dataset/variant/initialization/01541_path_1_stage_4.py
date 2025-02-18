import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

decades = ['1990s', '2000s', '2010s', '2020s']
solar = np.array([5, 20, 100, 250])
wind = np.array([10, 50, 200, 500])
hydroelectric = np.array([200, 250, 300, 350])
biomass = np.array([30, 60, 100, 150])
geothermal = np.array([15, 25, 40, 60])
nuclear = np.array([50, 55, 60, 65])
tide = np.array([2, 4, 6, 8])

data = np.vstack([solar, wind, hydroelectric, biomass, geothermal, nuclear, tide])

colors = ['#d62728', '#9467bd', '#2ca02c', '#ff7f0e', '#1f77b4', '#e377c2', '#8c564b']

plt.figure(figsize=(10, 7))
plt.stackplot(decades, data, colors=colors, alpha=0.85)

plt.xticks(rotation=30, ha='center')
plt.grid(visible=True, which='major', color='blue', linestyle='-', linewidth=0.6, alpha=0.6)

plt.yticks(np.arange(0, 801, 100))
plt.gca().yaxis.set_minor_locator(MultipleLocator(25))
plt.grid(which='minor', linestyle='--', linewidth=0.4, alpha=0.4)

plt.axvspan(1.5, 2.5, color='blue', alpha=0.15)
plt.tight_layout()
plt.show()