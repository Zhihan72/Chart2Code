import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)
city_a_temps = [5, 7, 10, 15, 20, 25, 28, 27, 23, 17, 10, 6]
city_c_temps = [12, 12, 15, 18, 22, 25, 30, 31, 28, 24, 20, 15]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(months, city_a_temps, marker='s', linestyle='--', color='coral', linewidth=2)
ax.plot(months, city_c_temps, marker='d', linestyle='-.', color='green', linewidth=2)

ax.grid(True, linestyle=':', alpha=0.9)

plt.xticks(months, fontsize=10)

plt.tight_layout()
plt.show()