import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)
city_alpha_temp = np.array([30, 32, 35, 40, 45, 50, 55, 54, 48, 42, 35, 31])
city_bravo_temp = np.array([20, 25, 30, 40, 50, 60, 65, 64, 55, 45, 30, 22])
city_charlie_temp = np.array([10, 15, 20, 25, 30, 35, 40, 38, 32, 26, 20, 15])

plt.figure(figsize=(14, 8))

plt.plot(months, city_alpha_temp, label='Alpha', marker='x', color='teal', linestyle='-.', linewidth=1.5)
plt.plot(months, city_bravo_temp, label='Bravo', marker='*', color='orange', linestyle=':', linewidth=2.5)
plt.plot(months, city_charlie_temp, label='Charlie', marker='D', color='magenta', linestyle='-', linewidth=1)

plt.grid(True, linestyle='-', color='gray', alpha=0.3)

plt.title("Temp Trends in Cities", fontsize=16, pad=20)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Temp (°C)", fontsize=14)

plt.annotate('Peak', xy=(6, city_alpha_temp[5]), xytext=(8, 58),
             arrowprops=dict(facecolor='red', arrowstyle='fancy'),
             fontsize=12)

plt.annotate('Cold', xy=(12, city_bravo_temp[11]), xytext=(10, 15),
             arrowprops=dict(facecolor='blue', arrowstyle='wedge,tail_width=0.7'),
             fontsize=12, rotation=15)

plt.annotate('Steady', xy=(8, city_charlie_temp[7]), xytext=(5, 42),
             arrowprops=dict(facecolor='green', arrowstyle='simple'),
             fontsize=12, rotation=-15)

plt.ylim(0, 70)
plt.xlim(1, 12)
plt.xticks(months, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

plt.legend(loc='lower left', fontsize=12, shadow=True, fancybox=True)

plt.tight_layout()

plt.show()