import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2020, 2031)
brand_a = np.array([32, 37, 39, 44, 51, 53, 48, 50, 47, 45, 48])  # Manually altered values
brand_b = np.array([21, 23, 23, 26, 28, 31, 30, 34, 33, 32, 35])  # Manually altered values
brand_c = np.array([11, 13, 14, 14, 19, 18, 22, 21, 19, 25, 22])  # Manually altered values
brand_d = np.array([16, 13, 14, 11, 11, 8, 9, 9, 7, 10, 9])       # Manually altered values
brand_e = np.array([24, 17, 12, 4, 3, 2, 2, 1, 3, 2, 1])         # Manually altered values

data = np.vstack([brand_a, brand_b, brand_c, brand_d, brand_e])

fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(years, data, colors=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#CCD1FF'], alpha=0.8)

ax.set_title('Smartphone Market Penetration in a Futuristic Tech City (2020-2030)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Market Share (%)', fontsize=12)
ax.set_xticks(years)
ax.set_xticklabels(years)

ax.annotate('Peak of Brand A', xy=(2021, 37), xytext=(2023, 52),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')
ax.annotate('Rise of Brand E', xy=(2020, 24), xytext=(2020, 44),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')

plt.tight_layout()
plt.show()