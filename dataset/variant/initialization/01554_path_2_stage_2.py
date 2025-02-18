import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

desktops = np.array([48, 42, 50, 35, 32, 45, 38, 24, 30, 26, 28])
laptops = np.array([32, 38, 30, 46, 35, 49, 41, 47, 43, 48, 45])
tablets = np.array([5, 6, 5, 13, 7, 14, 8, 12, 10, 11, 5])
smartphones = 100 - (desktops + laptops + tablets)

average_screen_time = np.array([6, 6.2, 6.5, 6.8, 7.1, 7.4, 7.8, 8.2, 8.6, 9, 9.5])

fig, ax1 = plt.subplots(figsize=(14, 8))

# Apply a single color across all data groups
single_color = '#4682B4'
ax1.stackplot(years, desktops, laptops, tablets, smartphones, labels=['Desktops', 'Laptops', 'Tablets', 'Smartphones'], colors=[single_color]*4, alpha=0.85)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Percentage of Time Spent', fontsize=12, color='k')
ax1.set_title('Evolution of Device Usage and Average Screen Time\nin Remote Work Environments (2010-2020)', fontsize=16, weight='bold')

ax1.grid(alpha=0.3)
ax1.legend(loc='upper left', title='Devices', fontsize=10)

ax2 = ax1.twinx()
ax2.plot(years, average_screen_time, color='purple', marker='o', linestyle='--', linewidth=2.5, label='Average Screen Time per Day')
ax2.set_ylabel('Average Screen Time (hours)', fontsize=12, color='purple')
ax2.tick_params(axis='y', labelcolor='purple')

ax2.legend(loc='upper right', fontsize=10)

plt.tight_layout()
plt.show()