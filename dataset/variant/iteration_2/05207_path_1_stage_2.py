import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

years = np.arange(2013, 2023)
monthly_avg_temp_coastal = np.array([15, 16, 15.5, 16, 16.5, 17, 16.7, 17.2, 17.5, 18])
monthly_avg_temp_inland = np.array([10, 10.5, 10.3, 11, 10.8, 11.5, 11.3, 11.8, 12, 12.2])

coastal_spline = make_interp_spline(years, monthly_avg_temp_coastal, k=3)  
inland_spline = make_interp_spline(years, monthly_avg_temp_inland, k=3)

years_smooth = np.linspace(years.min(), years.max(), 300)
coastal_temp_smooth = coastal_spline(years_smooth)
inland_temp_smooth = inland_spline(years_smooth)

plt.figure(figsize=(14, 8))

plt.plot(years_smooth, coastal_temp_smooth, label='Coastal Region', color='darkorange', linewidth=2)
plt.plot(years_smooth, inland_temp_smooth, label='Inland Region', color='purple', linewidth=2)

plt.scatter(years, monthly_avg_temp_coastal, color='darkorange', edgecolors='black', s=50)
plt.scatter(years, monthly_avg_temp_inland, color='purple', edgecolors='black', s=50)

plt.title('Decadal Trends in Average Monthly Temperatures Across Regions', fontsize=16, fontweight='bold', loc='center')
plt.xlabel('Year', fontsize=13)
plt.ylabel('Average Monthly Temperature (°C)', fontsize=13)

plt.xticks(np.arange(2013, 2024, step=1))
plt.yticks(np.arange(5, 19, step=1))
plt.legend(loc='upper left', fontsize=11, frameon=True)
plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()