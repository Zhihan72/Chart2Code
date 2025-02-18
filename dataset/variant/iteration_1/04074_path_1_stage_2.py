import numpy as np
import matplotlib.pyplot as plt

days = np.arange(0, 91, 1)

battery_usage = 100 - 0.5*days
signal_strength = np.clip(100 - (0.8 * days) + 5*np.sin(0.1*days), 0, 100)
discovery_rate = np.clip(5 + 0.2 * days + 0.5*np.sin(0.5*days), 0, 20)
temperature_readings = -60 + 10*np.sin(0.1*days)

fig, ax1 = plt.subplots(figsize=(14, 7))

# Altered Marker Styles, Linestyles and Colors
ax1.plot(days, battery_usage, 'o-', color='green', label='Battery Usage (%)', linewidth=1)
ax1.set_xlabel('Days since mission start', fontsize=10)
ax1.set_ylabel('Battery Usage (%)', color='green', fontsize=10)
ax1.tick_params(axis='y', labelcolor='green')

ax2 = ax1.twinx()
ax2.plot(days, signal_strength, 'x--', color='red', label='Signal Strength (%)', linewidth=1)
ax2.set_ylabel('Signal Strength (%)', color='red', fontsize=10)
ax2.tick_params(axis='y', labelcolor='red')

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 70))
ax3.plot(days, discovery_rate, 's:', color='blue', label='Discovery Rate (finds/day)', linewidth=1)
ax3.set_ylabel('Discovery Rate (finds/day)', color='blue', fontsize=10)
ax3.tick_params(axis='y', labelcolor='blue')

ax4 = ax1.twinx()
ax4.spines['right'].set_position(('outward', 140))
ax4.plot(days, temperature_readings, 'd-.', color='black', label='Temperature (°C)', linewidth=1)
ax4.set_ylabel('Temperature (°C)', color='black', fontsize=10)
ax4.tick_params(axis='y', labelcolor='black')

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines3, labels3 = ax3.get_legend_handles_labels()
lines4, labels4 = ax4.get_legend_handles_labels()

# Changed legend location
ax1.legend(lines1 + lines2 + lines3 + lines4, labels1 + labels2 + labels3 + labels4, loc='upper left', fontsize=10)

# Added grid lines and altered title
ax1.grid(True, linestyle='--', linewidth=0.5)
plt.title('Exploratory Analysis: Battery, Signal, Discovery, Temp\n(Three-Month Period)', fontsize=14, fontweight='normal', pad=10)

plt.tight_layout()
plt.show()