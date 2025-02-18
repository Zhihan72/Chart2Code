import matplotlib.pyplot as plt
import numpy as np

# Data setup
days = np.array(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
probe_A = np.array([250, 245, 243, 240, 242, 244, 248])
probe_B = np.array([252, 247, 245, 243, 244, 247, 251])
probe_C = np.array([249, 245, 244, 241, 243, 246, 250])

# Plotting Script
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot data for all three lunar probes
ax1.plot(days, probe_A, '-o', color='tomato', markersize=6, linewidth=2, markerfacecolor='darkred')
ax1.plot(days, probe_B, '-s', color='mediumseagreen', markersize=6, linewidth=2, markerfacecolor='darkgreen')
ax1.plot(days, probe_C, '-^', color='cornflowerblue', markersize=6, linewidth=2, markerfacecolor='darkblue')

# Customize the main plot
ax1.set_xticks(np.arange(len(days)))
ax1.set_xticklabels(days)
ax1.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to better fit elements
plt.tight_layout()

# Display the plot
plt.show()