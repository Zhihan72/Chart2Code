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

ax.plot(years, atlantic_anomalies, color='green', marker='v', markersize=7, linewidth=2.5, linestyle='-.', label='Atlantic')
ax.plot(years, pacific_anomalies, color='red', marker='D', markersize=6, linewidth=1.5, linestyle='--', label='Pacific')
ax.plot(years, indian_anomalies, color='purple', marker='*', markersize=8, linewidth=2, linestyle='-', label='Indian')

ax.set_title("Ocean Temp Anomalies (2000-2020)", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Temp Anomaly (°C)", fontsize=14)
ax.legend(fontsize=12, title="Oceans", title_fontsize='13', loc='lower left')

ax.grid(False)  # Remove grid

ax.set_xticks(years)
ax.set_xlim([1999, 2021])
ax.set_ylim([0.08, 0.45])

ax_anomaly_change = ax.twinx()
atlantic_rate_of_change = np.diff(atlantic_anomalies)
ax_anomaly_change.plot(years[1:], atlantic_rate_of_change, color='brown', linestyle=':', linewidth=1.2, label='Change Rate (Atl)')

ax_anomaly_change.set_ylim([0.00, 0.05])
ax_anomaly_change.set_ylabel("Rate of Change (°C/yr)", fontsize=14)

# Removed annotations for cleaner look
ax_anomaly_change.legend(loc='upper center', fontsize=12)

plt.tight_layout()
plt.show()