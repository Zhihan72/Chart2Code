import numpy as np
import matplotlib.pyplot as plt

days = np.arange(0, 91, 1)

# Mars rover "Pathfinder" mission data
battery_usage = 100 - 0.5 * days
signal_strength = np.clip(100 - (0.8 * days) + 5 * np.sin(0.1*days), 0, 100)
discovery_rate = np.clip(5 + 0.2 * days + 0.5 * np.sin(0.5*days), 0, 20)
temperature_readings = -60 + 10 * np.sin(0.1 * days)

fig, ax1 = plt.subplots(figsize=(14, 7))

ax1.plot(days, battery_usage, 'g-', label='Battery Level Check', linewidth=2)
ax1.set_xlabel('Timeline (Days)', fontsize=12)
ax1.set_ylabel('Battery Capacity (%)', color='g', fontsize=12)
ax1.tick_params(axis='y', labelcolor='g')

ax2 = ax1.twinx()
ax2.plot(days, signal_strength, 'b-', label='Signal Intensity', linewidth=2)
ax2.set_ylabel('Signal Intensity (%)', color='b', fontsize=12)
ax2.tick_params(axis='y', labelcolor='b')

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 70))
ax3.plot(days, discovery_rate, 'r-', label='Findings Rate (units/day)', linewidth=2)
ax3.set_ylabel('Find Rate (units/day)', color='r', fontsize=12)
ax3.tick_params(axis='y', labelcolor='r')

ax4 = ax1.twinx()
ax4.spines['right'].set_position(('outward', 140))
ax4.plot(days, temperature_readings, 'k-.', label='Temp Readings (C)', linewidth=2)
ax4.set_ylabel('Surrounding Temp (C)', color='k', fontsize=12)
ax4.tick_params(axis='y', labelcolor='k')

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines3, labels3 = ax3.get_legend_handles_labels()
lines4, labels4 = ax4.get_legend_handles_labels()

ax1.legend(lines1 + lines2 + lines3 + lines4, labels1 + labels2 + labels3 + labels4, loc='upper right', fontsize=12)

plt.title('Pathfinder Mission Analysis: \nBattery-Level, Signal, Findings, and Temp Overview\n(90 Days)', 
          fontsize=16, fontweight='bold', pad=20)

plt.tight_layout()
plt.show()