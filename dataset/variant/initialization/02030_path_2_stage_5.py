import matplotlib.pyplot as plt
import numpy as np

# Updated datasets with shorter names
beverages = ['Org Tea', 'Herbal Inf', 'Kombucha', 'Coco Water', 'Aloe Juice', 'Ginger Ale', 'Matcha L', 'Chia Fresca']
production_volumes = [55, 42, 63, 80, 37, 45, 50, 40]

colors = ['#FF5733', '#33FFBD', '#3358FF', '#58FF33', '#F0FF33', '#FFD700', '#ADFF2F', '#FFB6C1']
linestyles = ['-', '--', '-.', ':', '-', '--', '-.', ':']

fig, ax = plt.subplots(figsize=(10, 8))
bars = ax.barh(beverages, production_volumes, color=colors[:len(beverages)], alpha=0.75, edgecolor='#555555', linestyle=linestyles[0])

for bar, volume in zip(bars, production_volumes):
    xval = bar.get_width()
    ax.text(xval + 1.5, bar.get_y() + bar.get_height() / 2, f'{volume}M', va='center', ha='left', fontsize=10)

ax.set_title("Eco Beverages: Year Review", fontsize=18, color='darkgreen')
ax.set_xlabel("Volume (M Liters)", fontsize=13, color='black', fontstyle='italic')
ax.set_ylabel("Beverage", fontsize=13, color='black', fontstyle='italic')

most_produced_index = np.argmax(production_volumes)
ax.legend([bars[most_produced_index]], [beverages[most_produced_index]], title="Top Producer", loc='upper left', fontsize=11, frameon=True, facecolor='lightgray', edgecolor='gray')

ax.xaxis.grid(True, color='gray', linestyle=linestyles[3], linewidth=0.8, alpha=0.5)

plt.tight_layout()
plt.show()