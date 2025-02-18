import matplotlib.pyplot as plt
import numpy as np

# Data for ocean temperature anomalies
years = np.arange(2000, 2021)
atlantic_anomalies = [0.12, 0.13, 0.14, 0.12, 0.15, 0.18, 0.17, 0.19, 0.20, 0.21, 0.23, 0.25, 0.28, 0.30, 0.32, 0.33, 0.35, 0.37, 0.38, 0.40, 0.42]
pacific_anomalies = [0.10, 0.11, 0.13, 0.10, 0.14, 0.16, 0.18, 0.15, 0.17, 0.18, 0.19, 0.20, 0.22, 0.24, 0.26, 0.27, 0.29, 0.30, 0.32, 0.34, 0.36]
indian_anomalies = [0.09, 0.10, 0.12, 0.11, 0.13, 0.15, 0.14, 0.16, 0.18, 0.20, 0.21, 0.22, 0.24, 0.25, 0.27, 0.28, 0.30, 0.31, 0.33, 0.34, 0.35]

fig, ax = plt.subplots(figsize=(14, 8))

# Plot the line charts with shuffled colors
ax.plot(years, atlantic_anomalies, color='green', marker='o', markersize=5, linewidth=2)
ax.plot(years, pacific_anomalies, color='red', marker='^', markersize=5, linewidth=2)
ax.plot(years, indian_anomalies, color='blue', marker='s', markersize=5, linewidth=2)

# Titles and labels
ax.set_title("Ocean Temperature Anomalies (2000 - 2020):\nTracking Climate Change", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel("Years", fontsize=14)
ax.set_ylabel("Temperature Anomaly (°C)", fontsize=14)

# Set axis limits
ax.set_xticks(years)
ax.set_xlim([1999, 2021])
ax.set_ylim([0.08, 0.45])

# Adding a secondary indicator subplot
ax_anomaly_change = ax.twinx()  # Create a second y axis
atlantic_rate_of_change = np.diff(atlantic_anomalies)
ax_anomaly_change.plot(years[1:], atlantic_rate_of_change, color='darkblue', linestyle='--', linewidth=1.5)

# Align secondary y-axis to primary
ax_anomaly_change.set_ylim([0.00, 0.05])
ax_anomaly_change.set_ylabel("Rate of Change (°C/year)", fontsize=14)

# Annotate the change plot
for i, rate in enumerate(atlantic_rate_of_change):
    ax_anomaly_change.annotate(f"{rate:.2f}", (years[i+1], rate), textcoords="offset points", xytext=(0,5), ha='center', fontsize=9, color='darkblue')

plt.tight_layout()
plt.show()