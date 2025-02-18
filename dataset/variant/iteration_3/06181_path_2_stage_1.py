import matplotlib.pyplot as plt
import numpy as np

months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

max_temp_2022 = np.array([5, 7, 12, 16, 21, 25, 29, 28, 24, 18, 11, 6])
min_temp_2022 = np.array([-3, -2, 1, 6, 10, 14, 18, 17, 12, 8, 3, -1])
max_temp_2023 = np.array([6, 8, 13, 17, 22, 26, 30, 29, 25, 19, 12, 7])
min_temp_2023 = np.array([-2, -1, 2, 7, 11, 15, 19, 18, 13, 9, 4, 0])

fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the data for 2022 with new colors
ax.plot(months, max_temp_2022, label='Max Temp 2022', color='purple', marker='o', linestyle='-', linewidth=2)
ax.plot(months, min_temp_2022, label='Min Temp 2022', color='green', marker='o', linestyle='-', linewidth=2)

# Plotting the data for 2023 with new colors
ax.plot(months, max_temp_2023, label='Max Temp 2023', color='brown', marker='s', linestyle='--', linewidth=2)
ax.plot(months, min_temp_2023, label='Min Temp 2023', color='pink', marker='s', linestyle='--', linewidth=2)

ax.set_title('Monthly Temperature Trends in Sunnyvale (2022-2023)', fontsize=16, fontweight='bold')
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Temperature (°C)', fontsize=14)

ax.legend(loc='upper right', fontsize=12, title='Temperature Data')
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

ax.annotate('Hottest Month 2023', xy=('Jul', 30), xytext=('May', 32),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)

ax.annotate('Coldest Month 2022', xy=('Jan', -3), xytext=('Mar', -5),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)

plt.tight_layout()
plt.show()