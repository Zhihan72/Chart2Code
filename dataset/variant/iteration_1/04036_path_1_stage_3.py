import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
city_a_temps = np.array([2.0, 4.1, 9.3, 13.4, 18.2, 22.3, 25.6, 25.3, 20.1, 14.0, 8.1, 3.2])

avg_city_a = np.mean(city_a_temps)

fig, ax = plt.subplots(figsize=(10, 6))

# Using a single consistent color across all plotting elements
consistent_color = '#1f77b4'

ax.plot(months, city_a_temps, marker='o', color=consistent_color, linewidth=2)
ax.axhline(y=avg_city_a, color=consistent_color, linestyle='--', linewidth=1.5, alpha=0.7)

ax.grid(visible=True, which='both', linestyle='--', linewidth=0.6, color='grey', alpha=0.7)
ax.set_xticks(months)
ax.set_yticks(np.arange(-10, 31, 5))
ax.set_ylim(-10, 30)

plt.tight_layout()
plt.show()