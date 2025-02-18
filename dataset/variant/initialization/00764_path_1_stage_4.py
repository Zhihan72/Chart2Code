import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

biodiversity_data = np.array([
    [0.85, 0.75, 0.60, 0.70, 0.65],
    [0.78, 0.50, 0.55, 0.68, 0.60],
    [0.82, 0.55, 0.58, 0.75, 0.68],
    [0.80, 0.65, 0.62, 0.72, 0.66],
    [0.88, 0.78, 0.74, 0.76, 0.69],
    [0.90, 0.72, 0.67, 0.80, 0.77]
])

region_avg = biodiversity_data.mean(axis=1)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8), gridspec_kw={'width_ratios': [3, 1]})

cax = ax1.imshow(biodiversity_data, cmap='cividis', aspect='equal', interpolation='bicubic')  # Changed colormap
fig.colorbar(cax, ax=ax1, fraction=0.046, pad=0.04)

ax1.set_xticks(np.arange(biodiversity_data.shape[1]))
ax1.set_yticks(np.arange(biodiversity_data.shape[0]))

for i in range(biodiversity_data.shape[0]):
    for j in range(biodiversity_data.shape[1]):
        value = biodiversity_data[i, j]
        color = 'white' if value < 0.65 else 'black'
        ax1.text(j, i, f'{value:.2f}', ha='center', va='center', color=color)

ax2.barh(np.arange(biodiversity_data.shape[0]), region_avg, color='darkorange', edgecolor='navy', linestyle=':')  # Changed bar colors
ax2.set_xlim(0, 1)

highlight_index = np.argmax(biodiversity_data)
highlight_x, highlight_y = np.unravel_index(highlight_index, biodiversity_data.shape)
highlight_patch = mpatches.Rectangle((highlight_y-0.5, highlight_x-0.5), 1, 1, fill=False, edgecolor='red', linewidth=3, linestyle='-')  # Changed rectangle color
ax1.add_patch(highlight_patch)

ax1.grid(visible=True, linestyle='--', linewidth=0.5, color='gray')

plt.tight_layout()
plt.show()