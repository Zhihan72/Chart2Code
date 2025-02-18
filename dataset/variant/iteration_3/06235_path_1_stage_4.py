import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1960, 2021)
co2_levels = [
    317, 318, 319, 321, 320, 322, 323, 325, 324, 326,
    328, 330, 329, 331, 333, 332, 334, 336, 337, 339,
    338, 341, 340, 343, 342, 346, 345, 347, 349, 351,
    350, 354, 356, 355, 358, 360, 362, 364, 368, 366,
    370, 372, 374, 376, 378, 382, 380, 385, 387, 389,
    391, 396, 394, 398, 402, 404, 406, 411, 409, 413,
    418
]

fig, ax = plt.subplots(figsize=(14, 8))
ax.plot(years, co2_levels, color='teal', linestyle='-', marker='o', markersize=5, linewidth=2)

ax.set_title('Mauna Loa CO2 (1960-2020)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('CO2 (ppm)', fontsize=14)

plt.axvline(x=1960, color='grey', linestyle='--', linewidth=1.5, alpha=0.7)
plt.axvline(x=1992, color='grey', linestyle='--', linewidth=1.5, alpha=0.7)
plt.axvline(x=1997, color='grey', linestyle='--', linewidth=1.5, alpha=0.7)
plt.axvline(x=2015, color='grey', linestyle='--', linewidth=1.5, alpha=0.7)
plt.axvline(x=2020, color='grey', linestyle='--', linewidth=1.5, alpha=0.7)

ax.set_xticks(np.arange(1960, 2021, 5))
ax.set_yticks(np.arange(300, 450, 10))
plt.tight_layout()
plt.show()