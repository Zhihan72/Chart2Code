import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2030, 2041)
solar_panels_A = np.array([50, 55, 60, 62, 65, 67, 70, 73, 75, 78, 80])
solar_panels_B = np.array([45, 50, 52, 55, 60, 62, 65, 68, 70, 72, 75])
solar_panels_C = np.array([40, 42, 45, 48, 50, 55, 57, 60, 65, 67, 70])

fig, ax = plt.subplots(figsize=(12, 7))

ax.plot(years, solar_panels_A, linestyle='-', marker='o', color='#ff5733', linewidth=2, markersize=6)
ax.plot(years, solar_panels_B, linestyle='--', marker='s', color='#33ff57', linewidth=2, markersize=6)
ax.plot(years, solar_panels_C, linestyle=':', marker='^', color='#3357ff', linewidth=2, markersize=6)

ax.annotate('Milestone 1', xy=(2035, 67), xytext=(2033, 72),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, fontweight='bold')
ax.annotate('Milestone 2', xy=(2040, 67), xytext=(2038, 74),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, fontweight='bold')

ax.set_title('Mars Colony Solar Power Generation:\nProgress Across Different Arrays (2030-2040)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Power Generation (GW)', fontsize=12)

ax.set_xticks(years)
ax.set_yticks(np.arange(40, 85, step=5))

plt.tight_layout()
plt.show()