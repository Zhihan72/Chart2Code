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
        autopct='%1.2f%%',  # Altered from '%1.1f%%' for more precision
        startangle=45,  # Changed from 90 to create variation
        colors=[plt.cm.plasma(i / len(elements)) for i in range(len(elements))],  # Changed colormap to 'plasma'
        wedgeprops=dict(width=0.4, edgecolor='w', linestyle='dashed')  # Changed wedge width, edgecolor, and linestyle
    )
    for text in autotexts:  # Adjusting font size and weight for clarity
        text.set_fontsize(8)
        text.set_weight("bold")
    ax[idx].set_title(region, fontsize=10, color='darkred')  # Changed title font size and color

# Remove the last unnecessary subplot
for a in ax[len(regions):]:
    a.remove()

# Altered suptitle properties
fig.suptitle("Element Distribution by Region", fontsize=18, fontweight='bold', color='navy', style='italic')

# Adding grid randomly to some subplots
ax[1].grid(True, which='both', linestyle='--', linewidth=0.7, color='gray')
ax[2].grid(True, which='both', linestyle='--', linewidth=0.7, color='gray')

plt.tight_layout(pad=3.0, h_pad=2.5, w_pad=2.5)  # Altered padding for variation
plt.show()