import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

years = np.arange(2013, 2023)
monthly_avg_temp_coastal = np.array([16.5, 17, 15, 17.5, 16.7, 17.2, 16, 18, 15.5, 16])
monthly_avg_temp_inland = np.array([12, 10.3, 11.3, 10, 11.5, 12.2, 10.8, 11, 10.5, 11.8])
monthly_avg_temp_mountain = np.array([5.7, 7, 6.8, 6, 5.3, 6.4, 5.5, 6.2, 7.2, 5])

coastal_spline = make_interp_spline(years, monthly_avg_temp_coastal, k=3)
inland_spline = make_interp_spline(years, monthly_avg_temp_inland, k=3)
mountain_spline = make_interp_spline(years, monthly_avg_temp_mountain, k=3)

years_smooth = np.linspace(years.min(), years.max(), 300)
coastal_temp_smooth = coastal_spline(years_smooth)
inland_temp_smooth = inland_spline(years_smooth)
mountain_temp_smooth = mountain_spline(years_smooth)

plt.figure(figsize=(14, 8))

plt.plot(years_smooth, coastal_temp_smooth, color='darkblue', linewidth=2)
plt.plot(years_smooth, inland_temp_smooth, color='darkblue', linewidth=2)
plt.plot(years_smooth, mountain_temp_smooth, color='darkblue', linewidth=2)

plt.scatter(years, monthly_avg_temp_coastal, color='darkblue', edgecolors='black', s=50)
plt.scatter(years, monthly_avg_temp_inland, color='darkblue', edgecolors='black', s=50)
plt.scatter(years, monthly_avg_temp_mountain, color='darkblue', edgecolors='black', s=50)

plt.title('Analysis of Climate Changes Over Ten Years', fontsize=16, fontweight='bold', loc='center')
plt.xlabel('Time (Years)', fontsize=13)
plt.ylabel('Avg Temp (°C) Monthly', fontsize=13)

plt.xticks(np.arange(2013, 2024, step=1))
plt.yticks(np.arange(5, 19, step=1))

plt.show()