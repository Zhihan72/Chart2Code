import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
moon_crystals = np.array([6, 8, 10, 12, 15, 20, 22, 28, 33, 37, 42])
sun_gemstones = np.array([4, 5, 6, 5, 9, 10, 13, 15, 17, 18, 22])
star_dust = np.array([3, 4, 5, 7, 10, 11, 13, 15, 17, 19, 21])
sky_pearls = np.array([1, 3, 3, 3, 5, 6, 7, 8, 9, 10, 11])

resource_data = np.vstack([moon_crystals, sun_gemstones, star_dust, sky_pearls])

fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(years, resource_data, colors=['#FF5733', '#33FF57', '#3357FF', '#FF33A1'], alpha=0.8)

ax.set_title('Fantasy World Natural Resource Usage in Mythica (2010-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Resource Usage (Thousands of Units)', fontsize=14)

ax.set_xticks(years)
ax.set_yticks(np.arange(0, 101, 10))

ax.annotate('Introduction of Moon Crystals', xy=(2015, 20), xytext=(2012, 50),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, ha='center', backgroundcolor='white')

ax.annotate('Discovery of Star Dust', xy=(2017, 28), xytext=(2018, 65),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, ha='center', backgroundcolor='white')

plt.tight_layout()
plt.show()