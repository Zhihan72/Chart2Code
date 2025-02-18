import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
desktops = np.array([50, 48, 45, 42, 38, 35, 32, 30, 28, 26, 24])
laptops = np.array([30, 32, 35, 38, 41, 43, 45, 46, 47, 48, 49])
tablets = np.array([5, 5, 5, 6, 7, 8, 10, 11, 12, 13, 14])
smartphones = 100 - (desktops + laptops + tablets)
average_screen_time = np.array([6, 6.2, 6.5, 6.8, 7.1, 7.4, 7.8, 8.2, 8.6, 9, 9.5])

fig, ax1 = plt.subplots(figsize=(14, 8))

colors = ['#32CD32', '#FFDEAD', '#FF6347', '#4682B4']  # Randomized color order
ax1.stackplot(years, desktops, laptops, tablets, smartphones, 
              labels=['Desktops', 'Laptops', 'Tablets', 'Smartphones'], 
              colors=colors, alpha=0.75)  # Changed transparency
ax1.set_xlabel('Year', fontsize=14)  # Increased fontsize
ax1.set_ylabel('Percentage of Time Spent', fontsize=14, color='gray')  # Changed color
ax1.set_title('Device Usage & Screen Time in Remote Work (2010-2020)', fontsize=18, weight='light')  # Altered title

ax1.grid(visible=False)  # Removed grid

ax1.legend(loc='lower right', title='Devices', fontsize=12, frameon=False)  # Changed position and removed frame

ax2 = ax1.twinx()
ax2.plot(years, average_screen_time, color='brown', marker='x', linestyle='-', linewidth=1.5, label='Avg Screen Time')  # Altered line style
ax2.set_ylabel('Avg Screen Time (hrs)', fontsize=12, color='brown')
ax2.tick_params(axis='y', labelcolor='brown')

ax2.legend(loc='center left', fontsize=11, framealpha=0.5)  # Changed position and semi-transparent frame

plt.tight_layout()
plt.show()