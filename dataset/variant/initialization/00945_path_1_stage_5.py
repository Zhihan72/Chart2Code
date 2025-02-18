import matplotlib.pyplot as plt
import numpy as np

categories = ['Biomass', 'Solar', 'Tidal', 'Hydro', 'Wind', 'Geothermal']
contributions = np.array([45, 130, 20, 65, 105, 30])

# New set of colors chosen for the chart
new_colors = ['#FF6347', '#4682B4', '#9ACD32', '#8A2BE2', '#FF69B4', '#40E0D0']
hatches = ['o', '/', '.', 'x', '\\', '*']

fig, ax = plt.subplots(figsize=(12, 7))

ax.bar(categories, contributions, color=new_colors, edgecolor='black', hatch=hatches, alpha=0.75)

ax.set_title("Renewable Energy Revenue in EcoCity\nSector Analysis", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Categories", fontsize=14)
ax.set_ylabel("Revenue (Million $)", fontsize=14)

ax.legend(['Biomass', 'Solar', 'Tidal', 'Hydro', 'Wind', 'Geothermal'], loc='upper left', fontsize=12)

ax.grid(axis='y', linestyle=':', alpha=0.5)

plt.xticks(rotation=45)

plt.tight_layout(rect=[0, 0, 0.98, 1])

plt.show()