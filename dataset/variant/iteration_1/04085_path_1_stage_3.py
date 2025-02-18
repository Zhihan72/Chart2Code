import matplotlib.pyplot as plt
import numpy as np

years = np.array([2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 
                  2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])

temperature_anomalies = np.array([-0.2, -0.15, -0.1, 0.02, 0.1, 0.12, 0.18, 0.22, 0.3, 
                                  0.38, 0.4, 0.5, 0.55, 0.57, 0.62, 0.65, 0.68, 0.7, 0.75, 0.8])

colors = np.where(temperature_anomalies < 0, 'red', 'blue')

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(years, temperature_anomalies, marker='o', linestyle='-', color='black', linewidth=2, markersize=8, label='Temp Deviations')

ax.fill_between(years, temperature_anomalies, where=(temperature_anomalies < 0), color='red', alpha=0.3, interpolate=True)
ax.fill_between(years, temperature_anomalies, where=(temperature_anomalies >= 0), color='blue', alpha=0.3, interpolate=True)

ax.set_title("Climate Trends Over Two Decades\nRelative to Historical Average", fontsize=16, fontweight='bold')
ax.set_xlabel("Chronological Year", fontsize=14)
ax.set_ylabel("Deviation in Temp (°C)", fontsize=14)
ax.set_xticks(np.arange(2000, 2021, 2))
ax.set_yticks(np.arange(-0.2, 0.9, 0.1))
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(loc="upper left", fontsize=12)

significant_points = [2003, 2012, 2016, 2020]
for sp in significant_points:
    if sp in years:
        sp_index = np.where(years == sp)[0][0]
        ax.annotate(f'{temperature_anomalies[sp_index]:.2f}°C', 
                    xy=(sp, temperature_anomalies[sp_index]), 
                    xytext=(sp+0.5, temperature_anomalies[sp_index]+0.15),
                    arrowprops=dict(facecolor='black', arrowstyle='->'),
                    fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()