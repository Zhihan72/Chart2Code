import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
e_commerce_sales = np.array([20, 40, 60, 85, 115, 150, 190, 240, 300])
retail_sales = np.array([250, 245, 230, 210, 185, 160, 140, 120, 100])
direct_sales = np.array([30, 35, 40, 48, 60, 75, 90, 110, 135])

total_sales = e_commerce_sales + retail_sales + direct_sales
e_commerce_market_share = e_commerce_sales / total_sales * 100
retail_market_share = retail_sales / total_sales * 100
direct_market_share = direct_sales / total_sales * 100

fig, ax1 = plt.subplots(figsize=(7, 6))

uniform_color = 'teal'

ax1.scatter(years, e_commerce_sales, color=uniform_color, label='E-com', marker='o', s=100, alpha=0.8)
ax1.scatter(years, retail_sales, color=uniform_color, label='Retail', marker='x', s=100, alpha=0.8)
ax1.scatter(years, direct_sales, color=uniform_color, label='Direct', marker='s', s=100, alpha=0.8)

years_fine = np.linspace(years.min(), years.max(), 300)
e_commerce_spline = make_interp_spline(years, e_commerce_sales)(years_fine)
retail_spline = make_interp_spline(years, retail_sales)(years_fine)
direct_spline = make_interp_spline(years, direct_sales)(years_fine)

ax1.plot(years_fine, e_commerce_spline, color=uniform_color, linestyle='-', linewidth=2, alpha=0.6)
ax1.plot(years_fine, retail_spline, color=uniform_color, linestyle='-', linewidth=2, alpha=0.6)
ax1.plot(years_fine, direct_spline, color=uniform_color, linestyle='-', linewidth=2, alpha=0.6)

ax1.set_title("E-com vs. Retail vs. Direct Sales", fontsize=14, weight='bold')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Sales (M USD)", fontsize=12)
ax1.legend(loc='upper left')
ax1.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()