import matplotlib.pyplot as plt
import numpy as np

years = np.arange(3050, 3055)
planets = ['Zerion', 'Yutopia', 'Cetheron', 'Luthar']

tritanium_exports = [50, 55, 52, 54, 53]       # Zerion
dilithium_exports = [20, 22, 23, 25, 24]       # Yutopia
plasmoid_exports = [30, 33, 35, 36, 38]        # Cetheron
quantum_flux_exports = [10, 15, 18, 20, 22]    # Luthar

# New colors for the stacked bars
colors = ['#FF6347', '#4682B4', '#9ACD32', '#DA70D6']

fig, ax = plt.subplots(figsize=(12, 8))

ax.bar(years, tritanium_exports, label='Tritanium - Zerion', color=colors[0])
ax.bar(years, dilithium_exports, bottom=tritanium_exports, label='Dilithium - Yutopia', color=colors[1])
ax.bar(years, plasmoid_exports, bottom=np.array(tritanium_exports) + np.array(dilithium_exports), label='Plasmoid - Cetheron', color=colors[2])
ax.bar(years, quantum_flux_exports, bottom=np.array(tritanium_exports) + np.array(dilithium_exports) + np.array(plasmoid_exports), label='Quantum Flux - Luthar', color=colors[3])

ax.set_title("Intergalactic Commodity Exports\nfrom Major Alien Planets (3050-3054)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Export Quantity (Thousands of Tons)", fontsize=14)

plt.xticks(years, rotation=45)

ax.legend(title='Commodities by Planet', loc='upper left', bbox_to_anchor=(1, 1))

ax.yaxis.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()

plt.show()