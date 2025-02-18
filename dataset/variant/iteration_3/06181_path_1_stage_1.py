import matplotlib.pyplot as plt
import numpy as np

months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

# Manually altered temperature data for Sunnyvale (preserving the original data structure)
max_temp_2022 = np.array([5, 6, 15, 16, 21, 30, 25, 29, 24, 10, 11, 6])
min_temp_2022 = np.array([-3, -1, 3, 6, 9, 14, 17, 18, 12, 4, 3, -2])
max_temp_2023 = np.array([7, 9, 13, 20, 19, 25, 31, 28, 27, 18, 12, 8])
min_temp_2023 = np.array([-1, 0, 4, 7, 10, 15, 20, 19, 14, 9, 5, 1])

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(months, max_temp_2022, label='Max Temp 2022', color='red', marker='o', linestyle='-', linewidth=2)
ax.plot(months, min_temp_2022, label='Min Temp 2022', color='blue', marker='o', linestyle='-', linewidth=2)

ax.plot(months, max_temp_2023, label='Max Temp 2023', color='orange', marker='s', linestyle='--', linewidth=2)
ax.plot(months, min_temp_2023, label='Min Temp 2023', color='cyan', marker='s', linestyle='--', linewidth=2)

ax.set_title('Monthly Temperature Trends in Sunnyvale (2022-2023)', fontsize=16, fontweight='bold')
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Temperature (°C)', fontsize=14)

ax.legend(loc='upper right', fontsize=12, title='Temperature Data')

ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

ax.annotate('Hottest Month 2023', xy=('Jul', 31), xytext=('May', 33),
            arrowprops=dict(facecolor='green', shrink=0.05), fontsize=12)

ax.annotate('Coldest Month 2022', xy=('Jan', -3), xytext=('Mar', -5),
            arrowprops=dict(facecolor='green', shrink=0.05), fontsize=12)

plt.tight_layout()
plt.show()