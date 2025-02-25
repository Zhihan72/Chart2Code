import matplotlib.pyplot as plt
import numpy as np

regions = ['Solaris', 'Lunaria', 'Astoria', 'Nebula', 'Quasaris']
elements = ['Plasma', 'Ether', 'Luminal', 'Void', 'Astral']
distributions = [
    [30, 20, 10, 25, 15],
    [10, 25, 20, 30, 15],
    [20, 30, 15, 10, 25],
    [25, 10, 30, 15, 20],
    [15, 25, 20, 15, 25],
]

fig, ax = plt.subplots(figsize=(10, 10), nrows=2, ncols=3)
ax = ax.flatten()

for idx, region in enumerate(regions):
    wedges, texts, autotexts = ax[idx].pie(
        distributions[idx],
        labels=elements,
        autopct='%1.1f%%',
        startangle=90,
        colors=[plt.cm.viridis(i / len(elements)) for i in range(len(elements))],
        wedgeprops=dict(width=0.3)
    )
    ax[idx].set_title(region)

for a in ax[len(regions):]:
    a.remove()

fig.suptitle("Element Distribution by Region", fontsize=16, weight='bold')

plt.tight_layout(pad=3.0)
plt.show()