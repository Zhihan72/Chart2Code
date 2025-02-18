import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
city_a_temps = np.array([2.0, 4.1, 9.3, 13.4, 18.2, 22.3, 25.6, 25.3, 20.1, 14.0, 8.1, 3.2])
city_b_temps = np.array([-5.0, -2.8, 2.5, 10.1, 15.3, 19.8, 23.4, 22.9, 16.5, 9.0, 1.2, -3.7])

avg_city_a = np.mean(city_a_temps)
avg_city_b = np.mean(city_b_temps)

fig, ax = plt.subplots(figsize=(10, 6))

# Changed colors to new ones
ax.plot(months, city_a_temps, marker='x', color='#1f77b4', linestyle='-.', linewidth=2)  # Updated color
ax.plot(months, city_b_temps, marker='d', color='#ff7f0e', linestyle=':', linewidth=2)  # Updated color

ax.axhline(y=avg_city_a, color='#1f77b4', linestyle='-', linewidth=1.5, alpha=0.6)  # Updated color
ax.axhline(y=avg_city_b, color='#ff7f0e', linestyle='-', linewidth=1.5, alpha=0.6)  # Updated color

ax.grid(visible=True, which='both', linestyle='-', linewidth=0.5, color='black', alpha=0.5)
ax.set_xticks(months)
ax.set_yticks(np.arange(-10, 31, 5))
ax.set_ylim(-12, 30)

plt.tight_layout()
plt.show()