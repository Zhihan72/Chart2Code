import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)
per_capita_emissions = [
    co2 / pop for co2, pop in zip(
        [27.5, 28.2, 28.9, 29.5, 30.1, 30.8, 31.5, 32.0, 32.6, 33.2, 33.9, 34.5, 35.1, 35.8, 36.4, 37.0, 37.6, 38.2, 38.9, 39.5, 40.1],
        [6112.8, 6235.1, 6364.7, 6493.4, 6622.4, 6751.2, 6880.1, 7009.1, 7138.2, 7267.4, 7396.8, 7526.2, 7655.8, 7785.6, 7915.4, 8045.4, 8175.5, 8305.7, 8436.0, 8566.4, 8697.0]
    )
]
renewable_energy_adoption = [4.0, 4.2, 4.5, 4.7, 5.0, 5.4, 5.9, 6.5, 7.1, 7.8, 8.6, 9.5, 10.5, 11.6, 12.8, 14.1, 15.5, 17.0, 18.6, 20.3, 22.1]
co2_levels = [369, 371, 373, 376, 379, 382, 384, 387, 390, 392, 394, 397, 400, 403, 405, 407, 410, 412, 414, 416, 418]
global_temps = [14.3, 14.4, 14.2, 14.5, 14.6, 14.7, 14.5, 14.8, 14.9, 15.0, 14.9, 15.1, 15.2, 15.3, 15.4, 15.5, 15.6, 15.6, 15.7, 15.8, 15.9]

fig, (ax2, ax1, ax3) = plt.subplots(3, 1, figsize=(14, 15), dpi=100)

ax2.plot(years, per_capita_emissions, color='green', linestyle='-', linewidth=2, marker='o')
ax1.plot(years, co2_levels, color='darkred', linestyle='-', linewidth=2, marker='o')
ax1_secondary = ax1.twinx()
ax1_secondary.plot(years, global_temps, color='darkblue', linestyle='--', linewidth=2, marker='s')
ax3.plot(years, renewable_energy_adoption, color='purple', linestyle='-', linewidth=2, marker='^')

plt.tight_layout()
plt.show()