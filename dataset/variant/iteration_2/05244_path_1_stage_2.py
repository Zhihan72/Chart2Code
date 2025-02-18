import numpy as np
import matplotlib.pyplot as plt

years = np.arange(1920, 2021, 10)

northern_hemisphere = [-0.1, -0.2, -0.3, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4]
tropical_regions = [0.1, 0.0, 0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.9, 1.0, 1.1]
southern_hemisphere = [-0.2, -0.3, -0.2, 0.0, 0.1, 0.3, 0.5, 0.6, 0.7, 0.8, 0.9]

# Adding a new data series for polar regions
polar_regions = [-0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.2, 0.3, 0.5, 0.7, 0.9]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, northern_hemisphere, marker='o', linestyle='-', color='#FF4500', linewidth=2)
ax.plot(years, tropical_regions, marker='^', linestyle='--', color='#32CD32', linewidth=2)
ax.plot(years, southern_hemisphere, marker='s', linestyle='-.', color='#1E90FF', linewidth=2)

# Plotting the new data series
ax.plot(years, polar_regions, marker='d', linestyle=':', color='#8A2BE2', linewidth=2)

ax.set_title('Temperature Anomalies Over the Last Century\nAcross Different Regions', fontsize=18, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Temperature Anomaly (°C)', fontsize=14)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

plt.gca().set_facecolor('white')

plt.tight_layout()
plt.show()