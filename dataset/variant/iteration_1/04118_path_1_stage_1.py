import matplotlib.pyplot as plt
import numpy as np

# Define the years and months
years = np.arange(2013, 2023)
months = np.arange(1, 13)

# Randomly alter contents in some data groups while preserving the structure
monthly_temps = np.array([
    [0, 3, 5, 9, 14, 17, 22, 20, 17, 12, 6, 2],  # Changed March temperature
    [1, 3, 6, 10, 15, 19, 23, 21, 18, 13, 5, 3], # Changed November temperature
    [0, 1, 5, 9, 13, 18, 21, 20, 16, 10, 6, 1],  # Changed February and October temperatures
    [1, 5, 7, 11, 16, 19, 23, 21, 19, 14, 8, 4], # Changed February and July temperatures
    [2, 4, 7, 10, 16, 21, 23, 22, 19, 15, 8, 5], # Changed April temperature
    [1, 3, 6, 10, 14, 19, 22, 21, 16, 13, 9, 2], # Changed May and November temperatures
    [0, 2, 4, 8, 13, 17, 21, 20, 16, 11, 6, 1],  # Changed March and June temperatures
    [2, 4, 9, 12, 17, 21, 23, 24, 20, 15, 9, 5], # Changed July temperature
    [1, 3, 8, 11, 15, 20, 23, 21, 18, 12, 7, 4], # Changed March and April temperatures
    [0, 2, 6, 11, 15, 18, 22, 21, 17, 13, 6, 3]  # Changed June and November temperatures
])

# Average temperatures over the decade for each month
average_temps = np.mean(monthly_temps, axis=0)

# Set up the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot each year's data
for i, year in enumerate(years):
    ax.plot(months, monthly_temps[i], marker='o', linestyle='-', linewidth=2, markersize=6, label=f'{year}')

# Plot the average temperatures
ax.plot(months, average_temps, marker='D', linestyle='--', color='black', linewidth=2, markersize=8, label='Decadal Average', zorder=10)

# Add title and labels
ax.set_title('Seasonal Changes in Average Temperature Over a Decade', fontsize=18, fontweight='bold')
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Average Temperature (°C)', fontsize=14)

# Customize the x-axis to display month names
ax.set_xticks(months)
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Highlight specific insights
ax.annotate('Warmest Year', xy=(7, 24), xytext=(2, 25),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=12, color='darkred', bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightgrey', alpha=0.8))

ax.annotate('Coldest Year', xy=(1, 0), xytext=(5, -5),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=12, color='darkblue', bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightgrey', alpha=0.8))

# Set axis limits
ax.set_xlim(1, 12)
ax.set_ylim(-5, 30)

# Add a legend to the plot
ax.legend(loc='upper left', fontsize=12, ncol=2, title='Year', title_fontsize='13')

plt.tight_layout()

plt.show()