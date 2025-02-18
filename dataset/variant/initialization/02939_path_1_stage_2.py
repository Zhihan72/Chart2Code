import matplotlib.pyplot as plt
import numpy as np

years = np.arange(3050, 3055)
planets = ['Zerion', 'Yutopia', 'Cetheron', 'Luthar']

tritanium_exports = [50, 55, 52, 54, 53]       
dilithium_exports = [20, 22, 23, 25, 24]       
plasmoid_exports = [30, 33, 35, 36, 38]        
quantum_flux_exports = [10, 15, 18, 20, 22]    

colors = ['#FF6347', '#4682B4', '#9ACD32', '#DA70D6']

fig, ax = plt.subplots(figsize=(12, 8))

ax.bar(years, tritanium_exports, label='Tritanium - Cetheron', color=colors[0])
ax.bar(years, dilithium_exports, bottom=tritanium_exports, label='Dilithium - Luthar', color=colors[1])
ax.bar(years, plasmoid_exports, bottom=np.array(tritanium_exports) + np.array(dilithium_exports), label='Plasmoid - Zerion', color=colors[2])
ax.bar(years, quantum_flux_exports, bottom=np.array(tritanium_exports) + np.array(dilithium_exports) + np.array(plasmoid_exports), label='Quantum Flux - Yutopia', color=colors[3])

ax.set_title("Interplanetary Resource Movement\nfor Conclave Worlds", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Cycle Year", fontsize=14)
ax.set_ylabel("Volume Exported (Kilotons)", fontsize=14)

plt.xticks(years, rotation=45)

ax.legend(title='Goods per Source', loc='upper left', bbox_to_anchor=(1, 1))

ax.yaxis.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()

plt.show()