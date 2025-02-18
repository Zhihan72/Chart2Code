import matplotlib.pyplot as plt
import numpy as np

months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
new_york_temps = np.array([-1, 0, 5, 12, 18, 24, 27, 26, 22, 16, 10, 3])
tokyo_temps = np.array([5, 6, 10, 15, 20, 24, 29, 30, 26, 20, 14, 8])
paris_temps = np.array([4, 5, 9, 12, 17, 21, 24, 23, 19, 14, 9, 5])

avg_temps = (new_york_temps + tokyo_temps + paris_temps) / 3

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 1]})

# Changed color assignment for shuffling
ax1.plot(months, new_york_temps, label="New York", linestyle='-', color='red', marker='o')
ax1.plot(months, tokyo_temps, label="Tokyo", linestyle='-', color='blue', marker='s')
ax1.plot(months, paris_temps, label="Paris", linestyle='-', color='green', marker='^')

cities_data = {'New York': new_york_temps, 'Tokyo': tokyo_temps, 'Paris': paris_temps}
colors = ['red', 'blue', 'green']  # Adjusted colors to match the plot changes
markers = ['o', 's', '^']
for i, (city, temps) in enumerate(cities_data.items()):
    max_temp = max(temps)
    min_temp = min(temps)
    ax1.annotate(f'High: {max_temp}°C', xy=(months[temps.argmax()], max_temp), 
                 xytext=(months[temps.argmax()], max_temp + 3), ha='center',
                 color=colors[i], fontsize=10, arrowprops=dict(facecolor=colors[i], arrowstyle='->'))
    ax1.annotate(f'Low: {min_temp}°C', xy=(months[temps.argmin()], min_temp), 
                 xytext=(months[temps.argmin()], min_temp - 5), ha='center',
                 color=colors[i], fontsize=10, arrowprops=dict(facecolor=colors[i], arrowstyle='->'))

ax1.set_title("Monthly Temperature Variation in 2023 - New York, Tokyo, and Paris", fontsize=16, fontweight='bold')
ax1.set_xlabel("Month", fontsize=14)
ax1.set_ylabel("Temperature (°C)", fontsize=14)
ax1.legend(loc="upper right", fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.6)

ax2.plot(months, avg_temps, label="Average Temperature", linestyle='--', color='purple', marker='d')
ax2.axhline(y=avg_temps.mean(), color='orange', linestyle='-', linewidth=2, label="Year Average")

ax2.set_title("Average Monthly Temperature - 2023", fontsize=14, fontweight='bold')
ax2.set_xlabel("Month", fontsize=12)
ax2.set_ylabel("Average Temperature (°C)", fontsize=12)
ax2.legend(loc="upper right", fontsize=10)
ax2.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()