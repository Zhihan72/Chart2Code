import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
e_commerce_sales = np.array([20, 40, 60, 85, 115, 150, 190, 240, 300])

fig, ax1 = plt.subplots(figsize=(7, 6))  # Updated for single plot configuration

ax1.scatter(years, e_commerce_sales, color='red', label='E-com Sales', marker='o', s=100, alpha=0.8)

years_fine = np.linspace(years.min(), years.max(), 300)
e_commerce_spline = make_interp_spline(years, e_commerce_sales)(years_fine)

ax1.plot(years_fine, e_commerce_spline, color='red', linestyle='-', linewidth=2, alpha=0.6)

ax1.set_title("E-commerce Sales", fontsize=14, weight='bold')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Sales (M USD)", fontsize=12)
ax1.legend(loc='upper left')
ax1.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()