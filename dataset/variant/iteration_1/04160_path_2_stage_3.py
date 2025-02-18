import matplotlib.pyplot as plt
import numpy as np

months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
new_york_temps = np.array([-1, 0, 5, 12, 18, 24, 27, 26, 22, 16, 10, 3])
tokyo_temps = np.array([5, 6, 10, 15, 20, 24, 29, 30, 26, 20, 14, 8])
paris_temps = np.array([4, 5, 9, 12, 17, 21, 24, 23, 19, 14, 9, 5])
sydney_temps = np.array([26, 26, 24, 21, 18, 15, 14, 15, 17, 19, 22, 25])
avg_temps = (new_york_temps + tokyo_temps + paris_temps + sydney_temps) / 4

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 1]})

ax1.plot(months, new_york_temps, label="NY", linestyle='--', color='blue', marker='^')
ax1.plot(months, tokyo_temps, label="Tokyo", linestyle='-.', color='green', marker='*')
ax1.plot(months, paris_temps, label="Paris", linestyle='-', color='red', marker='p')
ax1.plot(months, sydney_temps, label="Sydney", linestyle=':', color='orange', marker='h')

cities_data = {'NY': new_york_temps, 'Tokyo': tokyo_temps, 'Paris': paris_temps, 'Sydney': sydney_temps}
colors = ['blue', 'green', 'red', 'orange']
for i, (city, temps) in enumerate(cities_data.items()):
    max_temp = max(temps)
    min_temp = min(temps)
    ax1.annotate(f'{max_temp}°C', xy=(months[temps.argmax()], max_temp), 
                 xytext=(months[temps.argmax()], max_temp + 3), ha='center',
                 color=colors[i], fontsize=10, arrowprops=dict(facecolor=colors[i], arrowstyle='->'))
    ax1.annotate(f'{min_temp}°C', xy=(months[temps.argmin()], min_temp), 
                 xytext=(months[temps.argmin()], min_temp - 5), ha='center',
                 color=colors[i], fontsize=10, arrowprops=dict(facecolor=colors[i], arrowstyle='->'))

ax1.set_title("2023 Temps - NY, Tokyo, Paris, Sydney", fontsize=16, fontweight='bold')
ax1.set_xlabel("Mo", fontsize=14)
ax1.set_ylabel("Temp (°C)", fontsize=14)
ax1.legend(loc="lower left", fontsize=12, frameon=False)
ax1.grid(True, linestyle='-', alpha=0.8)

ax2.plot(months, avg_temps, label="Avg Temp", linestyle='-', color='purple', marker='o')
ax2.axhline(y=avg_temps.mean(), color='grey', linestyle='--', linewidth=2, label="Yr Avg")

ax2.set_title("Avg Mo Temps - 2023", fontsize=14, fontweight='bold')
ax2.set_xlabel("Mo", fontsize=12)
ax2.set_ylabel("Avg Temp (°C)", fontsize=12)
ax2.legend(loc="lower left", fontsize=10, frameon=False)
ax2.grid(True, linestyle=':', alpha=0.9)

plt.tight_layout()
plt.show()