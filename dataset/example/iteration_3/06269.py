import matplotlib.pyplot as plt
import numpy as np

# Backstory: Monitoring Earth's Climate Change through Ocean Temperature Anomalies.
# The data represents ocean temperature anomalies in degrees Celsius across three different ocean basins (Atlantic, Pacific, Indian) from 2000 to 2020.

# Define years and temperature anomalies for each ocean basin
years = np.arange(2000, 2021)
atlantic_anomalies = [
    0.12, 0.13, 0.14, 0.12, 0.15, 0.18, 0.17, 0.19, 0.20, 0.21, 0.23, 0.25, 0.28, 0.30, 0.32, 0.33, 0.35, 0.37, 0.38, 0.40, 0.42
]
pacific_anomalies = [
    0.10, 0.11, 0.13, 0.10, 0.14, 0.16, 0.18, 0.15, 0.17, 0.18, 0.19, 0.20, 0.22, 0.24, 0.26, 0.27, 0.29, 0.30, 0.32, 0.34, 0.36
]
indian_anomalies = [
    0.09, 0.10, 0.12, 0.11, 0.13, 0.15, 0.14, 0.16, 0.18, 0.20, 0.21, 0.22, 0.24, 0.25, 0.27, 0.28, 0.30, 0.31, 0.33, 0.34, 0.35
]

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the line charts for each ocean basin
ax.plot(years, atlantic_anomalies, color='blue', marker='o', markersize=5, linewidth=2, label='Atlantic Ocean')
ax.plot(years, pacific_anomalies, color='green', marker='^', markersize=5, linewidth=2, label='Pacific Ocean')
ax.plot(years, indian_anomalies, color='red', marker='s', markersize=5, linewidth=2, label='Indian Ocean')

# Titles and labels
ax.set_title("Ocean Temperature Anomalies (2000 - 2020):\nTracking Climate Change", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel("Years", fontsize=14)
ax.set_ylabel("Temperature Anomaly (°C)", fontsize=14)
ax.legend(fontsize=12, title="Oceans", title_fontsize='13')

# Customizing the grid
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Customize the x and y axis
ax.set_xticks(years)
ax.set_xlim([1999, 2021])
ax.set_ylim([0.08, 0.45])

# Adding a secondary indicator subplot
ax_anomaly_change = ax.twinx()  # Create a second y axis sharing the same x axis
# Calculate and plot the rate of change in temperature anomalies for the Atlantic
atlantic_rate_of_change = np.diff(atlantic_anomalies)
ax_anomaly_change.plot(years[1:], atlantic_rate_of_change, color='darkblue', linestyle='--', linewidth=1.5, label='Rate of Change (Atlantic)')

# Align secondary y-axis to primary
ax_anomaly_change.set_ylim([0.00, 0.05])
ax_anomaly_change.set_ylabel("Rate of Change (°C/year)", fontsize=14)

# Annotate the change plot
for i, rate in enumerate(atlantic_rate_of_change):
    ax_anomaly_change.annotate(f"{rate:.2f}", (years[i+1], rate), textcoords="offset points", xytext=(0,5), ha='center', fontsize=9, color='darkblue')

# Adding a legend for the secondary axis chart
ax_anomaly_change.legend(loc='upper center', fontsize=12)

# Apply a tight layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()