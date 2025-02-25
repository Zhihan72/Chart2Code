import matplotlib.pyplot as plt
import numpy as np
from math import pi

categories = ['Solar Power', 'Wind Power', 'Hydropower', 'Geothermal', 'Biomass']
regions = ['North America', 'Europe', 'Asia', 'South America']

data = {
    'North America': [20, 15, 30, 10, 25],
    'Europe': [25, 20, 25, 15, 15],
    'Asia': [15, 25, 35, 10, 15],
    'South America': [30, 10, 40, 10, 10],
}

angles = np.linspace(0, 2 * pi, len(categories), endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

colors = ['#4682B4', '#8A2BE2', '#3CB371', '#FFD700']
for region, color in zip(data.keys(), colors):
    values = data[region]
    values += values[:1]
    ax.plot(angles, values, linewidth=2, linestyle='solid', label=region, color=color)
    ax.fill(angles, values, color=color, alpha=0.25)

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, color='gray')

ax.set_ylim(0, 40)

plt.title("Global Renewable Energy Distribution by Region in 2025", fontsize=16, fontweight='bold', pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))

plt.tight_layout()
plt.show()