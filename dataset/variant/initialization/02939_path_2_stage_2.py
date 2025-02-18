import matplotlib.pyplot as plt
import numpy as np

# Define the years and planet-specific exports
years = np.arange(3050, 3055)
planets = ['Zerion', 'Yutopia', 'Cetheron', 'Luthar', 'Xanadu', 'Hyperion']

# Export data for each commodity (in thousands of tons)
tritanium_exports = [50, 55, 52, 54, 53]
dilithium_exports = [20, 22, 23, 25, 24]
plasmoid_exports = [-30, -33, -35, -36, -38]
quantum_flux_exports = [-10, -15, -18, -20, -22]
neutronium_exports = [40, 42, 45, 46, 48]  # New positive exports
antimatter_exports = [-25, -28, -30, -32, -34]  # New negative exports

colors = ['#4C72B0', '#DD8452', '#55A868', '#C44E52', '#8172B2', '#937860']

# Create diverging bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting each stack, expanding from the central axis
ax.bar(years, tritanium_exports, label='Tritanium - Zerion', color=colors[0])
ax.bar(years, dilithium_exports, bottom=tritanium_exports, label='Dilithium - Yutopia', color=colors[1])
ax.bar(years, plasmoid_exports, label='Plasmoid - Cetheron', color=colors[2], align='center')
ax.bar(years, quantum_flux_exports, bottom=plasmoid_exports, label='Quantum Flux - Luthar', color=colors[3], align='center')
ax.bar(years, neutronium_exports, bottom=[sum(x) for x in zip(tritanium_exports, dilithium_exports)], label='Neutronium - Xanadu', color=colors[4])
ax.bar(years, antimatter_exports, bottom=[sum(x) for x in zip(plasmoid_exports, quantum_flux_exports)], label='Antimatter - Hyperion', color=colors[5], align='center')

ax.set_title("Intergalactic Commodity Exports\nfrom Major Alien Planets (3050-3054)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Export Quantity (Thousands of Tons)", fontsize=14, labelpad=20)

plt.xticks(years, rotation=45)

ax.legend(title='Commodities by Planet', loc='upper left', bbox_to_anchor=(1, 1))

ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.axhline(0, color='black', linewidth=0.8)

plt.tight_layout()
plt.show()