import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

decades = ['1990s', '2000s', '2010s', '2020s']
solar = np.array([5, 20, 100, 250])
wind = np.array([10, 50, 200, 500])
hydroelectric = np.array([200, 250, 300, 350])
biomass = np.array([30, 60, 100, 150])
geothermal = np.array([15, 25, 40, 60])

data = np.vstack([solar, wind, hydroelectric, biomass, geothermal])

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

plt.figure(figsize=(14, 9))
plt.stackplot(decades, data, colors=colors, alpha=0.8)

plt.xticks(rotation=45, ha='right')
plt.grid(visible=True, which='both', color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

plt.yticks(np.arange(0, 601, 100))
plt.gca().yaxis.set_minor_locator(MultipleLocator(50))
plt.grid(which='minor', linestyle=':', linewidth=0.5)

plt.axvspan(2.5, 3.5, color='grey', alpha=0.1)
plt.tight_layout()
plt.show()