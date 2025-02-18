import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
city_a_temps = np.array([3, 4, 8, 12, 17, 22, 24, 23, 19, 14, 8, 4])
city_b_temps = np.array([5, 7, 12, 18, 24, 28, 30, 29, 25, 18, 11, 7])
city_c_temps = np.array([-1, 0, 5, 10, 15, 20, 22, 21, 17, 10, 5, 0])

fig, ax = plt.subplots(figsize=(14, 8))

# Use a consistent color for all city temperature plots
common_color = 'b'
ax.plot(months, city_a_temps, marker='o', linestyle='-', color=common_color)
ax.plot(months, city_b_temps, marker='s', linestyle='--', color=common_color)
ax.plot(months, city_c_temps, marker='d', linestyle='-.', color=common_color)

ax.grid(False)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.tight_layout()
plt.show()