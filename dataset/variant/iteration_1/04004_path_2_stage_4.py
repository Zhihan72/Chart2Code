import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Mar', 'Jul', 'Jan', 'Oct', 'Apr', 'Dec', 'Jun', 'Sep', 'Feb', 'May', 'Nov', 'Aug'])
la_temps = np.array([14, 15, 17, 19, 22, 24, 27, 27, 26, 22, 18, 15])
ny_temps = np.array([0, 1, 7, 13, 19, 24, 27, 26, 22, 15, 10, 4])
chicago_temps = np.array([-3, 0, 6, 12, 18, 23, 26, 25, 20, 13, 6, -1])

# Added fictional data for two new cities.
fictional_city_a_temps = np.array([10, 14, 16, 18, 21, 23, 26, 27, 24, 20, 15, 12])
fictional_city_b_temps = np.array([5, 7, 10, 15, 19, 22, 25, 24, 21, 17, 11, 6])

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(months, la_temps, marker='v', linestyle='--', color='blue', label='L.A.', linewidth=1.5)
ax.plot(months, ny_temps, marker='s', linestyle='-', color='red', label='NYC', linewidth=2.5)
ax.plot(months, chicago_temps, marker='d', linestyle='-.', color='green', label='Chi-town', linewidth=2)

# Plotting the additional data series for Fictional City A and B
ax.plot(months, fictional_city_a_temps, marker='o', linestyle=':', color='purple', label='Fictional City A', linewidth=1.5)
ax.plot(months, fictional_city_b_temps, marker='x', linestyle='-', color='orange', label='Fictional City B', linewidth=2)

ax.set_title("Temperature Trends Across Cities", fontsize=18, weight='bold', pad=20)
ax.set_xlabel("Month", fontsize=14)
ax.set_ylabel("Average Temperature (°C)", fontsize=14)
ax.set_ylim(-5, 30)
ax.grid(True, linestyle=':', alpha=0.8)

# Adding annotations for the fictional data series.
for i, txt in enumerate(la_temps):
    ax.text(months[i], la_temps[i] + 0.2, str(txt), ha='center', fontsize=9, color='blue')
for i, txt in enumerate(ny_temps):
    ax.text(months[i], ny_temps[i] + 0.2, str(txt), ha='center', fontsize=9, color='red')
for i, txt in enumerate(chicago_temps):
    ax.text(months[i], chicago_temps[i] + 0.2, str(txt), ha='center', fontsize=9, color='green')
for i, txt in enumerate(fictional_city_a_temps):
    ax.text(months[i], fictional_city_a_temps[i] + 0.2, str(txt), ha='center', fontsize=9, color='purple')
for i, txt in enumerate(fictional_city_b_temps):
    ax.text(months[i], fictional_city_b_temps[i] + 0.2, str(txt), ha='center', fontsize=9, color='orange')

ax.legend(title='Cities', title_fontsize='13', fontsize='10', loc='lower right', frameon=False)

plt.tight_layout()
plt.show()