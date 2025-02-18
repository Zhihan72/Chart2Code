import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

delta_a_pollution = [4.5, 4.6, 4.8, 5.0, 5.2, 5.4, 5.7, 6.0, 6.2, 6.3, 6.4, 6.5, 6.8, 7.0, 7.2, 7.3, 7.4, 7.6, 7.8, 8.0, 8.2]
delta_a_fish_population = [1500, 1480, 1460, 1440, 1420, 1400, 1380, 1370, 1350, 1320, 1300, 1280, 1260, 1240, 1220, 1200, 1180, 1150, 1130, 1100, 1080]
delta_a_water_clarity = [89, 87, 85, 83, 81, 78, 76, 74, 72, 70, 68, 65, 62, 60, 58, 56, 54, 53, 51, 49, 47]

fig, axs = plt.subplots(2, 1, figsize=(14, 12), sharex=True)

# Subplot 1: Pollution Levels
axs[0].plot(years, delta_a_pollution, color='green', linestyle='--', marker='^', linewidth=2)
axs[0].grid(True, linestyle='-', linewidth=0.5, alpha=0.9)

# Subplot 2: Water Clarity
axs[1].plot(years, delta_a_water_clarity, color='darkred', linestyle='-', marker='P', linewidth=2)
axs[1].grid(True, linestyle='-', linewidth=0.7, alpha=0.8)

plt.subplots_adjust(hspace=0.4)
plt.show()