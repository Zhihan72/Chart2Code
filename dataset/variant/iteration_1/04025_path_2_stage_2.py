import matplotlib.pyplot as plt
import squarify
import numpy as np

data = {
    'Mars': {'Population': 5200, 'Greenhouses': 140, 'Water Supply': 110, 'Energy Cells': 320, 'Medical Facilities': 45},
    'Luna': {'Population': 3100, 'Greenhouses': 105, 'Water Supply': 85, 'Energy Cells': 190, 'Medical Facilities': 38},
    'Titan': {'Population': 1950, 'Greenhouses': 85, 'Water Supply': 55, 'Energy Cells': 145, 'Medical Facilities': 25},
    'Europa': {'Population': 950, 'Greenhouses': 45, 'Water Supply': 35, 'Energy Cells': 95, 'Medical Facilities': 18}
}

labels = []
sizes = []
colors = ['#43A047', '#1E88E5', '#FDD835', '#E53935']

for planet, amenities in data.items():
    for amenity, count in amenities.items():
        label = f"{planet}\n{amenity} ({count})"
        labels.append(label)
        sizes.append(count)

fig, ax = plt.subplots(figsize=(12, 7))
squarify.plot(sizes=sizes, label=labels, color=colors * len(data), alpha=0.8, edgecolor="white", linewidth=1.5, text_kwargs={'fontsize': 8, 'wrap': True})

plt.title("Planetary Spots: Resident & Essentials Allocation", fontsize=15, fontweight='bold')
plt.axis('off')
plt.tight_layout()
plt.show()

# Stacked bar chart

planets = list(data.keys())
amenities = list(data['Mars'].keys())
totals = np.array([[data[planet][amenity] for amenity in amenities] for planet in planets]).T

fig, ax = plt.subplots(figsize=(10, 6))

bottom = np.zeros(len(planets))
colors = ['#43A047', '#1E88E5', '#FDD835', '#E53935', '#8E24AA']
for i, amenity in enumerate(amenities):
    ax.bar(planets, totals[i], bottom=bottom, label=amenity, color=colors[i % len(colors)], edgecolor='white')
    bottom += totals[i]

plt.title("Aggregate Essentials by Category Among Cosmic Colonies", fontsize=16, fontweight='bold')
plt.xlabel("Worlds", fontsize=12)
plt.ylabel("Numbers", fontsize=12)
plt.legend(title="Essentials", fontsize=10)
plt.xticks(ticks=range(len(planets)), labels=["Mar", "Lun", "Tit", "Eur"])
plt.tight_layout()
plt.show()