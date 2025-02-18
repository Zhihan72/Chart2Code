import numpy as np
import matplotlib.pyplot as plt

categories = ['Renewable Energy', 'Waste Management', 'Biodiversity',
              'Water Conservation', 'Air Quality', 'Green Transportation']
values = np.array([85, 78, 65, 90, 70, 60])
values = np.concatenate((values, [values[0]]))
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

ax.fill(angles, values, color='orange', alpha=0.4)
ax.plot(angles, values, color='orange', linewidth=2)

ax.set_yticklabels([])
ax.set_xticks(angles)
ax.set_xticklabels(categories + [categories[0]], fontsize=10, fontweight='bold', color='darkgreen')

plt.title("EcoVision: Sustainability Index 2040\nPerformance of EcoNation",
          size=16, color='darkblue', weight='bold', pad=20)

ax.set_ylim(0, 100)
ax.legend(['Performance Score'], loc='upper right', bbox_to_anchor=(1.1, 1.1), fontsize='medium', frameon=True)

plt.tight_layout()
plt.show()