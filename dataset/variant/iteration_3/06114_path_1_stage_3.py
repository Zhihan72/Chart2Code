import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

delta_a_pollution = [4.5, 4.6, 4.8, 5.0, 5.2, 5.4, 5.7, 6.0, 6.2, 6.3, 6.4, 6.5, 6.8, 7.0, 7.2, 7.3, 7.4, 7.6, 7.8, 8.0, 8.2]
delta_a_fish_population = [1500, 1480, 1460, 1440, 1420, 1400, 1380, 1370, 1350, 1320, 1300, 1280, 1260, 1240, 1220, 1200, 1180, 1150, 1130, 1100, 1080]
delta_a_water_clarity = [89, 87, 85, 83, 81, 78, 76, 74, 72, 70, 68, 65, 62, 60, 58, 56, 54, 53, 51, 49, 47]

delta_b_pollution = [3.5, 3.6, 3.7, 3.8, 4.0, 4.2, 4.3, 4.4, 4.5, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 5.6, 5.8, 6.0, 6.2]
delta_b_fish_population = [1600, 1590, 1580, 1570, 1550, 1540, 1520, 1510, 1500, 1480, 1470, 1450, 1430, 1420, 1400, 1390, 1370, 1360, 1340, 1320, 1300]
delta_b_water_clarity = [85, 84, 82, 80, 78, 76, 73, 70, 68, 65, 63, 60, 58, 57, 55, 53, 51, 50, 48, 46, 44]

delta_c_pollution = [2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.5, 3.6, 3.7, 3.8, 4.0, 4.2, 4.4, 4.5]
delta_c_fish_population = [1200, 1190, 1180, 1170, 1160, 1150, 1140, 1120, 1110, 1100, 1080, 1070, 1060, 1050, 1030, 1020, 1000, 980, 960, 940, 920]
delta_c_water_clarity = [92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 78, 76, 74, 72, 70, 68, 66, 65]

fig, axs = plt.subplots(3, 1, figsize=(14, 18), sharex=True)

# Subplot 1: Pollution Levels
axs[0].plot(years, delta_c_pollution, color='blue', linestyle=':', marker='o', linewidth=2)
axs[0].plot(years, delta_a_pollution, color='green', linestyle='--', marker='^', linewidth=2)
axs[0].plot(years, delta_b_pollution, color='purple', linestyle='-', marker='s', linewidth=2)
axs[0].grid(True, linestyle='-', linewidth=0.5, alpha=0.9)

# Subplot 2: Fish Population
axs[1].plot(years, delta_b_fish_population, color='brown', linestyle='--', marker='x', linewidth=2)
axs[1].plot(years, delta_c_fish_population, color='cyan', linestyle=':', marker='d', linewidth=2)
axs[1].plot(years, delta_a_fish_population, color='magenta', linestyle='-.', marker='v', linewidth=2)
axs[1].grid(True, linestyle=':', linewidth=0.5, alpha=0.5)

# Subplot 3: Water Clarity
axs[2].plot(years, delta_a_water_clarity, color='darkred', linestyle='-', marker='P', linewidth=2)
axs[2].plot(years, delta_b_water_clarity, color='gold', linestyle='--', marker='H', linewidth=2)
axs[2].plot(years, delta_c_water_clarity, color='darkgreen', linestyle='-.', marker='<', linewidth=2)
axs[2].grid(True, linestyle='-', linewidth=0.7, alpha=0.8)

plt.subplots_adjust(hspace=0.4)
plt.show()