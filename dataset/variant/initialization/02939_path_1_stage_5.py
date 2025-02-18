import matplotlib.pyplot as plt
import numpy as np

years = np.arange(3050, 3055)
tritanium_exports = [50, 55, 52, 54, 53]
dilithium_exports = [20, 22, 23, 25, 24]
plasmoid_exports = [30, 33, 35, 36, 38]
quantum_flux_exports = [10, 15, 18, 20, 22]
hyperium_exports = [5, 8, 7, 9, 10]

colors = ['#9ACD32', '#DA70D6', '#FFD700', '#FF6347', '#4682B4']

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.15  # Width of each bar
indices = np.arange(len(years))

# Plot each dataset side by side (grouped)
ax.bar(indices, tritanium_exports, bar_width, label='Tritanium - Cetheron', color=colors[0])
ax.bar(indices + bar_width, dilithium_exports, bar_width, label='Dilithium - Luthar', color=colors[1])
ax.bar(indices + 2 * bar_width, plasmoid_exports, bar_width, label='Plasmoid - Zerion', color=colors[2])
ax.bar(indices + 3 * bar_width, quantum_flux_exports, bar_width, label='Quantum Flux - Yutopia', color=colors[3])
ax.bar(indices + 4 * bar_width, hyperium_exports, bar_width, label='Hyperium - Zephyr', color=colors[4])

ax.set_title("Interplanetary Resource Movement\nfor Conclave Worlds", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Cycle Year", fontsize=14)
ax.set_ylabel("Volume Exported (Kilotons)", fontsize=14)

ax.set_xticks(indices + 2 * bar_width)
ax.set_xticklabels(years, rotation=45)

ax.legend(title='Goods per Source', loc='upper right')

ax.yaxis.grid(True, linestyle=':', alpha=0.7)

plt.tight_layout()
plt.show()