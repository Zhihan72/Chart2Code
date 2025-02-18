import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)
co2_emissions = [300, 310, 320, 330, 340, 335, 325, 315, 310, 305, 295, 280, 270, 260, 250, 240, 235, 229, 225, 220, 210]
renewable_energy = [5, 6, 8, 10, 13, 18, 20, 25, 30, 35, 42, 50, 60, 70, 85, 100, 120, 145, 170, 200, 230]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12), sharex=True)

ax1.plot(years, renewable_energy, color='green', linewidth=2, marker='s', linestyle='-', markersize=6)
ax1.grid(True, linestyle='--', alpha=0.5)

ax2.plot(years, co2_emissions, color='red', linewidth=2, marker='o', linestyle='-', markersize=6)
ax2.grid(True, linestyle='--', alpha=0.5)

plt.xticks(years, rotation=45)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()