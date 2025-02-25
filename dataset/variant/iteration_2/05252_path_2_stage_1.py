import matplotlib.pyplot as plt
import numpy as np

# Define months
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Rainfall data in mm for each city over one year
city_a = np.array([80, 70, 75, 60, 55, 65, 85, 90, 70, 80, 95, 100])
city_b = np.array([90, 80, 85, 75, 65, 75, 95, 100, 90, 95, 110, 105])
city_c = np.array([60, 55, 50, 45, 50, 55, 65, 70, 60, 65, 70, 75])

# Stack the data for plotting
data = np.vstack([city_a, city_b, city_c])

# Plot the stacked area chart
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(months, data, labels=['City A', 'City B', 'City C'], colors=['#ff7f0e', '#2ca02c', '#1f77b4'], alpha=0.7)

# Customize the plot
ax.set_title("2021 Monthly Rainfall Pattern for Cities", fontsize=17, fontweight='bold', pad=25)
ax.set_xlabel("Month", fontsize=11, weight='bold')
ax.set_ylabel("Rainfall/mm", fontsize=11, weight='bold')
ax.legend(loc='upper left', frameon=False, fontsize=9, title='City Names', title_fontsize='11')
ax.grid(True, which='both', linestyle='-.', linewidth=0.6, alpha=0.6)

# Show y-ticks with grid lines for readability
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)} mm'))
ax.set_xticks(np.arange(len(months)))
ax.set_xticklabels(months, fontsize=9, rotation=40)
ax.set_yticks(np.arange(0, 301, 60))
ax.set_yticklabels(np.arange(0, 301, 60), fontsize=9)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()