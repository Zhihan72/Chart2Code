import matplotlib.pyplot as plt
import numpy as np

years = np.array([2025, 2030, 2035, 2040, 2045, 2050])
colony_A = np.array([-70, -65, -60, -55, -50, -45])
colony_B = np.array([-68, -63, -58, -53, -47, -42])
colony_C = np.array([-72, -67, -62, -58, -52, -48])
colony_D = np.array([-69, -64, -61, -56, -50, -46])

fig, ax = plt.subplots(figsize=(14, 8))

# Plot for Colony A
ax.plot(years, colony_A, label='Colony A', color='navy', marker='x', linestyle=':', linewidth=2, markersize=10)

# Plot for Colony B
ax.plot(years, colony_B, label='Colony B', color='crimson', marker='v', linestyle='--', linewidth=3, markersize=9)

# Plot for Colony C
ax.plot(years, colony_C, label='Colony C', color='purple', marker='p', linestyle='-.', linewidth=2, markersize=7)

# Plot for Colony D
ax.plot(years, colony_D, label='Colony D', color='chocolate', marker='h', linestyle='-', linewidth=2, markersize=8)

ax.set_title("Average Temperature Evolution in Martian Colonies (2025-2050)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Temperature (°C)", fontsize=14)

# Adding legend with a different location and no title
ax.legend(fontsize=10, loc='upper right')

# Adding a different style of grid
ax.grid(True, linestyle=':', alpha=0.5)

plt.tight_layout()
plt.show()