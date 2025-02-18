import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
city_a_temps = [2, 3, 7, 12, 18, 23, 27, 26, 21, 15, 9, 4]
city_b_temps = [5, 6, 10, 16, 21, 26, 31, 30, 25, 19, 12, 6]
city_c_temps = [-1, 0, 4, 10, 16, 21, 25, 24, 19, 13, 6, 0]
city_d_temps = [3, 4, 9, 14, 20, 25, 29, 28, 23, 18, 11, 5]
city_e_temps = [-2, -1, 3, 9, 14, 19, 23, 22, 17, 11, 5, -1]

fig, axs = plt.subplots(1, 2, figsize=(14, 7), constrained_layout=True)

axs[0].plot(months, city_c_temps, ':o', color='lime', label='City C', linewidth=2, markerfacecolor='black')
axs[0].plot(months, city_e_temps, '--v', color='magenta', label='City E', linewidth=2, markerfacecolor='black')

winter_mean = np.mean(city_c_temps[0:2] + city_c_temps[11:])
spring_mean = np.mean(city_c_temps[2:5])
summer_mean = np.mean(city_c_temps[5:8])
autumn_mean = np.mean(city_c_temps[8:11])

axs[0].axhline(y=winter_mean, color='pink', linestyle=':', label='Winter Mean')
axs[0].axhline(y=spring_mean, color='cyan', linestyle='-.', label='Spring Mean')
axs[0].axhline(y=summer_mean, color='brown', linestyle='-', label='Summer Mean')
axs[0].axhline(y=autumn_mean, color='darkgreen', linestyle='-', label='Autumn Mean')

axs[0].set_title('Avg Monthly Temps (2050): City C & City E', fontsize=16, fontweight='bold')
axs[0].set_xlabel('Months', fontsize=10)
axs[0].set_ylabel('Temperature (°C)', fontsize=10)
axs[0].set_xticks(np.arange(len(months)))
axs[0].set_xticklabels(months)
axs[0].grid(True, linestyle='-', alpha=0.3)
axs[0].legend(loc='lower right', fontsize=10)

season_annot = [('Winter', winter_mean), ('Spring', spring_mean), ('Summer', summer_mean), ('Autumn', autumn_mean)]
for season, mean_temp in season_annot:
    axs[0].text(len(months)-1, mean_temp + 0.5, f'{season} mean: {mean_temp:.1f}°C', 
                fontsize=8, color='darkred', ha='right', backgroundcolor='lightyellow')

axs[1].plot(months, city_a_temps, '-s', color='gray', label='City A', linewidth=2, markerfacecolor='yellow')
axs[1].plot(months, city_b_temps, '-^', color='navy', label='City B', linewidth=2, markerfacecolor='yellow')
axs[1].plot(months, city_d_temps, ':p', color='coral', label='City D', linewidth=2, markerfacecolor='yellow')

axs[1].set_title('Avg Monthly Temps (2050): City A, B, & D', fontsize=16, fontweight='bold')
axs[1].set_xlabel('Months', fontsize=10)
axs[1].set_ylabel('Temperature (°C)', fontsize=10)
axs[1].set_xticks(np.arange(len(months)))
axs[1].set_xticklabels(months)
axs[1].grid(False)
axs[1].legend(loc='upper right', fontsize=10)

plt.show()