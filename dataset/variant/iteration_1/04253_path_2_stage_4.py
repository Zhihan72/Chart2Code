import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)
city_alpha_temp = np.array([30, 32, 35, 40, 45, 50, 55, 54, 48, 42, 35, 31])
# Removed the data for city_bravo_temp and city_charlie_temp

plt.figure(figsize=(14, 8))

plt.plot(months, city_alpha_temp, linestyle='--', marker='v', color='blue', linewidth=2.5)
# Removed the plotting commands for city_bravo_temp and city_charlie_temp

plt.grid(True, linestyle='-', alpha=0.7)

plt.ylim(0, 70)
plt.xlim(1, 12)

plt.xticks(months, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

plt.legend(['City Alpha'], loc='upper right')
# Removed the legend entries for City Bravo and City Charlie
plt.tight_layout()

plt.show()