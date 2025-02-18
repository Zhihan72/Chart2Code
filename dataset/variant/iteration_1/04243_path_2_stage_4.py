import matplotlib.pyplot as plt
import numpy as np

years = np.array([2025, 2030, 2035, 2040, 2045, 2050])
# Shuffle within the data groups while preserving dimension and structure
colony_A_shuffled = np.array([-55, -60, -65, -45, -50, -70])
colony_B_shuffled = np.array([-63, -68, -42, -53, -47, -58])
colony_C_shuffled = np.array([-48, -52, -67, -62, -58, -72])
colony_D_shuffled = np.array([-50, -61, -64, -56, -69, -46])

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, colony_A_shuffled, color='navy', marker='o', linestyle='-', linewidth=2, markersize=10)
ax.plot(years, colony_B_shuffled, color='crimson', marker='s', linestyle='--', linewidth=3, markersize=9)
ax.plot(years, colony_C_shuffled, color='purple', marker='^', linestyle='-.', linewidth=2, markersize=7)
ax.plot(years, colony_D_shuffled, color='chocolate', marker='d', linestyle=':', linewidth=2, markersize=8)

ax.grid(True, linestyle=':', alpha=0.5)

plt.tight_layout()
plt.show()