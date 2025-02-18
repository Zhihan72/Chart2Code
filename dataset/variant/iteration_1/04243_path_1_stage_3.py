import matplotlib.pyplot as plt
import numpy as np

years = np.array([2025, 2030, 2035, 2040, 2045, 2050])
colony_A = np.array([-70, -65, -60, -55, -50, -45])
colony_B = np.array([-68, -63, -58, -53, -47, -42])
colony_C = np.array([-72, -67, -62, -58, -52, -48])
colony_D = np.array([-69, -64, -61, -56, -50, -46])
colony_E = np.array([-71, -66, -59, -54, -48, -43])
colony_F = np.array([-73, -69, -63, -57, -51, -47])

fig, ax = plt.subplots(figsize=(14, 8))

# Use a consistent color 'steelblue' for all plots
ax.plot(years, colony_A, label='A', color='steelblue', marker='o', linestyle='-', linewidth=2, markersize=8)
ax.plot(years, colony_B, label='B', color='steelblue', marker='s', linestyle='-', linewidth=2, markersize=8)
ax.plot(years, colony_C, label='C', color='steelblue', marker='^', linestyle='-', linewidth=2, markersize=8)
ax.plot(years, colony_D, label='D', color='steelblue', marker='D', linestyle='-', linewidth=2, markersize=8)
ax.plot(years, colony_E, label='E', color='steelblue', marker='x', linestyle='-', linewidth=2, markersize=8)
ax.plot(years, colony_F, label='F', color='steelblue', marker='*', linestyle='-', linewidth=2, markersize=8)

ax.set_title("Temp Change in Colonies (2025-50)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Yr", fontsize=14)
ax.set_ylabel("Temp (°C)", fontsize=14)

ax.legend(title="Colonies", fontsize=12, title_fontsize=14, loc='lower left')
ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()