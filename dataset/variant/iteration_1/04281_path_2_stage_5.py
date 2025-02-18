import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)
avg_temperatures_2022 = np.array([5.5, 6.3, 10.8, 15.0, 19.5, 22.8, 17.5, 23.0, 20.5, 14.2, 7.2, 9.0])
avg_temperatures_2021 = np.array([4.8, 8.2, 9.1, 14.0, 18.4, 21.9, 16.8, 19.6, 22.1, 13.2, 6.5, 5.7])
high_temperatures_2022 = np.array([8.0, 17.5, 10.0, 20.0, 28.5, 22.5, 15.0, 29.0, 26.0, 9.0, 12.0, 24.0])
low_temperatures_2022 = np.array([3.5, 4.5, 6.0, 17.0, 10.0, 15.0, 17.5, 12.0, 8.0, 11.0, 3.0, 6.5])

temperature_range_2022 = high_temperatures_2022 - low_temperatures_2022

fig, (ax2, ax1) = plt.subplots(1, 2, figsize=(18, 8))

ax2.plot(months, avg_temperatures_2022, marker='o', linestyle='-', color='#ff7f0e', linewidth=2)
ax2.plot(months, avg_temperatures_2021, marker='s', linestyle='--', color='#2ca02c', linewidth=2)

ax2.set_title('Avg Temp Monthly: AquaTown (Year2021 vs Yr22)', fontsize=16, fontweight='bold')
ax2.set_xlabel('Mnth', fontsize=14)
ax2.set_ylabel('Temp (°C)', fontsize=14)
ax2.set_xticks(months)
ax2.set_xticklabels(['J', 'Feb', 'Mrch', 'Ap', 'M', 'Jn', 'Jly', 'Au', 'S', 'Oc', 'N', 'De'])

ax1.bar(months, temperature_range_2022, color='#1f77b4', alpha=0.7)

ax1.set_title('Temp Diff in Aqua (Yr22)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Mnth', fontsize=14)
ax1.set_ylabel('Temp Diff (°C)', fontsize=14)
ax1.set_xticks(months)
ax1.set_xticklabels(['J', 'Feb', 'Mrch', 'Ap', 'M', 'Jn', 'Jly', 'Au', 'S', 'Oc', 'N', 'De'])

plt.tight_layout()
plt.show()