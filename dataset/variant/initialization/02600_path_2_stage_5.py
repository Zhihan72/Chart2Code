import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
e_commerce_sales = np.array([20, 40, 60, 85, 115, 150, 190, 240, 300])
retail_sales = np.array([250, 245, 230, 210, 185, 160, 140, 120, 100])
direct_sales = np.array([30, 35, 40, 48, 60, 75, 90, 110, 135])

fig, ax1 = plt.subplots(figsize=(7, 6))

# Altered color and marker types, styles
e_commerce_color = 'orange'
retail_color = 'blue'
direct_color = 'green'

ax1.scatter(years, e_commerce_sales, color=e_commerce_color, label='E-com', marker='^', s=80, alpha=0.9)
ax1.scatter(years, retail_sales, color=retail_color, label='Retail', marker='d', s=80, alpha=0.7)
ax1.scatter(years, direct_sales, color=direct_color, label='Direct', marker='*', s=100, alpha=0.5)

years_fine = np.linspace(years.min(), years.max(), 300)
e_commerce_spline = make_interp_spline(years, e_commerce_sales)(years_fine)
retail_spline = make_interp_spline(years, retail_sales)(years_fine)
direct_spline = make_interp_spline(years, direct_sales)(years_fine)

ax1.plot(years_fine, e_commerce_spline, color=e_commerce_color, linestyle='-.', linewidth=2.5, alpha=0.7)
ax1.plot(years_fine, retail_spline, color=retail_color, linestyle=':', linewidth=2.5, alpha=0.7)
ax1.plot(years_fine, direct_spline, color=direct_color, linestyle='--', linewidth=2.5, alpha=0.7)

ax1.set_title("E-com vs. Retail vs. Direct Sales", fontsize=14, weight='bold', color='darkred')
ax1.set_xlabel("Year", fontsize=12, color='gray')
ax1.set_ylabel("Sales (M USD)", fontsize=12, color='gray')

# Legend style update
ax1.legend(loc='upper right', fontsize=10, frameon=True, framealpha=0.9, shadow=True, facecolor='lightgrey')

# Grid style update
ax1.grid(True, linestyle='-', alpha=0.3, color='lightblue')

plt.tight_layout()
plt.show()