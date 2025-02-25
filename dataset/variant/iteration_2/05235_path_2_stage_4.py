import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

north_region = np.array([1, 2, 4, 8, 15, 25, 38, 50, 70, 85, 100])
south_region = np.array([0, 1, 2, 5, 10, 18, 28, 37, 50, 60, 75])
east_region = np.array([0, 0, 1, 4, 7, 12, 20, 28, 39, 49, 60])
west_region = np.array([0, 0, 0, 1, 4, 8, 14, 22, 32, 44, 55])
central_zone = np.array([0, 0, 2, 6, 12, 20, 33, 45, 60, 75, 90])
highland_district = np.array([0, 1, 3, 5, 9, 15, 23, 35, 40, 50, 58])

fig, ax = plt.subplots(figsize=(14, 8))

# Applying a single color consistently across all data groups
single_color = '#4682B4'  # Steel blue color chosen for consistency across all regions

ax.stackplot(years, north_region, south_region, east_region, west_region, central_zone, highland_district,
             labels=['Northern Areas', 'Southern Parts', 'Eastern Block', 'Western Lands', 'Central Zone', 'Highland District'],
             colors=[single_color] * 6, alpha=0.8, 
             edgecolor='black', linewidth=0.5, hatch=['/', '\\', '|', '-', 'x', 'o'])

ax.set_title("EV Expansion in Green Nation (2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Time Period", fontsize=12)
ax.set_ylabel("Electric Vehicles (x1000)", fontsize=12)
ax.set_xlim(years.min(), years.max())
ax.set_ylim(0, 250)

ax.grid(True, linestyle=':', color='gray', alpha=0.7)

ax.legend(title="Zones", loc="upper right", fontsize=11, frameon=True, shadow=True, facecolor='lightgray')

ax.annotate('Eco Initiative Kickoff', xy=(2015, 12), xytext=(2013, 70),
            arrowprops=dict(arrowstyle='->', connectionstyle='angle3', color='red'), fontsize=10)
ax.annotate('Rapid Growth Period', xy=(2018, 160), xytext=(2017, 200),
            arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3', color='blue'), fontsize=10)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()