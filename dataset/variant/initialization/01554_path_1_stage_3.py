import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
desktops = np.array([50, 48, 45, 42, 38, 35, 32, 30, 28, 26, 24])
laptops = np.array([30, 32, 35, 38, 41, 43, 45, 46, 47, 48, 49])
tablets = np.array([5, 5, 5, 6, 7, 8, 10, 11, 12, 13, 14])
smartphones = 100 - (desktops + laptops + tablets)
wearables = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
vr_devices = np.array([1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3])

smartphones -= (wearables + vr_devices)

average_screen_time = np.array([6, 6.2, 6.5, 6.8, 7.1, 7.4, 7.8, 8.2, 8.6, 9, 9.5])

fig, ax1 = plt.subplots(figsize=(14, 8))

colors = ['#FFDEAD', '#4682B4', '#8A2BE2', '#32CD32', '#FF6347', '#FFD700']
ax1.stackplot(years, desktops, laptops, tablets, smartphones, wearables, vr_devices,
              labels=['Desktops', 'Laptops', 'Tablets', 'Smartphones', 'Wearables', 'VR Devices'],
              colors=colors, alpha=0.75)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Percentage of Time Spent', fontsize=14, color='gray')
ax1.set_title('Device Usage & Screen Time in Remote Work (2010-2020)', fontsize=18, weight='light')

ax1.legend(loc='lower right', title='Devices', fontsize=12, frameon=False)

ax2 = ax1.twinx()
ax2.plot(years, average_screen_time, color='brown', marker='x', linestyle='-', linewidth=1.5, label='Avg Screen Time')
ax2.set_ylabel('Avg Screen Time (hrs)', fontsize=12, color='brown')
ax2.tick_params(axis='y', labelcolor='brown')

ax2.legend(loc='center left', fontsize=11, framealpha=0.5)

plt.tight_layout()
plt.show()