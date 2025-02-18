import matplotlib.pyplot as plt
import numpy as np

beverages = ['Organic Tea', 'Herbal Infusion', 'Kombucha', 'Coconut Water', 'Aloe Vera Juice']
production_volumes = [55, 42, 63, 80, 37]

colors = ['#FF5733', '#33FFBD', '#3358FF', '#58FF33', '#F0FF33']
linestyles = ['-', '--', '-.', ':', '-']

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(beverages, production_volumes, color=colors, alpha=0.75, edgecolor='#555555', linestyle=linestyles[0])

for bar, volume in zip(bars, production_volumes):
    xval = bar.get_width()
    ax.text(xval + 1.5, bar.get_y() + bar.get_height() / 2, f'{volume}M', va='center', ha='left', fontsize=10, fontweight='normal')

ax.set_title("Eco-Friendly Beverage Production\nA Year in Review", fontsize=18, fontweight='normal', color='darkgreen')
ax.set_xlabel("Production Volume (Million Liters)", fontsize=13, color='black', fontstyle='italic')
ax.set_ylabel("Beverage Type", fontsize=13, color='black', fontstyle='italic')

most_produced_index = np.argmax(production_volumes)
ax.legend([bars[most_produced_index]], [beverages[most_produced_index]], title="Top Producer", loc='upper left', fontsize=11, frameon=True, facecolor='lightgray', edgecolor='gray')

ax.xaxis.grid(True, color='gray', linestyle=linestyles[3], linewidth=0.8, alpha=0.5)

plt.tight_layout()
plt.show()