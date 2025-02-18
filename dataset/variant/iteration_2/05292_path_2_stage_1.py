import matplotlib.pyplot as plt
import numpy as np

# Data for the bike-sharing program over one year (January to December)
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
checkouts = np.array([1500, 2300, 2800, 3500, 4300, 6000, 7400, 8100, 7600, 6500, 4800, 2900])
stations = np.array([10, 15, 20, 25, 30, 35, 35, 40, 40, 40, 40, 40])
subscriptions = np.array([300, 450, 550, 700, 750, 900, 1000, 1050, 1100, 1150, 1200, 1250])

fig, ax1 = plt.subplots(figsize=(10, 6))

# Updated plotting with different markers and line styles
ax1.plot(months, checkouts, color='navy', linestyle='-', marker='^', linewidth=2.5, label='Bike Checkouts')
ax1.set_xlabel('Month')
ax1.set_ylabel('Number of Checkouts', color='navy')
ax1.tick_params(axis='y', labelcolor='navy')
ax1.set_title("Evolution of Bike-Sharing Program Usage Over a Year", fontsize=16, fontweight='bold', pad=20)

# Secondary y-axis for station count and subscription numbers with altered styles
ax2 = ax1.twinx()
ax2.plot(months, stations, color='purple', linestyle='-.', marker='x', linewidth=1.5, label='Stations')
ax2.plot(months, subscriptions, color='teal', linestyle=':', marker='*', linewidth=3, label='Subscriptions')
ax2.set_ylabel('Number of Stations & Subscriptions', color='black')
ax2.tick_params(axis='y', labelcolor='black')

# Changed legend positioning and styling
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines1 + lines2, labels1 + labels2, loc='upper right', fontsize=9, frameon=False)

# Annotate with modified style
max_checkouts_month = months[np.argmax(checkouts)]
max_checkouts_value = max(checkouts)
ax1.annotate(f'Most Checkouts in {max_checkouts_month}', 
             xy=(max_checkouts_month, max_checkouts_value), 
             xytext=(8, max_checkouts_value + 1500),
             arrowprops=dict(facecolor='grey', arrowstyle='->'), fontsize=10, color='navy')

# Altered grid style
ax1.grid(True, which='both', linestyle=':', linewidth=0.7)
ax2.grid(False)

plt.tight_layout()
plt.show()