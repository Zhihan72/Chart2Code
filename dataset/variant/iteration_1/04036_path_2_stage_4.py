import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
# Manually shuffled temperature data for demonstration
city_a_temps = np.array([4.1, 2.0, 13.4, 9.3, 22.3, 18.2, 3.2, 25.3, 25.6, 20.1, 14.0, 8.1]) # shuffled values
city_b_temps = np.array([15.3, -5.0, 22.9, 10.1, -2.8, 23.4, -3.7, 1.2, 16.5, 19.8, 2.5, 9.0]) # shuffled values

avg_city_a = np.mean(city_a_temps)
avg_city_b = np.mean(city_b_temps)

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(months, city_a_temps, marker='x', color='#1f77b4', linestyle='-.', linewidth=2)
ax.plot(months, city_b_temps, marker='d', color='#ff7f0e', linestyle=':', linewidth=2)

ax.axhline(y=avg_city_a, color='#1f77b4', linestyle='-', linewidth=1.5, alpha=0.6)
ax.axhline(y=avg_city_b, color='#ff7f0e', linestyle='-', linewidth=1.5, alpha=0.6)

ax.grid(visible=True, which='both', linestyle='-', linewidth=0.5, color='black', alpha=0.5)
ax.set_xticks(months)
ax.set_yticks(np.arange(-10, 31, 5))
ax.set_ylim(-12, 30)

plt.tight_layout()
plt.show()