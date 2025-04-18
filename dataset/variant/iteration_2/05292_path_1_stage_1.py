import matplotlib.pyplot as plt
import numpy as np

# Data for the bike-sharing program over one year (January to December)
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
checkouts = np.array([1500, 2300, 2800, 3500, 4300, 6000, 7400, 8100, 7600, 6500, 4800, 2900])
stations = np.array([10, 15, 20, 25, 30, 35, 35, 40, 40, 40, 40, 40])
subscriptions = np.array([300, 450, 550, 700, 750, 900, 1000, 1050, 1100, 1150, 1200, 1250])

fig, ax1 = plt.subplots(figsize=(10, 6))

# Alterations: Changed line styles and markers for stylistic variance
ax1.plot(months, checkouts, color='darkred', linestyle='-', marker='x', linewidth=2.5, label='Bike Checkouts')
ax1.set_xlabel('Month')
ax1.set_ylabel('Number of Checkouts', color='darkred')
ax1.tick_params(axis='y', labelcolor='darkred')
ax1.set_title("Evolution of Bike-Sharing Program Usage Over the Year",
              fontsize=16, fontweight='bold', pad=20)

# Alternate representation for stations and subscriptions
ax2 = ax1.twinx()
ax2.plot(months, stations, color='purple', linestyle='-.', marker='v', linewidth=2, label='Stations')
ax2.plot(months, subscriptions, color='brown', linestyle=':', marker='^', linewidth=2, label='Subscriptions')
ax2.set_ylabel('Number of Stations & Subscriptions', color='black')
ax2.tick_params(axis='y', labelcolor='black')

# Change legend position and styling
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines1 + lines2, labels1 + labels2, loc='lower center', fontsize=9, borderpad=1)

# Annotate with different style
max_checkouts_month = months[np.argmax(checkouts)]
max_checkouts_value = max(checkouts)
ax1.annotate(f'Most Checkouts in {max_checkouts_month}', 
             xy=(max_checkouts_month, max_checkouts_value), 
             xytext=(8, max_checkouts_value + 1500),
             arrowprops=dict(facecolor='darkred', arrowstyle='->'), fontsize=10, color='darkred')

# Adjust grid styling for clarity
ax1.grid(True, which='major', linestyle='-', linewidth=0.75)
ax2.grid(False)

plt.tight_layout()
plt.show()