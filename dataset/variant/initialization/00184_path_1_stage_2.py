import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

years = np.array([1990, 1995, 2000, 2005, 2010, 2015, 2020])
internet_usage = np.array([2, 10, 30, 45, 65, 85, 90])
mobile_devices = np.array([5, 20, 50, 60, 70, 88, 95])
artificial_intelligence = np.array([1, 2, 5, 8, 15, 30, 70])

def get_smooth_curve(years, data):
    spline = make_interp_spline(years, data, k=3)
    smooth_years = np.linspace(years.min(), years.max(), 300)
    smooth_data = spline(smooth_years)
    return smooth_years, smooth_data

smooth_years_internet, smooth_internet_usage = get_smooth_curve(years, internet_usage)
smooth_years_mobile, smooth_mobile_devices = get_smooth_curve(years, mobile_devices)
smooth_years_ai, smooth_ai = get_smooth_curve(years, artificial_intelligence)

plt.figure(figsize=(14, 9))

plt.scatter(years, internet_usage, color='darkblue', s=100, label='Mobile Devices', alpha=0.6, edgecolor='black')
plt.plot(smooth_years_internet, smooth_internet_usage, color='steelblue', linewidth=2)

plt.scatter(years, mobile_devices, color='darkorange', s=100, label='Artificial Intelligence', alpha=0.6, edgecolor='black')
plt.plot(smooth_years_mobile, smooth_mobile_devices, color='orange', linewidth=2)

plt.scatter(years, artificial_intelligence, color='darkred', s=100, label='Cloud Computing', alpha=0.6, edgecolor='black')
plt.plot(smooth_years_ai, smooth_ai, color='red', linewidth=2)

plt.title("Year vs. Technology Usage\nAdoption Index Over Decades", fontsize=18, weight='bold', pad=20)
plt.xlabel("Adoption Rate (%)", fontsize=14)
plt.ylabel("Year", fontsize=14)
plt.xlim(1985, 2025)
plt.ylim(0, 100)
plt.xticks(np.arange(1990, 2025, 5))
plt.yticks(np.arange(0, 101, 10))
plt.legend(loc='upper left', fontsize=12, frameon=True, shadow=True)
plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()