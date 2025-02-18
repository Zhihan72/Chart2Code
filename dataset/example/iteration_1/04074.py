import numpy as np
import matplotlib.pyplot as plt

# Time period in days (three months)
days = np.arange(0, 91, 1)

# Hypothetical data for the Mars rover "Pathfinder" mission
battery_usage = 100 - 0.5*days  # Battery draining slowly over time
signal_strength = np.clip(100 - (0.8 * days) + 5*np.sin(0.1*days), 0, 100)  # Oscillating signal strength
discovery_rate = np.clip(5 + 0.2 * days + 0.5*np.sin(0.5*days), 0, 20)  # Increasing discoveries over time
temperature_readings = -60 + 10*np.sin(0.1*days)  # Simulating temperature around -60°C with some variance

# Setting up the plot
fig, ax1 = plt.subplots(figsize=(14, 7))

# Plotting battery usage on the primary y-axis
ax1.plot(days, battery_usage, 'g-', label='Battery Usage (%)', linewidth=2)
ax1.set_xlabel('Days since mission start', fontsize=12)
ax1.set_ylabel('Battery Usage (%)', color='g', fontsize=12)
ax1.tick_params(axis='y', labelcolor='g')

# Creating a second y-axis to plot signal strength
ax2 = ax1.twinx()
ax2.plot(days, signal_strength, 'b-', label='Signal Strength (%)', linewidth=2)
ax2.set_ylabel('Signal Strength (%)', color='b', fontsize=12)
ax2.tick_params(axis='y', labelcolor='b')

# Creating a third y-axis to plot discovery rate and temperature readings
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 70))  # Offset the third y-axis
ax3.plot(days, discovery_rate, 'r-', label='Discovery Rate (finds/day)', linewidth=2)
ax3.set_ylabel('Discovery Rate (finds/day)', color='r', fontsize=12)
ax3.tick_params(axis='y', labelcolor='r')

ax4 = ax1.twinx()
ax4.spines['right'].set_position(('outward', 140))  # Offset the fourth y-axis
ax4.plot(days, temperature_readings, 'k-.', label='Temperature (°C)', linewidth=2)
ax4.set_ylabel('Temperature (°C)', color='k', fontsize=12)
ax4.tick_params(axis='y', labelcolor='k')

# Combining all labels into one legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines3, labels3 = ax3.get_legend_handles_labels()
lines4, labels4 = ax4.get_legend_handles_labels()

ax1.legend(lines1 + lines2 + lines3 + lines4, labels1 + labels2 + labels3 + labels4, loc='upper right', fontsize=12)

# Adding title with line breaks for readability
plt.title('Mars Rover "Pathfinder" Mission: \nBattery, Signal, Discovery, and Temperature Analysis\n(Three-Month Period)', 
          fontsize=16, fontweight='bold', pad=20)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()