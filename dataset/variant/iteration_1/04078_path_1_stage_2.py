import matplotlib.pyplot as plt
import numpy as np

decades = np.array([1970, 1980, 1990, 2000, 2010, 2020])

co2_emissions = np.array([7000, 9000, 11000, 13000, 15000, 16000])
ch4_emissions = np.array([1500, 1700, 1800, 1900, 2000, 2100])
n2o_emissions = np.array([300, 350, 400, 450, 500, 550])
fgases_emissions = np.array([50, 100, 150, 200, 250, 300])

emissions_data = np.vstack([co2_emissions, ch4_emissions, n2o_emissions, fgases_emissions])

colors = ['#d95f02', '#e7298a', '#1b9e77', '#7570b3']

fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(decades, emissions_data, colors=colors, alpha=0.85)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_xticks(decades)
ax.set_xticklabels(decades, rotation=45)
plt.tight_layout()
plt.show()