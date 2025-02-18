import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2005, 2021)

# Each group will be manually altered while preserving the original dimensional structure
waste_reduction = [15, 9, 5, 22, 35, 18, 12, 46, 26, 30, 7, 40, 72, 59, 52, 65]
water_conservation = [7, 15, 19, 4, 5, 12, 28, 9, 45, 67, 39, 33, 23, 59, 3, 52]
green_energy = [14, 49, 19, 2, 3, 32, 25, 70, 95, 10, 1, 40, 82, 59, 7, 5]
community_awareness = [35, 10, 6, 3, 48, 13, 8, 56, 65, 29, 20, 2, 16, 24, 41, 4]
urban_greenery = [52, 71, 5, 3, 15, 8, 30, 61, 37, 19, 11, 24, 94, 82, 2, 44]

sustainability_efforts = np.vstack([waste_reduction, water_conservation, green_energy, community_awareness, urban_greenery])

fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(years, sustainability_efforts, colors=['#76C1A1'], alpha=0.8)
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.legend(['Waste Reduction', 'Water Conservation', 'Green Energy',
           'Community Awareness', 'Urban Greenery'], loc='upper left', frameon=False)

plt.tight_layout()
plt.show()