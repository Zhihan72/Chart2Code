import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

temperature_anomalies = np.array([-0.2, -0.15, -0.1, 0.02, 0.1, 0.12, 0.18, 0.22, 0.3, 0.35, 
                         0.38, 0.4, 0.5, 0.55, 0.57, 0.62, 0.65, 0.68, 0.7, 0.75, 0.8])

colors_below = 'green'  
colors_above = 'orange'

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(years, temperature_anomalies, marker='o', linestyle='-', color='black', linewidth=2, markersize=8)

ax.fill_between(years, temperature_anomalies, where=(temperature_anomalies < 0), color=colors_below, alpha=0.3, interpolate=True)
ax.fill_between(years, temperature_anomalies, where=(temperature_anomalies >= 0), color=colors_above, alpha=0.3, interpolate=True)

ax.set_xticks(np.arange(2000, 2021, 2))
ax.set_yticks(np.arange(-0.2, 0.9, 0.1))
ax.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()