import matplotlib.pyplot as plt
import numpy as np

months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
new_york_temps = np.array([-1, 0, 5, 12, 18, 24, 27, 26, 22, 16, 10, 3])
paris_temps = np.array([4, 5, 9, 12, 17, 21, 24, 23, 19, 14, 9, 5])

avg_temps = (new_york_temps + paris_temps) / 2

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 1]})

ax1.plot(months, new_york_temps, label="NY", linestyle='--', color='blue', marker='s')
ax1.plot(months, paris_temps, label="Paris", linestyle='-.', color='magenta', marker='*')

cities_data = {'NY': new_york_temps, 'Paris': paris_temps}
colors = ['blue', 'magenta']
markers = ['s', '*']

for i, (city, temps) in enumerate(cities_data.items()):
    max_temp = max(temps)
    min_temp = min(temps)
    ax1.annotate(f'H: {max_temp}°C', xy=(months[temps.argmax()], max_temp), 
                 xytext=(months[temps.argmax()], max_temp + 3), ha='center',
                 color=colors[i], fontsize=10, arrowprops=dict(facecolor=colors[i], arrowstyle='->'))
    ax1.annotate(f'L: {min_temp}°C', xy=(months[temps.argmin()], min_temp), 
                 xytext=(months[temps.argmin()], min_temp - 5), ha='center',
                 color=colors[i], fontsize=10, arrowprops=dict(facecolor=colors[i], arrowstyle='->'))

ax1.set_title("Monthly Temps 2023 - NY, Paris", fontsize=16, fontweight='bold')
ax1.set_xlabel("Mo", fontsize=14)
ax1.set_ylabel("Temp (°C)", fontsize=14)
ax1.legend(loc="lower left", fontsize=12)
ax1.grid(True, linestyle='-.', alpha=0.7)

ax2.plot(months, avg_temps, label="Avg Temp", linestyle=':', color='orange', marker='x')
ax2.axhline(y=avg_temps.mean(), color='cyan', linestyle='-', linewidth=2, label="Year Avg")

ax2.set_title("Avg Monthly Temp - 2023", fontsize=14, fontweight='bold')
ax2.set_xlabel("Mo", fontsize=12)
ax2.set_ylabel("Avg Temp (°C)", fontsize=12)
ax2.legend(loc="upper left", fontsize=10)
ax2.grid(True, linestyle='-', alpha=0.5)

plt.tight_layout()
plt.show()