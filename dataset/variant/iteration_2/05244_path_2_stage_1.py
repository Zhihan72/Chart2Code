import numpy as np
import matplotlib.pyplot as plt

years = np.arange(1920, 2021, 10)

# Manually rearranged temperature anomalies data
northern_hemisphere = [0.6, 1.4, 0.8, -0.1, 0.4, 0.0, 1.2, -0.3, 1.0, 0.2, 0.8]
tropical_regions = [0.5, 0.1, 0.9, 0.0, 0.3, 1.0, 0.7, 0.2, 1.1, 0.1, 0.8]
southern_hemisphere = [-0.2, 0.0, 0.7, 0.1, 0.5, 0.3, -0.3, 0.9, 0.6, -0.2, 0.8]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, northern_hemisphere, marker='o', linestyle='-', color='#FF4500', linewidth=2, label='Northern Hemisphere')
ax.plot(years, tropical_regions, marker='^', linestyle='--', color='#32CD32', linewidth=2, label='Tropical Regions')
ax.plot(years, southern_hemisphere, marker='s', linestyle='-.', color='#1E90FF', linewidth=2, label='Southern Hemisphere')

ax.set_title('Temperature Anomalies Over the Last Century\nAcross Different Regions', fontsize=18, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Temperature Anomaly (°C)', fontsize=14)

ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.5)
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
ax.legend(loc='upper left', title='Regions', fontsize=12)
ax.axhline(0, color='gray', linewidth=1.5, linestyle='--', alpha=0.6)

ax.annotate('Sharp increase in NH temperatures',
             xy=(1980, 0.4), xytext=(1960, 0.8),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')
ax.annotate('Consistent rise in Tropical temperatures',
             xy=(1990, 0.7), xytext=(1970, 1.1),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='black')

plt.gca().set_facecolor('#f7f7f7')
plt.tight_layout()
plt.show()