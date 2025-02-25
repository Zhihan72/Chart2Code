import matplotlib.pyplot as plt
import numpy as np

regions = ['Nebula', 'Solaris', 'Astoria', 'Quasaris', 'Lunaria']
elements = ['Astral', 'Void', 'Ether', 'Luminal', 'Plasma']
distributions = [
    [20, 15, 30, 25, 10],
    [10, 30, 25, 15, 20],
    [25, 20, 10, 15, 30],
    [15, 25, 25, 20, 15],
    [30, 10, 15, 20, 25],
]

fig, ax = plt.subplots(figsize=(10, 10), nrows=2, ncols=3)
ax = ax.flatten()

for idx, region in enumerate(regions):
    wedges, texts, autotexts = ax[idx].pie(
        distributions[idx],
        labels=elements,
        autopct='%1.2f%%',
        startangle=45,
        colors=[plt.cm.plasma(i / len(elements)) for i in range(len(elements))],
        wedgeprops=dict(width=0.4, edgecolor='w', linestyle='dashed')
    )
    for text in autotexts:
        text.set_fontsize(8)
        text.set_weight('bold')
    ax[idx].set_title(region, fontsize=10, color='darkred')

for a in ax[len(regions):]:
    a.remove()

fig.suptitle("Element Distribution by Region", fontsize=18, fontweight='bold', color='navy', style='italic')

ax[1].grid(True, which='both', linestyle='--', linewidth=0.7, color='gray')
ax[2].grid(True, which='both', linestyle='--', linewidth=0.7, color='gray')

plt.tight_layout(pad=3.0, h_pad=2.5, w_pad=2.5)
plt.show()