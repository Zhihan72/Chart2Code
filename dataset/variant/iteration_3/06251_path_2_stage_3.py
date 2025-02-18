import matplotlib.pyplot as plt
import numpy as np

# Data setup
days = np.array(['Wed', 'Fri', 'Tue', 'Mon', 'Sat', 'Thu', 'Sun'])
probe_A = np.array([250, 245, 243, 240, 242, 244, 248])
probe_B = np.array([252, 247, 245, 243, 244, 247, 251])

fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot data for two lunar probes
ax1.plot(days, probe_A, ':x', label='Unit Alpha', color='tomato', markersize=8, linewidth=2, markerfacecolor='none')
ax1.plot(days, probe_B, '--^', label='Unit Bravo', color='mediumseagreen', markersize=8, linewidth=2, markerfacecolor='darkgreen')

# Annotate a significant observation
ax1.annotate('Midweek Temperature Dip', 
             xy=('Tue', 243), 
             xytext=('Thu', 245), 
             arrowprops=dict(arrowstyle='->', color='gray'),
             fontsize=12, 
             bbox=dict(boxstyle="round,pad=0.3", edgecolor='blue', facecolor='lightcyan'))

# Customize the main plot
ax1.set_title('Lunar Temperature: Weekly Fluctuations of Surface', fontsize=16, fontweight='bold', loc='left')
ax1.set_xlabel('Weekdays Observed', fontsize=14)
ax1.set_ylabel('Kelvin Temperature', fontsize=14)
ax1.set_xticks(np.arange(len(days)))
ax1.set_xticklabels(days)
ax1.grid(True, linestyle='-', alpha=0.5)
ax1.legend(loc='lower left', fontsize=10, frameon=True)

plt.tight_layout()
plt.show()