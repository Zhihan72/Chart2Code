import matplotlib.pyplot as plt
import squarify
import numpy as np

# Data for colonies
data = {
    'Mars': {'Pop': 5000, 'Green': 150, 'Water': 100, 'Energy': 300, 'Med': 50},
    'Luna': {'Pop': 3000, 'Green': 100, 'Water': 80, 'Energy': 200, 'Med': 40},
    'Titan': {'Pop': 2000, 'Green': 80, 'Water': 60, 'Energy': 150, 'Med': 30},
    'Europa': {'Pop': 1000, 'Green': 40, 'Water': 30, 'Energy': 100, 'Med': 20}
}

# Prepare data for treemap
labels = []
sizes = []
colors = ['#43A047', '#1E88E5', '#FDD835', '#E53935']

for planet, amenities in data.items():
    for amenity, count in amenities.items():
        label = f"{planet}\n{amenity}\n({count})"
        labels.append(label)
        sizes.append(count)

# Plotting the treemap
fig, ax = plt.subplots(figsize=(12, 7))
squarify.plot(sizes=sizes, label=labels, color=colors * len(data), alpha=0.8, edgecolor="white", linewidth=1.5, text_kwargs={'fontsize': 8, 'wrap': True})

plt.title("Colony Pop & Amenities", fontsize=14, fontweight='bold')
plt.axis('off')
plt.tight_layout()

plt.show()

# Stacked bar chart data
planets = list(data.keys())
amenities = list(data['Mars'].keys())
totals = np.array([[data[planet][amenity] for amenity in amenities] for planet in planets]).T

# Plot the stacked bar chart
fig, ax = plt.subplots(figsize=(10, 6))

bottom = np.zeros(len(planets))
colors = ['#43A047', '#1E88E5', '#FDD835', '#E53935', '#8E24AA']
for i, amenity in enumerate(amenities):
    ax.bar(planets, totals[i], bottom=bottom, label=amenity, color=colors[i % len(colors)], edgecolor='white')
    bottom += totals[i]

plt.title("Amenities by Type", fontsize=14, fontweight='bold')
plt.xlabel("Planets", fontsize=11)
plt.ylabel("Count", fontsize=11)
plt.legend(title="Amenities", fontsize=9)
plt.xticks(ticks=range(len(planets)), labels=planets)
plt.tight_layout()

plt.show()