import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

city_a_temps = [3, 2, 7, 12, 22, 23, 26, 27, 20, 15, 9, 4]
city_b_temps = [6, 5, 9, 17, 22, 25, 31, 30, 24, 19, 12, 7]
city_c_temps = [1, 0, 5, 9, 15, 20, 24, 25, 18, 13, 7, -1]

fig, axs = plt.subplots(1, 2, figsize=(14, 7))

axs[0].plot(months, city_a_temps, '-o', color='red', linewidth=2, markerfacecolor='white')  # changed from blue to red
axs[0].plot(months, city_b_temps, '-s', color='orange', linewidth=2, markerfacecolor='white')  # changed from green to orange
axs[0].set_title('Average Monthly Temperatures (2050):\nCity A and City B', fontsize=14, fontweight='bold')
axs[0].set_xlabel('Months', fontsize=12)
axs[0].set_ylabel('Temperature (°C)', fontsize=12)
axs[0].set_xticks(np.arange(len(months)))
axs[0].set_xticklabels(months)

axs[1].plot(months, city_c_temps, '-^', color='purple', linewidth=2, markerfacecolor='white')  # changed from red to purple

winter_mean = np.mean(city_c_temps[0:2] + city_c_temps[11:])
spring_mean = np.mean(city_c_temps[2:5])
summer_mean = np.mean(city_c_temps[5:8])
autumn_mean = np.mean(city_c_temps[8:11])

axs[1].axhline(y=winter_mean, color='green', linestyle='--')  # changed from blue to green
axs[1].axhline(y=spring_mean, color='purple', linestyle='--')  # changed from green to purple
axs[1].axhline(y=summer_mean, color='gray', linestyle='--')  # changed from orange to gray
axs[1].axhline(y=autumn_mean, color='blue', linestyle='--')  # changed from purple to blue
axs[1].set_title('Average Monthly Temperatures (2050):\nCity C with Seasonal Means', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Months', fontsize=12)
axs[1].set_ylabel('Temperature (°C)', fontsize=12)
axs[1].set_xticks(np.arange(len(months)))
axs[1].set_xticklabels(months)

season_annot = [('Winter', winter_mean), ('Spring', spring_mean), ('Summer', summer_mean), ('Autumn', autumn_mean)]
for season, mean_temp in season_annot:
    axs[1].text(len(months)-1, mean_temp + 0.5, f'{season} mean: {mean_temp:.1f}°C', 
                fontsize=10, color='black', ha='right', backgroundcolor='white')

plt.show()