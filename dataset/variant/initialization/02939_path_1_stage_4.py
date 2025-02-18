import matplotlib.pyplot as plt
import numpy as np

years = np.arange(3050, 3055)
tritanium_exports = [50, 55, 52, 54, 53]
dilithium_exports = [20, 22, 23, 25, 24]
plasmoid_exports = [30, 33, 35, 36, 38]
quantum_flux_exports = [10, 15, 18, 20, 22]
hyperium_exports = [5, 8, 7, 9, 10]

colors = ['#9ACD32', '#DA70D6', '#FFD700', '#FF6347', '#4682B4']
markers = ['o', '+', '-', 'O', 'X']
line_styles = ['-', '--', '-.', ':', '-']
edge_colors = ['black', 'gray', 'darkred', 'brown', 'darkgray']

fig, ax = plt.subplots(figsize=(12, 8))

# Randomized elements: color, marker, line style for bars
ax.bar(years, tritanium_exports, label='Tritanium - Cetheron', color=colors[0], edgecolor=edge_colors[0])
ax.bar(years, dilithium_exports, bottom=tritanium_exports, label='Dilithium - Luthar', color=colors[1], edgecolor=edge_colors[1])
ax.bar(years, plasmoid_exports, bottom=np.array(tritanium_exports) + np.array(dilithium_exports), label='Plasmoid - Zerion', color=colors[2], edgecolor=edge_colors[2])
ax.bar(years, quantum_flux_exports, bottom=np.array(tritanium_exports) + np.array(dilithium_exports) + np.array(plasmoid_exports), label='Quantum Flux - Yutopia', color=colors[3], edgecolor=edge_colors[3])
ax.bar(years, hyperium_exports, bottom=np.array(tritanium_exports) + np.array(dilithium_exports) + np.array(plasmoid_exports) + np.array(quantum_flux_exports), label='Hyperium - Zephyr', color=colors[4], edgecolor=edge_colors[4])

ax.set_title("Interplanetary Resource Movement\nfor Conclave Worlds", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Cycle Year", fontsize=14)
ax.set_ylabel("Volume Exported (Kilotons)", fontsize=14)

plt.xticks(years, rotation=45)

# Modify legend to use markers
handles, labels = ax.get_legend_handles_labels()
for i in range(len(handles)):
    handles[i] = mpatches.PathPatch(handles[i]) # Use markers as hatches for differentiation
    handles[i].set(hatch=markers[i])
    

ax.legend(handles, labels, title='Goods per Source', loc='upper right')

ax.yaxis.grid(True, linestyle=line_styles[3], alpha=0.7)  # Change grid line style

plt.tight_layout()

plt.show()