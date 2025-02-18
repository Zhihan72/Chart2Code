import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)

city_a_temps = [5, 7, 10, 15, 20, 25, 28, 27, 23, 17, 10, 6]
city_b_temps = [-2, 0, 5, 12, 18, 24, 30, 29, 22, 15, 8, 2]
city_c_temps = [12, 12, 15, 18, 22, 25, 30, 31, 28, 24, 20, 15]
city_d_temps = [8, 9, 13, 17, 21, 26, 29, 28, 26, 19, 13, 9]
city_e_temps = [-5, -3, 2, 9, 16, 22, 27, 26, 19, 12, 5, -1]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(months, city_a_temps, marker='<', linestyle=':', color='purple', linewidth=1.5, label='A')
ax.plot(months, city_b_temps, marker='*', linestyle='--', color='green', linewidth=1.5, label='B')
ax.plot(months, city_c_temps, marker='h', linestyle='-.', color='red', linewidth=1.5, label='C')
ax.plot(months, city_d_temps, marker='p', linestyle='-', color='orange', linewidth=1.5, label='D')
ax.plot(months, city_e_temps, marker='1', linestyle='-', color='cyan', linewidth=1.5, label='E')

ax.set_title('Temperature Trends', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Temp (°C)', fontsize=12)

ax.legend(loc='lower left', fontsize=9, title='City Temperatures', title_fontsize=11)

ax.grid(False)

ax.annotate('Summer Peak', xy=(8, 31), xytext=(6, 34),
            arrowprops=dict(facecolor='darkred', arrowstyle='->', lw=1.5), fontsize=10, color='darkblue')
ax.annotate('Cold Winter', xy=(1, -5), xytext=(3, -10),
            arrowprops=dict(facecolor='darkgreen', arrowstyle='->', lw=1.5), fontsize=10, color='darkred')

month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.xticks(months, month_names, fontsize=10)

plt.tight_layout()
plt.show()