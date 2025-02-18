import matplotlib.pyplot as plt
import numpy as np

decades = np.array([1980, 1990, 2000, 2010, 2020])
single_core_mips = np.array([1, 10, 100, 1000, 8000])
multi_core_mips = np.array([0, 0, 100, 3000, 15000])
gpu_acceleration_mips = np.array([0, 0, 0, 5000, 20000])
cloud_computing_mips = np.array([0, 0, 0, 0, 30000])
quantum_computing_mips = np.array([0, 0, 0, 0, 5000])

# Define a list of colors for each data group
colors = ['#87CEEB' for _ in range(5)]  # Light sky blue, tomato, lime green, gold, blueviolet

fig, ax = plt.subplots(figsize=(12, 8))

# Use the colors list to apply colors to each area in the stackplot
ax.stackplot(decades, single_core_mips, multi_core_mips, gpu_acceleration_mips, cloud_computing_mips, quantum_computing_mips,
             colors=colors,  # Now we're passing a list of colors
             alpha=0.8)

ax.set_title('Evolution of Personal Computer Computing Power\n(1980-2020)', fontsize=16, fontweight='bold')
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Computing Power (MIPS)', fontsize=12)

ax.set_xticks(decades)
ax.set_xticklabels([f"{decade}s" for decade in decades], fontsize=10)

plt.tight_layout()
plt.show()
