import matplotlib.pyplot as plt
import numpy as np
from math import pi

categories = ['Solar', 'Wind', 'Hydro', 'Geo', 'Bio']
regions = ['NA', 'EU', 'AS', 'SA', 'AF', 'OC']

num_vars = len(categories)

data = {
    'NA': [20, 15, 30, 10, 25],
    'EU': [25, 20, 25, 15, 15],
    'AS': [15, 25, 35, 10, 15],
    'SA': [30, 10, 40, 10, 10],
    'AF': [20, 10, 25, 15, 30],
    'OC': [18, 22, 28, 13, 17],
}

angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Updated color palette
colors = ['#FF69B4', '#40E0D0', '#FFD700', '#7B68EE', '#FF6347', '#2E8B57']
for region, color in zip(data.keys(), colors):
    values = data[region]
    values += values[:1]
    ax.plot(angles, values, linewidth=2, linestyle='solid', color=color)
    ax.fill(angles, values, color=color, alpha=0.25)

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=11, color='gray')
ax.set_ylim(0, 40)

plt.title("Renewables by Region (2025)", fontsize=14, fontweight='bold', pad=15)
plt.tight_layout()
plt.show()