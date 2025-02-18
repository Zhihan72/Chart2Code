import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart displays the progression of bike-sharing program usage in a city over the span of a year.
# It delineates the variation on a monthly basis, showing the number of bike checkouts,
# station expansion, and user subscriptions. This chart provides an insightful look at how
# the program has evolved and its dynamic period over the months.

# Data for the bike-sharing program over one year (January to December)
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
checkouts = np.array([1500, 2300, 2800, 3500, 4300, 6000, 7400, 8100, 7600, 6500, 4800, 2900])
stations = np.array([10, 15, 20, 25, 30, 35, 35, 40, 40, 40, 40, 40])
subscriptions = np.array([300, 450, 550, 700, 750, 900, 1000, 1050, 1100, 1150, 1200, 1250])

# Create a figure with two subplots
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plotting bike checkouts using a line plot
ax1.plot(months, checkouts, color='blue', linestyle='-', marker='o', linewidth=2.5, label='Bike Checkouts')
ax1.set_xlabel('Month')
ax1.set_ylabel('Number of Checkouts', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.set_title("Evolution of Bike-Sharing Program Usage Over a Year",
              fontsize=16, fontweight='bold', pad=20)

# Adding a secondary y-axis for station count and subscription numbers
ax2 = ax1.twinx()
ax2.plot(months, stations, color='green', linestyle='--', marker='s', linewidth=2, label='Stations')
ax2.plot(months, subscriptions, color='orange', linestyle='-.', marker='d', linewidth=2, label='Subscriptions')
ax2.set_ylabel('Number of Stations & Subscriptions', color='black')
ax2.tick_params(axis='y', labelcolor='black')

# Adding legends to both plots
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

# Annotate highest checkout month
max_checkouts_month = months[np.argmax(checkouts)]
max_checkouts_value = max(checkouts)
ax1.annotate(f'Most Checkouts in {max_checkouts_month}', 
             xy=(max_checkouts_month, max_checkouts_value), 
             xytext=(8, max_checkouts_value + 1500),
             arrowprops=dict(facecolor='blue', arrowstyle='->'), fontsize=10, color='blue')

# Add grid to improve readability
ax1.grid(True, which='both', linestyle='--', linewidth=0.5)
ax2.grid(False)

# Adjust the layout to fit all elements
plt.tight_layout()

# Display the plot
plt.show()