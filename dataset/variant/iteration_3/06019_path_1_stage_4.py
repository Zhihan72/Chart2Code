import matplotlib.pyplot as plt
import numpy as np

decades = np.array([1980, 1990, 2000, 2010, 2020])
single_core_mips = np.array([1, 10, 100, 1000, 8000])
multi_core_mips = np.array([0, 0, 100, 3000, 15000])
gpu_acceleration_mips = np.array([0, 0, 0, 5000, 20000])
cloud_computing_mips = np.array([0, 0, 0, 0, 30000])
quantum_computing_mips = np.array([0, 0, 0, 0, 5000])

colors = ['#87CEEB' for _ in range(5)] 

fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(decades, single_core_mips, multi_core_mips, gpu_acceleration_mips, cloud_computing_mips, quantum_computing_mips,
             colors=colors, 
             alpha=0.8)

# Randomly altered textual elements
ax.set_title('Comp. Power Trends\n(1980-2020)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year Mark', fontsize=12)
ax.set_ylabel('MIPS Power', fontsize=12)

ax.set_xticks(decades)
ax.set_xticklabels([f"Era {decade}" for decade in decades], fontsize=10)

plt.tight_layout()
plt.show()