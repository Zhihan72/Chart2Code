import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)

avg_temperatures_2022 = np.array([15.0, 5.5, 7.2, 20.5, 23.0, 10.8, 17.5, 22.8, 19.5, 14.2, 6.3, 9.0])
avg_temperatures_2021 = np.array([18.4, 13.2, 5.7, 6.5, 9.1, 16.8, 4.8, 19.6, 14.0, 22.1, 21.9, 8.2])

high_temperatures_2022 = np.array([20.0, 26.0, 29.0, 17.5, 24.0, 10.0, 12.0, 15.0, 28.5, 22.5, 8.0, 9.0])
low_temperatures_2022 = np.array([11.0, 3.0, 4.5, 6.5, 15.0, 3.5, 6.0, 10.0, 12.0, 17.0, 17.5, 15.0])

temperature_range_2022 = high_temperatures_2022 - low_temperatures_2022

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

ax1.plot(months, avg_temperatures_2022, marker='o', linestyle='-', color='#1f77b4', linewidth=2, label='2022')
ax1.plot(months, avg_temperatures_2021, marker='s', linestyle='--', color='#ff7f0e', linewidth=2, label='2021')

ax1.set_title('Avg Temp: 2021 vs 2022', fontsize=16, fontweight='bold')
ax1.set_xlabel('Mo', fontsize=14)
ax1.set_ylabel('Temp (°C)', fontsize=14)

ax1.set_xticks(months)
ax1.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax1.legend(loc='upper left', fontsize=12)

ax2.bar(months, temperature_range_2022, color='#2ca02c', label='Temp Range', alpha=0.7)

ax2.set_title('Temp Range: 2022', fontsize=16, fontweight='bold')
ax2.set_xlabel('Mo', fontsize=14)
ax2.set_ylabel('Range (°C)', fontsize=14)

ax2.set_xticks(months)
ax2.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

ax2.grid(axis='y', linestyle='--', alpha=0.7)
ax2.legend(loc='upper right', fontsize=12)

plt.tight_layout()
plt.show()