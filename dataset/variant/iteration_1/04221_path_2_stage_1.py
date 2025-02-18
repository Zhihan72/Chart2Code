import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2020, 2031)
brand_a = np.array([30, 35, 40, 45, 50, 52, 50, 49, 48, 47, 46])
brand_b = np.array([20, 22, 24, 25, 27, 30, 32, 33, 34, 34, 34])
brand_c = np.array([10, 11, 12, 15, 17, 19, 21, 22, 22, 23, 23])
brand_d = np.array([15, 14, 13, 12, 10, 9, 8, 8, 8, 9, 10])
brand_e = np.array([25, 18, 11, 3, 1, 1, 1, 1, 1, 1, 1])

data = np.vstack([brand_a, brand_b, brand_c, brand_d, brand_e])

fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(years, data, colors=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#CCD1FF'], alpha=0.8)

ax.set_title('Smartphone Market Penetration in a Futuristic Tech City (2020-2030)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Market Share (%)', fontsize=12)
ax.set_xticks(years)
ax.set_xticklabels(years)

ax.annotate('Peak of Brand A', xy=(2021, 35), xytext=(2023, 50),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')
ax.annotate('Rise of Brand E', xy=(2020, 25), xytext=(2020, 45),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')

plt.tight_layout()
plt.show()