import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)
atlantic_anomalies = [
    0.32, 0.12, 0.28, 0.13, 0.23, 0.33, 0.18, 0.25, 0.17, 0.20, 0.19, 0.15, 0.30, 0.35, 0.12, 0.38, 0.14, 0.40, 0.42, 0.21, 0.37
]
pacific_anomalies = [
    0.17, 0.18, 0.36, 0.10, 0.14, 0.19, 0.34, 0.26, 0.30, 0.22, 0.20, 0.24, 0.27, 0.29, 0.13, 0.11, 0.15, 0.32, 0.10, 0.16, 0.18
]
indian_anomalies = [
    0.16, 0.12, 0.27, 0.35, 0.14, 0.20, 0.09, 0.24, 0.18, 0.22, 0.31, 0.11, 0.28, 0.33, 0.13, 0.30, 0.25, 0.10, 0.34, 0.15, 0.21
]

fig, ax = plt.subplots(figsize=(14, 8))

# Use a single color for all plots
common_color = 'blue'

ax.plot(years, atlantic_anomalies, color=common_color, marker='o', markersize=5, linewidth=2, label='Atlantic')
ax.plot(years, pacific_anomalies, color=common_color, marker='^', markersize=5, linewidth=2, label='Pacific')
ax.plot(years, indian_anomalies, color=common_color, marker='s', markersize=5, linewidth=2, label='Indian')

ax.set_title("Ocean Temp Anomalies (2000-2020)", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Temp Anomaly (°C)", fontsize=14)
ax.legend(fontsize=12, title="Oceans", title_fontsize='13')

ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

ax.set_xticks(years)
ax.set_xlim([1999, 2021])
ax.set_ylim([0.08, 0.45])

ax_anomaly_change = ax.twinx()
atlantic_rate_of_change = np.diff(atlantic_anomalies)
# Use the same common color for rate of change
ax_anomaly_change.plot(years[1:], atlantic_rate_of_change, color=common_color, linestyle='--', linewidth=1.5, label='Change Rate (Atl)')

ax_anomaly_change.set_ylim([0.00, 0.05])
ax_anomaly_change.set_ylabel("Rate of Change (°C/yr)", fontsize=14)

for i, rate in enumerate(atlantic_rate_of_change):
    ax_anomaly_change.annotate(f"{rate:.2f}", (years[i+1], rate), textcoords="offset points", xytext=(0,5), ha='center', fontsize=9, color=common_color)

ax_anomaly_change.legend(loc='upper center', fontsize=12)

plt.tight_layout()
plt.show()