import matplotlib.pyplot as plt
import numpy as np

attributes = ['Fire Power', 'Flying Speed', 'Stealth', 'Wisdom', 'Defense', 'Healing Power']
n_attributes = len(attributes)

fire_dragon = [5, 8, 9, 7, 4, 6]
wind_dragon = [7, 6, 4, 8, 10, 6]
earth_dragon = [10, 5, 8, 9, 7, 6]
water_dragon = [7, 5, 9, 7, 8, 6]

for dragon in [fire_dragon, wind_dragon, earth_dragon, water_dragon]:
    dragon += dragon[:1]

angles = np.linspace(0, 2 * np.pi, n_attributes, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

single_color = 'darkorange'
dragon_names = ['Fire Dragon', 'Wind Dragon', 'Earth Dragon', 'Water Dragon']
dragon_data = [fire_dragon, wind_dragon, earth_dragon, water_dragon]

for dragon in dragon_data:
    ax.plot(angles, dragon, color=single_color, linewidth=2, linestyle='solid')
    ax.fill(angles, dragon, color=single_color, alpha=0.25)

plt.xticks(angles[:-1], attributes, fontsize=12, fontweight='bold', color='darkblue')

ax.set_facecolor('whitesmoke')
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
ax.set_yticklabels([])

plt.legend(dragon_names, loc='upper right', bbox_to_anchor=(1.3, 1.1), title='Dragon Breeds', fontsize=10)

plt.title('Mythical Dragon Traits Analysis\nComparative Overview of Different Breeds', size=16, fontweight='bold', pad=30, color='black')

plt.tight_layout()
plt.show()