import numpy as np
import matplotlib.pyplot as plt

days = np.arange(0, 91, 1)

battery_usage = 100 - 0.5*days
signal_strength = np.clip(100 - (0.8 * days) + 5*np.sin(0.1*days), 0, 100)
discovery_rate = np.clip(5 + 0.2 * days + 0.5*np.sin(0.5*days), 0, 20)
temperature_readings = -60 + 10*np.sin(0.1*days)

fig, ax1 = plt.subplots(figsize=(14, 7))

# Updated Line Colors
ax1.plot(days, battery_usage, '-', color='purple', label='Battery Usage (%)', linewidth=2)
ax1.set_xlabel('Days since mission start', fontsize=12)
ax1.set_ylabel('Battery Usage (%)', color='purple', fontsize=12)
ax1.tick_params(axis='y', labelcolor='purple')

ax2 = ax1.twinx()
ax2.plot(days, signal_strength, '-', color='orange', label='Signal Strength (%)', linewidth=2)
ax2.set_ylabel('Signal Strength (%)', color='orange', fontsize=12)
ax2.tick_params(axis='y', labelcolor='orange')

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 70))
ax3.plot(days, discovery_rate, '-', color='teal', label='Discovery Rate (finds/day)', linewidth=2)
ax3.set_ylabel('Discovery Rate (finds/day)', color='teal', fontsize=12)
ax3.tick_params(axis='y', labelcolor='teal')

ax4 = ax1.twinx()
ax4.spines['right'].set_position(('outward', 140))
ax4.plot(days, temperature_readings, '-.', color='brown', label='Temperature (°C)', linewidth=2)
ax4.set_ylabel('Temperature (°C)', color='brown', fontsize=12)
ax4.tick_params(axis='y', labelcolor='brown')

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines3, labels3 = ax3.get_legend_handles_labels()
lines4, labels4 = ax4.get_legend_handles_labels()

ax1.legend(lines1 + lines2 + lines3 + lines4, labels1 + labels2 + labels3 + labels4, loc='upper right', fontsize=12)

plt.title('Mars Rover "Pathfinder" Mission: \nBattery, Signal, Discovery, and Temperature Analysis\n(Three-Month Period)', 
          fontsize=16, fontweight='bold', pad=20)

plt.tight_layout()
plt.show()