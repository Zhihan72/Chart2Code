import matplotlib.pyplot as plt
import numpy as np

years = np.array([2025, 2030, 2035, 2040, 2045, 2050])
colony_A = np.array([-70, -65, -60, -55, -50, -45])
colony_B = np.array([-68, -63, -58, -53, -47, -42])
colony_C = np.array([-72, -67, -62, -58, -52, -48])
colony_D = np.array([-69, -64, -61, -56, -50, -46])

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, colony_A, color='navy', marker='x', linestyle=':', linewidth=2, markersize=10)
ax.plot(years, colony_B, color='crimson', marker='v', linestyle='--', linewidth=3, markersize=9)
ax.plot(years, colony_C, color='purple', marker='p', linestyle='-.', linewidth=2, markersize=7)
ax.plot(years, colony_D, color='chocolate', marker='h', linestyle='-', linewidth=2, markersize=8)

ax.grid(True, linestyle=':', alpha=0.5)

plt.tight_layout()
plt.show()