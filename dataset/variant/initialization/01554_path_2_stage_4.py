import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

desktops = np.array([48, 42, 50, 35, 32, 45, 38, 24, 30, 26, 28])
laptops = np.array([32, 38, 30, 46, 35, 49, 41, 47, 43, 48, 45])
tablets = np.array([5, 6, 5, 13, 7, 14, 8, 12, 10, 11, 5])
smartphones = 100 - (desktops + laptops + tablets)

average_screen_time = np.array([6, 6.2, 6.5, 6.8, 7.1, 7.4, 7.8, 8.2, 8.6, 9, 9.5])

fig, ax1 = plt.subplots(figsize=(14, 8))

random_colors = ['#FF6347', '#6A5ACD', '#3CB371', '#FFD700']
ax1.stackplot(years, desktops, laptops, tablets, smartphones, 
              labels=['Desktops', 'Laptops', 'Tablets', 'Smartphones'], 
              colors=random_colors, alpha=0.75)

ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Usage Percentage', fontsize=12, color='brown')
ax1.set_title('Device Usage Over Time and\nScreen Time Trends (2010-2020)', fontsize=16, weight='bold', color='darkblue')

ax1.grid(False)  # Removed the grid to alter stylistic elements
ax1.legend(loc='lower center', title='Device Types', fontsize=11)

ax2 = ax1.twinx()
ax2.plot(years, average_screen_time, color='darkred', marker='s', linestyle='-', linewidth=2, label='Avg Screen Time')
ax2.set_ylabel('Avg Daily Screen Time (hrs)', fontsize=12, color='darkred')
ax2.tick_params(axis='y', labelcolor='darkred')

ax2.legend(loc='lower right', fontsize=11)

plt.tight_layout()
plt.show()