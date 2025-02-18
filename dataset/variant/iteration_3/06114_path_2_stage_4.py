import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

delta_a_pollution = [6.4, 5.4, 5.0, 6.3, 4.8, 8.2, 7.6, 7.0, 4.5, 7.4, 5.2, 4.6, 7.8, 8.0, 4.5, 6.5, 7.2, 6.2, 6.0, 6.8, 7.3]
delta_a_fish_population = [1370, 1130, 1180, 1150, 1400, 1260, 1100, 1240, 1080, 1200, 1320, 1300, 1420, 1160, 1280, 1440, 1380, 1460, 1350, 1400, 1480]
delta_a_water_clarity = [76, 81, 62, 70, 54, 78, 72, 53, 74, 62, 85, 68, 51, 58, 83, 85, 56, 49, 47, 89, 87]

delta_b_pollution = [4.5, 4.2, 5.1, 5.0, 4.4, 3.5, 4.0, 5.6, 5.4, 6.2, 3.8, 5.3, 5.2, 4.8, 5.8, 3.7, 4.3, 4.9, 6.0, 3.6, 4.7]
delta_b_fish_population = [1510, 1550, 1320, 1570, 1480, 1580, 1300, 1600, 1340, 1520, 1450, 1370, 1590, 1540, 1420, 1400, 1430, 1360, 1390, 1500, 1470]
delta_b_water_clarity = [44, 69, 83, 55, 48, 46, 50, 78, 91, 57, 85, 80, 73, 82, 65, 51, 76, 84, 68, 60, 63]

delta_c_pollution = [2.5, 3.0, 3.7, 2.6, 3.1, 4.5, 3.3, 3.6, 3.8, 4.2, 2.2, 3.5, 4.0, 2.9, 2.4, 3.2, 4.4, 2.1, 2.3, 2.0, 2.8]
delta_c_fish_population = [1070, 1020, 1140, 1100, 980, 1080, 1170, 1150, 1000, 1200, 1180, 1190, 1060, 960, 1160, 1120, 1090, 940, 1110, 1050, 1030]
delta_c_water_clarity = [68, 89, 70, 78, 87, 74, 84, 90, 65, 81, 86, 83, 91, 92, 80, 76, 88, 69, 66, 82, 72]

fig, axs = plt.subplots(3, 1, figsize=(14, 18), sharex=True)
fig.suptitle('Environmental Impact of Urbanization on River Delta Regions (2000-2020)', fontsize=16, fontweight='bold', y=0.92)

# Subplot 1: Water Clarity
axs[0].plot(years, delta_a_water_clarity, color='lime', linestyle='-', linewidth=2)
axs[0].plot(years, delta_b_water_clarity, color='cyan', linestyle='--', linewidth=2)
axs[0].plot(years, delta_c_water_clarity, color='magenta', linestyle='-.', linewidth=2)
axs[0].set_title('Water Clarity (clarity units)', fontsize=14, pad=10)
axs[0].set_ylabel('Water Clarity', fontsize=12)

# Subplot 2: Fish Population
axs[1].plot(years, delta_a_fish_population, color='brown', linestyle='-', linewidth=2)
axs[1].plot(years, delta_b_fish_population, color='blue', linestyle='--', linewidth=2)
axs[1].plot(years, delta_c_fish_population, color='green', linestyle='-.', linewidth=2)
axs[1].set_title('Fish Population (in thousands)', fontsize=14, pad=10)
axs[1].set_ylabel('Fish Population', fontsize=12)

# Subplot 3: Pollution Levels
axs[2].plot(years, delta_a_pollution, color='purple', linestyle='-', linewidth=2)
axs[2].plot(years, delta_b_pollution, color='red', linestyle='--', linewidth=2)
axs[2].plot(years, delta_c_pollution, color='orange', linestyle='-.', linewidth=2)
axs[2].set_title('Pollution Levels (in arbitrary units)', fontsize=14, pad=10)
axs[2].set_xlabel('Year', fontsize=12)
axs[2].set_ylabel('Pollution Level', fontsize=12)

plt.subplots_adjust(hspace=0.4)
plt.show()