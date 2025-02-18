import matplotlib.pyplot as plt
import numpy as np

# Define months for the data
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Existing rainfall data in mm for each city over one year
city_a = np.array([80, 70, 75, 60, 55, 65, 85, 90, 70, 80, 95, 100])
city_b = np.array([90, 80, 85, 75, 65, 75, 95, 100, 90, 95, 110, 105])
city_c = np.array([60, 55, 50, 45, 50, 55, 65, 70, 60, 65, 70, 75])

# Additional made-up rainfall data for two new cities
city_d = np.array([50, 45, 55, 50, 60, 70, 80, 85, 75, 80, 85, 90])
city_e = np.array([100, 95, 105, 95, 80, 85, 90, 95, 110, 115, 120, 125])

# Stack the updated data for plotting
data = np.vstack([city_a, city_b, city_c, city_d, city_e])

# Plot the stacked area chart with additional cities
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(months, data, labels=['City A', 'City B', 'City C', 'City D', 'City E'],
             colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], alpha=0.8)

# Customize the plot
ax.set_title("Monthly Rainfall Pattern Analysis\nfor Five Cities in 2021", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Months", fontsize=12, weight='bold')
ax.set_ylabel("Rainfall (mm)", fontsize=12, weight='bold')
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=10, title='Cities')
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Show y-ticks with grid lines for readability
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)} mm'))
ax.set_xticks(np.arange(len(months)))
ax.set_xticklabels(months, fontsize=10, rotation=45)
ax.set_yticks(np.arange(0, 501, 50))  # Updated to accommodate more data
ax.set_yticklabels(np.arange(0, 501, 50), fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()