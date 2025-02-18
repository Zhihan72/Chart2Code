import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)
city_alpha_temp = np.array([30, 32, 35, 40, 45, 50, 55, 54, 48, 42, 35, 31])
city_bravo_temp = np.array([20, 25, 30, 40, 50, 60, 65, 64, 55, 45, 30, 22])
city_charlie_temp = np.array([10, 15, 20, 25, 30, 35, 40, 38, 32, 26, 20, 15])

plt.figure(figsize=(14, 8))

plt.plot(months, city_alpha_temp, marker='o', color='coral', linewidth=2)
plt.plot(months, city_bravo_temp, marker='s', color='dodgerblue', linewidth=2)
plt.plot(months, city_charlie_temp, marker='^', color='limegreen', linewidth=2)

plt.grid(True, linestyle='--', alpha=0.5)

plt.ylim(0, 70)
plt.xlim(1, 12)

plt.xticks(months, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

plt.tight_layout()

plt.show()