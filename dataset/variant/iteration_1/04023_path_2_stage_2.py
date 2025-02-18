import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
dissolved_oxygen = [7.5, 7.2, 6.9, 6.7, 6.5, 6.2, 6.0, 5.8, 5.6, 5.5, 5.2]
ph_level = [7.0, 6.9, 6.8, 6.7, 6.5, 6.4, 6.3, 6.1, 6.0, 6.0, 5.9]
nitrate_concentration = [5, 5.5, 6, 6.2, 6.5, 7, 7.3, 7.5, 8, 8.2, 8.5]

fig, ax1 = plt.subplots(figsize=(14, 7))
ax2 = ax1.twinx()

ax1.plot(years, dissolved_oxygen, color='cyan', marker='o', linewidth=2)
ax1.plot(years, ph_level, color='orange', marker='^', linewidth=2)
ax2.plot(years, nitrate_concentration, color='purple', marker='s', linewidth=2)

ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Dissolved Oxygen (mg/L) / pH Level', fontsize=12, color='cyan')
ax2.set_ylabel('Nitrate Concentration (mg/L)', fontsize=12, color='purple')
plt.title('Decadal Health Monitoring of River (2010-2020)', fontsize=16, fontweight='bold')

fig.tight_layout()
plt.show()