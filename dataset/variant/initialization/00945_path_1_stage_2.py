import matplotlib.pyplot as plt
import numpy as np

# Data for the analysis
categories = ['Solar', 'Wind', 'Hydro', 'Biomass']
contributions = np.array([130, 105, 65, 45])  # Final state of contributions for each category
colors = ['#FFD700', '#3CB371', '#4682B4', '#8B4513']
hatches = ['/', '\\', 'o', 'x']

fig, ax = plt.subplots(figsize=(12, 7))

# Plot the base bar chart
ax.bar(categories, contributions, color=colors, edgecolor='black', hatch=hatches, alpha=0.75)

ax.set_title("Economic Contribution of Renewable Energy\nin GreenVille", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Sector", fontsize=14)
ax.set_ylabel("Economic Contribution (Million USD)", fontsize=14)

ax.legend(categories, loc='upper right', fontsize=12)

# Altered grid style
ax.grid(axis='y', linestyle=':', alpha=0.5)

plt.xticks(rotation=60)

plt.tight_layout(rect=[0, 0, 0.98, 1])

# Display the plot
plt.show()