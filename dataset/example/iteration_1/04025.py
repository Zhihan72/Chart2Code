import matplotlib.pyplot as plt
import squarify

# Backstory: In the near future, space exploration has advanced, leading to the establishment of space colonies across several planets in our solar system. 
# This chart represents the distribution of colonial population and key amenities across different planets.

# Data: Population and key amenities across the new colonies
data = {
    'Mars': {'Population': 5000, 'Greenhouses': 150, 'Water Supply': 100, 'Energy Cells': 300, 'Medical Facilities': 50},
    'Luna': {'Population': 3000, 'Greenhouses': 100, 'Water Supply': 80, 'Energy Cells': 200, 'Medical Facilities': 40},
    'Titan': {'Population': 2000, 'Greenhouses': 80, 'Water Supply': 60, 'Energy Cells': 150, 'Medical Facilities': 30},
    'Europa': {'Population': 1000, 'Greenhouses': 40, 'Water Supply': 30, 'Energy Cells': 100, 'Medical Facilities': 20}
}

# Flatten data for squarify
labels = []
sizes = []
colors = ['#43A047', '#1E88E5', '#FDD835', '#E53935']

# Build data structure for plotting the treemap
for planet, amenities in data.items():
    for amenity, count in amenities.items():
        label = f"{planet}\n{amenity}\n({count})"
        labels.append(label)
        sizes.append(count)

# Plotting the tree map
fig, ax = plt.subplots(figsize=(12, 7))
squarify.plot(sizes=sizes, label=labels, color=colors * len(data), alpha=0.8, edgecolor="white", linewidth=1.5, text_kwargs={'fontsize': 8, 'wrap': True})

# Titles and aesthetics
plt.title("Space Colonies: Population and Key Amenities Distribution", fontsize=15, fontweight='bold')
plt.axis('off')

# Adjust layout to prevent text overlap
plt.tight_layout()

# Display plot
plt.show()

# Secondary visualization: Stacked bar chart to show the total amenities by type across all colonies
import numpy as np

# Organize data for stacked bar chart
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

# Configure the plot
plt.title("Total Amenities by Type Across Space Colonies", fontsize=16, fontweight='bold')
plt.xlabel("Planets", fontsize=12)
plt.ylabel("Counts", fontsize=12)
plt.legend(title="Amenities", fontsize=10)
plt.xticks(ticks=range(len(planets)), labels=planets)

# Adjust layout to prevent text overlap
plt.tight_layout()

# Display plot
plt.show()