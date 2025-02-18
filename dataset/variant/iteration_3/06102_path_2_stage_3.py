import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)
city_a_temps = [5, 7, 10, 15, 20, 25, 28, 27, 23, 17, 10, 6]
city_c_temps = [12, 12, 15, 18, 22, 25, 30, 31, 28, 24, 20, 15]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(months, city_a_temps, marker='s', linestyle='--', color='coral', linewidth=2, label='City A')
ax.plot(months, city_c_temps, marker='d', linestyle='-.', color='green', linewidth=2, label='City C')

ax.set_title('Yearly Temperature Trends in Fictional Cities', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Average Daily Temperature (°C)', fontsize=12)

ax.legend(loc='lower left', fontsize=12, title='Cities', title_fontsize=14)

ax.grid(True, linestyle=':', alpha=0.9)

month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.xticks(months, month_names, fontsize=10)

plt.tight_layout()
plt.show()