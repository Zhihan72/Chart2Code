import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart describes the cosmic findings of a hypothetical space mission, named the "Lunar Oscillation Project". 
# The line chart shows the variation in lunar surface temperature over a week as measured by three different lunar probes.

# Data setup
days = np.array(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
probe_A = np.array([250, 245, 243, 240, 242, 244, 248])  # temperature in Kelvin
probe_B = np.array([252, 247, 245, 243, 244, 247, 251])
probe_C = np.array([249, 245, 244, 241, 243, 246, 250])

# Plotting Script
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot data for all three lunar probes
ax1.plot(days, probe_A, '-o', label='Probe A', color='tomato', markersize=6, linewidth=2, markerfacecolor='darkred')
ax1.plot(days, probe_B, '-s', label='Probe B', color='mediumseagreen', markersize=6, linewidth=2, markerfacecolor='darkgreen')
ax1.plot(days, probe_C, '-^', label='Probe C', color='cornflowerblue', markersize=6, linewidth=2, markerfacecolor='darkblue')

# Annotate a significant observation
ax1.annotate('Sudden drop in mid-week', 
             xy=('Wed', 243), 
             xytext=('Thu', 245), 
             arrowprops=dict(arrowstyle='->', color='black'),
             fontsize=12, 
             bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightyellow'))

# Customize the main plot
ax1.set_title('Lunar Oscillation Project: Weekly Lunar Surface Temperature', fontsize=16, fontweight='bold', loc='center')
ax1.set_xlabel('Day of the Week', fontsize=14)
ax1.set_ylabel('Temperature (K)', fontsize=14)
ax1.set_xticks(np.arange(len(days)))
ax1.set_xticklabels(days)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend(loc='upper right', fontsize=12, frameon=False)

# Adjust layout to better fit elements
plt.tight_layout()

# Display the plot
plt.show()