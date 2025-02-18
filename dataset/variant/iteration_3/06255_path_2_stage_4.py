import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

moon_crystals = np.array([5, 7, 9, 11, 14, 17, 20, 25, 30, 35, 40])
sun_gemstones = np.array([3, 4, 5, 6, 8, 9, 11, 13, 15, 17, 20])
star_dust = np.array([2, 3, 4, 6, 8, 10, 12, 14, 16, 18, 20])
sky_pearls = np.array([1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10])
cosmo_orbs = np.array([0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 6])  # New data series

resource_data = np.vstack([moon_crystals, sun_gemstones, star_dust, sky_pearls, cosmo_orbs])

fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(years, resource_data, labels=['Moon Crystals', 'Sun Gemstones', 'Star Dust', 'Sky Pearls', 'Cosmo Orbs'], alpha=0.8)

ax.set_xticks(years)
ax.set_yticks(np.arange(0, 101, 10))
ax.legend(loc='upper left')

plt.tight_layout()
plt.show()