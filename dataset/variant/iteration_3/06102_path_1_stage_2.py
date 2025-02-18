import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)

city_a_temps = [5, 7, 10, 15, 20, 25, 28, 27, 23, 17, 10, 6]
city_b_temps = [-2, 0, 5, 12, 18, 24, 30, 29, 22, 15, 8, 2]
city_c_temps = [12, 12, 15, 18, 22, 25, 30, 31, 28, 24, 20, 15]
city_d_temps = [8, 9, 13, 17, 21, 26, 29, 28, 26, 19, 13, 9]
city_e_temps = [-5, -3, 2, 9, 16, 22, 27, 26, 19, 12, 5, -1]

fig, ax = plt.subplots(figsize=(14, 8))

# Set all lines to the same color: blue
ax.plot(months, city_a_temps, marker='o', linestyle='-', color='blue', linewidth=2, label='City A')
ax.plot(months, city_b_temps, marker='s', linestyle='-', color='blue', linewidth=2, label='City B')
ax.plot(months, city_c_temps, marker='^', linestyle='-', color='blue', linewidth=2, label='City C')
ax.plot(months, city_d_temps, marker='D', linestyle='-', color='blue', linewidth=2, label='City D')
ax.plot(months, city_e_temps, marker='x', linestyle='-', color='blue', linewidth=2, label='City E')

ax.set_title('Yearly Temperature Trends in Fictional Cities', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Average Daily Temperature (°C)', fontsize=12)

ax.legend(loc='upper right', fontsize=10, title='Cities', title_fontsize=12)

ax.grid(True, linestyle='--', alpha=0.7)

ax.annotate('Peak Summer Temps', xy=(7, 30), xytext=(5, 35),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1), fontsize=10, color='darkred')
ax.annotate('Winter Start', xy=(12, 6), xytext=(10, -5),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1), fontsize=10, color='darkblue')

month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.xticks(months, month_names, fontsize=10)

plt.tight_layout()
plt.show()