import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1960, 2021)
co2_levels = [
    316, 317, 318, 319, 320, 321, 322, 323, 325, 326,
    327, 329, 330, 331, 332, 333, 335, 336, 337, 338,
    339, 340, 341, 342, 344, 345, 347, 348, 350, 351,
    353, 355, 356, 358, 359, 361, 363, 365, 367, 369,
    371, 373, 375, 377, 379, 381, 384, 386, 388, 390,
    392, 395, 397, 400, 403, 405, 407, 410, 412, 415,
    417
]

fig, ax = plt.subplots(figsize=(14, 8))
ax.plot(years, co2_levels, color='darkred', linestyle='-', marker='o', markersize=5, linewidth=2)

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