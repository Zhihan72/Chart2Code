import numpy as np
import matplotlib.pyplot as plt

values = np.array([85, 78, 65, 90, 70, 60])
values = np.concatenate((values, [values[0]]))
angles = np.linspace(0, 2 * np.pi, len(values) - 1, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

ax.fill(angles, values, color='orange', alpha=0.4)
ax.plot(angles, values, color='orange', linewidth=2)

ax.set_yticklabels([])
ax.set_xticks(angles)
ax.set_xticklabels([])  # Remove group labels

ax.set_ylim(0, 100)
# Removed title and legend

plt.tight_layout()
plt.show()