import matplotlib.pyplot as plt
import numpy as np

countries = ['USA', 'China', 'Ger', 'Bra', 'India', 'UK', 'Fra', 'Aus', 'Canada', 'Jap']
urban_parks = np.array([1200, 3000, 900, 700, 450, 1100, 950, 800, 770, 1300])
urbanization_level = np.array([81, 64, 77, 86, 34, 84, 81, 90, 81, 91])

average_park_area = urban_parks / 10 + [25, 38, 15, 29, 40, 18, 30, 26, 33, 20]

fig, ax = plt.subplots(figsize=(14, 8))
scatter = ax.scatter(urbanization_level, urban_parks, s=average_park_area, c=average_park_area, cmap='coolwarm', alpha=0.6, edgecolor='black')

ax.set_title('Parks vs. Urbanization (%)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Urbanization (%)', fontsize=14)
ax.set_ylabel('Parks Count', fontsize=14)

cbar = fig.colorbar(scatter, ax=ax)
cbar.set_label('Park Area (ha)', fontsize=12, fontweight='bold')

for i, country in enumerate(countries):
    ax.annotate(country, (urbanization_level[i], urban_parks[i]), fontsize=10, ha='right', va='bottom', color='black')

ax.grid(True, linestyle='--', alpha=0.7)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
ax.set_xlim(30, 95)
ax.set_ylim(400, 3200)

plt.tight_layout()
plt.show()