import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
e_commerce_sales = np.array([20, 40, 60, 85, 115, 150, 190, 240, 300])

fig, ax1 = plt.subplots(figsize=(7, 6))

# Scatter plot with a different marker type and color
ax1.scatter(years, e_commerce_sales, color='blue', label='E-com Sales', marker='s', s=100, alpha=0.8)

years_fine = np.linspace(years.min(), years.max(), 300)
e_commerce_spline = make_interp_spline(years, e_commerce_sales)(years_fine)

# Smoothed line with a different line style and color
ax1.plot(years_fine, e_commerce_spline, color='green', linestyle='--', linewidth=2, alpha=0.6)

ax1.set_title("E-commerce Sales", fontsize=14, weight='bold')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Sales (M USD)", fontsize=12)

# Legend moved to a different location
ax1.legend(loc='lower right')

# Grid with different line style
ax1.grid(True, linestyle=':', alpha=0.7)

# Different border style and color
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_color('grey')

plt.tight_layout()
plt.show()