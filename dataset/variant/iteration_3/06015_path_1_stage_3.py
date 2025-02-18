import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2030, 2041)
solar_panels_A = np.array([50, 55, 60, 62, 65, 67, 70, 73, 75, 78, 80])
solar_panels_B = np.array([45, 50, 52, 55, 60, 62, 65, 68, 70, 72, 75])
solar_panels_C = np.array([40, 42, 45, 48, 50, 55, 57, 60, 65, 67, 70])
solar_panels_D = np.array([35, 40, 43, 47, 50, 54, 58, 61, 64, 68, 72])

fig, ax = plt.subplots(figsize=(12, 7))

ax.plot(years, solar_panels_A, linestyle='-', marker='o', color='#ff5733', linewidth=2, markersize=6)
ax.plot(years, solar_panels_B, linestyle='--', marker='s', color='#33ff57', linewidth=2, markersize=6)
ax.plot(years, solar_panels_C, linestyle=':', marker='^', color='#3357ff', linewidth=2, markersize=6)
ax.plot(years, solar_panels_D, linestyle='-.', marker='d', color='#ff33ab', linewidth=2, markersize=6)

ax.set_xticks(years)
ax.set_yticks(np.arange(35, 85, step=5))

plt.tight_layout()
plt.show()