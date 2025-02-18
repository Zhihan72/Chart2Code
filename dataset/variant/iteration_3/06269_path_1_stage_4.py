import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)
atlantic_anomalies = [0.12, 0.13, 0.14, 0.12, 0.15, 0.18, 0.17, 0.19, 0.20, 0.21, 0.23, 0.25, 0.28, 0.30, 0.32, 0.33, 0.35, 0.37, 0.38, 0.40, 0.42]

fig, ax = plt.subplots(figsize=(14, 8))
ax.plot(years, atlantic_anomalies, color='green', marker='o', markersize=5, linewidth=2)

ax.set_xticks(years)
ax.set_xlim([1999, 2021])
ax.set_ylim([0.08, 0.45])

ax_anomaly_change = ax.twinx()
atlantic_rate_of_change = np.diff(atlantic_anomalies)
ax_anomaly_change.plot(years[1:], atlantic_rate_of_change, color='darkblue', linestyle='--', linewidth=1.5)
ax_anomaly_change.set_ylim([0.00, 0.05])

plt.tight_layout()
plt.show()