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
ax.plot(years, co2_levels, color='darkred', linestyle='-', marker='o', markersize=5, linewidth=2, label='CO2')

ax.set_title('Mauna Loa CO2 (1960-2020)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('CO2 (ppm)', fontsize=14)

ax.legend(loc='upper left', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.6)

milestones = {
    1960: 'Start',
    1992: 'Earth Summit',
    1997: 'Kyoto',
    2015: 'Paris',
    2020: 'Recent'
}

for year, event in milestones.items():
    plt.axvline(x=year, color='grey', linestyle='--', linewidth=1.5, alpha=0.7)
    plt.text(year + 0.5, co2_levels[years.tolist().index(year)] + 3, event, rotation=90, verticalalignment='center', fontsize=10, color='grey', alpha=0.7)

ax.set_xticks(np.arange(1960, 2021, 5))
ax.set_yticks(np.arange(300, 450, 10))
plt.tight_layout()
plt.show()