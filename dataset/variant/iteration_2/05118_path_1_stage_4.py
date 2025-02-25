import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)
solar = np.array([33, 18, 27, 67, 14, 48, 78, 10, 40, 22, 57])
wind = np.array([22, 51, 31, 78, 59, 18, 68, 44, 26, 37, 15])
hydro = np.array([25, 22, 29, 21, 20, 27, 30, 28, 26, 23, 24])
geo = np.array([18, 25, 5, 22, 20, 8, 12, 6, 14, 10, 16])

data = np.vstack([solar, wind, hydro, geo])

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, data, colors=['#e57373', '#ba68c8', '#7986cb', '#64b5f6'], alpha=0.8)

ax.set_title('Renewable Energy (2020-2030)', fontsize=15, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy (TWh)', fontsize=12)

ax.set_xticks(years)
ax.set_yticks(np.arange(0, 221, 20))

plt.tight_layout()
plt.show()