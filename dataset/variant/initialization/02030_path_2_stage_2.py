import matplotlib.pyplot as plt
import numpy as np

beverages = ['Organic Tea', 'Herbal Infusion', 'Kombucha', 'Coconut Water', 'Aloe Vera Juice']
production_volumes = [55, 42, 63, 80, 37]

# Use a single consistent color for all bars
single_color = '#8FD14F'

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(beverages, production_volumes, color=single_color, alpha=0.85, edgecolor='black')

for bar, volume in zip(bars, production_volumes):
    xval = bar.get_width()
    ax.text(xval + 1, bar.get_y() + bar.get_height() / 2, f'{volume}M', va='center', ha='left', fontsize=11, fontweight='bold')

ax.set_title("Eco-Friendly Beverage Production\nA Year in Review", fontsize=16, fontweight='bold')
ax.set_xlabel("Production Volume (Million Liters)", fontsize=14)
ax.set_ylabel("Beverage Type", fontsize=14)

most_produced_index = np.argmax(production_volumes)
ax.legend([bars[most_produced_index]], [beverages[most_produced_index]], title="Top Producer", loc='lower right', fontsize=10, frameon=False)

ax.xaxis.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()