import matplotlib.pyplot as plt
import numpy as np

data = {
    'Mars': {'Population': 5200, 'Greenhouses': 140, 'Water Supply': 110, 'Energy Cells': 320, 'Medical Facilities': 45},
    'Luna': {'Population': 3100, 'Greenhouses': 105, 'Water Supply': 85, 'Energy Cells': 190, 'Medical Facilities': 38},
    'Titan': {'Population': 1950, 'Greenhouses': 85, 'Water Supply': 55, 'Energy Cells': 145, 'Medical Facilities': 25},
    'Europa': {'Population': 950, 'Greenhouses': 45, 'Water Supply': 35, 'Energy Cells': 95, 'Medical Facilities': 18}
}

planets = list(data.keys())
amenities = list(data['Mars'].keys())
totals = np.array([[data[planet][amenity] for amenity in amenities] for planet in planets])

fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.15
index = np.arange(len(planets))
colors = ['#43A047', '#1E88E5', '#FDD835', '#E53935', '#8E24AA']

for i, amenity in enumerate(amenities):
    ax.bar(index + i * bar_width, totals[:, i], bar_width, label=amenity, color=colors[i % len(colors)])

ax.set_xlabel("Worlds", fontsize=12)
ax.set_ylabel("Numbers", fontsize=12)
ax.set_xticks(index + bar_width * len(amenities) / 2 - bar_width / 2)
ax.set_xticklabels(["Mar", "Lun", "Tit", "Eur"])
ax.legend(title="Amenities")

plt.tight_layout()
plt.show()