import matplotlib.pyplot as plt
import numpy as np

tree_species = ['Elm', 'Ash', 'Cedar', 'Fir', 'Sycamore', 'Aspen', 'Spruce', 'Pine', 'Birch', 'Oak']
sunlight_hours = np.array([4, 6, 5, 8, 2, 9, 3, 7, 3.5, 8.5])

# Sort the indices based on sunlight_hours
sorted_indices = np.argsort(sunlight_hours)
sorted_species = [tree_species[i] for i in sorted_indices]
sorted_sunlight_hours = sunlight_hours[sorted_indices]

plt.figure(figsize=(12, 8))
plt.bar(sorted_species, sorted_sunlight_hours, color='skyblue', edgecolor='navy')

plt.title('Sunlight Hours for Tree Species in Ascending Order', fontsize=18, fontweight='heavy', color='navy')
plt.xlabel('Tree Species', fontsize=14, fontweight='bold', color='darkred')
plt.ylabel('Sunlight Duration (Hrs/Day)', fontsize=14, fontweight='bold', color='darkgreen')

plt.xticks(rotation=45, ha='right', fontsize=10, color='dodgerblue', fontstyle='italic')

plt.grid(True, linestyle='-.', linewidth=0.75, color='lightgrey', axis='y')
plt.tight_layout()
plt.show()