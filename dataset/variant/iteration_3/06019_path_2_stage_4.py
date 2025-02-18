import matplotlib.pyplot as plt
import numpy as np

decades = np.array([1980, 1990, 2000, 2010, 2020])

single_core_mips = np.array([1, 10, 100, 1000, 8000])
multi_core_mips = np.array([0, 0, 100, 3000, 15000])
gpu_acceleration_mips = np.array([0, 0, 0, 5000, 20000])
cloud_computing_mips = np.array([0, 0, 0, 0, 30000])
quantum_computing_mips = np.array([0, 0, 0, 0, 5000])
biocomputing_mips = np.array([0, 0, 0, 0, 2000])

fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(decades, 
             single_core_mips, 
             multi_core_mips, 
             gpu_acceleration_mips, 
             cloud_computing_mips,
             quantum_computing_mips,
             biocomputing_mips,
             labels=['Solo-chip Processors', 
                     'Multiple-core Processing Units', 
                     'Graphical Processing Boost', 
                     'Remote Computing',
                     'Quantum Computing',
                     'Biocomputing'],
             colors=['#FF6347', '#6A5ACD', '#32CD32', '#8A2BE2', '#FFD700', '#4682B4'],
             alpha=0.9)

ax.set_title('Transformation of Computing Capabilities\n(1980-2020)', fontsize=16, fontweight='bold')
ax.set_xlabel('Era', fontsize=12)
ax.legend(loc='upper right', title='Innovations', fontsize=10)
ax.set_xticks(decades)
ax.set_xticklabels([f"{decade}s" for decade in decades], fontsize=11)
ax.grid(True, linestyle='-.', alpha=0.6)
fig.patch.set_linewidth(2)
fig.patch.set_edgecolor('gray')
plt.tight_layout()

plt.show()