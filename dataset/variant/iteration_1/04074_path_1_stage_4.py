import numpy as np
import matplotlib.pyplot as plt

days = np.arange(0, 93, 1)

battery_usage = np.array([100, 99.5, 99, 98.5, 98, 97.5, 97, 96.5, 96, 95.5, 95, 94.5, 
                          94, 93.5, 93, 92.5, 92, 91.5, 91, 90.5, 90, 89.5, 89, 88.5, 88, 
                          87.5, 87, 86.5, 86, 85.5, 84, 85, 83.5, 83, 82.5, 82, 81.5, 81, 
                          80.5, 80, 79.5, 79, 78.5, 78, 77.5, 77, 76.5, 76, 75.5, 75, 74.5, 
                          74, 73.5, 73, 72.5, 72, 71.5, 71, 70.5, 70, 69.5, 68, 68.5, 67.5, 
                          67, 66.5, 66, 65.5, 65, 64.5, 64, 63.5, 63, 62.5, 62, 61.5, 61, 
                          60.5, 60, 59.5, 59, 58.5, 58, 57.5, 57, 56.5, 56, 55.5, 55, 54.5, 
                          54, 53.5, 53])

signal_strength = np.clip(100 - (0.8 * days) + 5*np.sin(0.1*days) + (days % 3 - 1), 0, 100)
discovery_rate = np.clip(5 + 0.2 * days + 0.5*np.sin(0.5*days), 0, 20)
temperature_readings = -60 + 10*np.sin(0.1*days)

fig, ax1 = plt.subplots(figsize=(14, 7))

ax1.plot(days, battery_usage, 'o-', color='green', label='Battery (%)', linewidth=1)
ax1.set_xlabel('Days', fontsize=10)
ax1.set_ylabel('Battery (%)', color='green', fontsize=10)
ax1.tick_params(axis='y', labelcolor='green')

ax2 = ax1.twinx()
ax2.plot(days, signal_strength, 'x--', color='red', label='Signal (%)', linewidth=1)
ax2.set_ylabel('Signal (%)', color='red', fontsize=10)
ax2.tick_params(axis='y', labelcolor='red')

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 70))
ax3.plot(days, discovery_rate, 's:', color='blue', label='Discoveries/day', linewidth=1)
ax3.set_ylabel('Discoveries/day', color='blue', fontsize=10)
ax3.tick_params(axis='y', labelcolor='blue')

ax4 = ax1.twinx()
ax4.spines['right'].set_position(('outward', 140))
ax4.plot(days, temperature_readings, 'd-.', color='black', label='Temp (°C)', linewidth=1)
ax4.set_ylabel('Temp (°C)', color='black', fontsize=10)
ax4.tick_params(axis='y', labelcolor='black')

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines3, labels3 = ax3.get_legend_handles_labels()
lines4, labels4 = ax4.get_legend_handles_labels()

ax1.legend(lines1 + lines2 + lines3 + lines4, labels1 + labels2 + labels3 + labels4, loc='upper left', fontsize=10)

ax1.grid(True, linestyle='--', linewidth=0.5)
plt.title('3-Month Analysis: Battery, Signal, Discoveries, Temp', fontsize=14, fontweight='normal', pad=10)

plt.tight_layout()
plt.show()