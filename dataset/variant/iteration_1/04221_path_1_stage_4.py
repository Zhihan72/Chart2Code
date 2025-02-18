import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2020, 2031)
brand_a = np.array([30, 35, 40, 45, 50, 52, 50, 49, 48, 47, 46])
brand_b = np.array([20, 22, 24, 25, 27, 30, 32, 33, 34, 34, 34])
brand_c = np.array([10, 11, 12, 15, 17, 19, 21, 22, 22, 23, 23])
brand_d = np.array([15, 14, 13, 12, 10, 9, 8, 8, 8, 9, 10])
brand_e = np.array([25, 18, 11, 3, 1, 1, 1, 1, 1, 1, 1])
brand_f = np.array([0, 0, 0, 0, 5, 7, 8, 9, 10, 11, 12])
brand_g = np.array([0, 0, 0, 0, 0, 2, 3, 4, 5, 6, 7])

data = np.vstack([brand_a, brand_b, brand_c, brand_d, brand_e, brand_f, brand_g])

fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(years, data, colors=['#FFCC99', '#FF9999', '#66B2FF', '#CCD1FF', '#99FF99', '#FF6666', '#FFB266'], alpha=0.8)

ax.set_title('Tech City Mobile Growth (2020-2030)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timeline (Years)', fontsize=12)
ax.set_ylabel('Ownership (%)', fontsize=12)

ax.set_xticks(years)
ax.set_xticklabels(years)

plt.tight_layout()
plt.show()