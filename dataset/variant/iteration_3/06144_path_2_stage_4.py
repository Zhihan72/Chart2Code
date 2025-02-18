import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2031)

# Manually shuffled/altered energy data arrays
solar_energy = np.array([2, 4, 1, 10, 16, 24, 6, 46, 34, 76, 60, 114, 94, 136, 160, 186, 214, 310, 244, 276, 346])
wind_energy = np.array([9, 5, 3, 20, 27, 14, 44, 35, 54, 66, 79, 108, 93, 124, 159, 141, 178, 264, 198, 219, 241])
hydro_energy = np.array([19, 12, 10, 24, 15, 30, 37, 64, 45, 54, 87, 75, 100, 114, 145, 129, 180, 240, 162, 199, 219])
bio_energy = np.array([8, 3, 5, 12, 17, 23, 30, 38, 138, 47, 57, 80, 93, 68, 80, 122, 173, 192, 155, 107, 212])
geothermal_energy = np.array([1, 1, 3, 2, 5, 7, 10, 19, 14, 32, 25, 49, 40, 59, 95, 109, 82, 157, 124, 140, 70])

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, solar_energy, wind_energy, hydro_energy, bio_energy, geothermal_energy,
             colors=['#ffa07a', '#20b2aa', '#778899', '#daa520', '#9370db'], alpha=0.8)

ax.tick_params(axis='x', rotation=45)
plt.tight_layout()
plt.show()