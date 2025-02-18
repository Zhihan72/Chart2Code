import matplotlib.pyplot as plt
import numpy as np

countries = ['USA', 'China', 'Ger', 'Bra', 'India', 'UK', 'Fra', 'Aus', 'Canada', 'Jap']
# Alter the urban_parks and urbanization_level slightly while preserving structure
urban_parks = np.array([1300, 2900, 850, 750, 500, 1050, 980, 820, 740, 1250])
urbanization_level = np.array([83, 68, 75, 85, 32, 82, 79, 88, 80, 89])

average_park_area = urban_parks / 10 + [30, 29, 20, 35, 38, 25, 28, 27, 31, 18]

fig, ax = plt.subplots(figsize=(14, 8))
scatter = ax.scatter(urbanization_level, urban_parks, s=average_park_area, color='blue', alpha=0.6, edgecolor='black')

ax.set_title('Parks vs. Urbanization (%)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Urbanization (%)', fontsize=14)
ax.set_ylabel('Parks Count', fontsize=14)

for i, country in enumerate(countries):
    ax.annotate(country, (urbanization_level[i], urban_parks[i]), fontsize=10, ha='right', va='bottom', color='black')

ax.grid(True, linestyle='--', alpha=0.7)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
ax.set_xlim(30, 95)
ax.set_ylim(400, 3200)

plt.tight_layout()
plt.show()