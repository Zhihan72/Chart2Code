import matplotlib.pyplot as plt
import numpy as np

# Extended data for the analysis
categories = ['Solar', 'Wind', 'Hydro', 'Biomass', 'Geothermal', 'Tidal']
contributions = np.array([130, 105, 65, 45, 30, 20])  # Updated contributions including new categories
colors = ['#FFD700', '#3CB371', '#4682B4', '#8B4513', '#FF4500', '#1E90FF']
hatches = ['/', '\\', 'o', 'x', '*', '.']

fig, ax = plt.subplots(figsize=(12, 7))

ax.bar(categories, contributions, color=colors, edgecolor='black', hatch=hatches, alpha=0.75)

ax.set_title("Economic Contribution of Renewable Energy\nin GreenVille", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Sector", fontsize=14)
ax.set_ylabel("Economic Contribution (Million USD)", fontsize=14)

ax.legend(categories, loc='upper right', fontsize=12)

ax.grid(axis='y', linestyle=':', alpha=0.5)

plt.xticks(rotation=60)

plt.tight_layout(rect=[0, 0, 0.98, 1])

plt.show()