import matplotlib.pyplot as plt
import numpy as np

attributes = ['Stealth', 'Healing Power', 'Defense', 'Flying Speed', 'Fire Power', 'Wisdom']
n_attributes = len(attributes)

fire_dragon = [5, 5, 6, 8, 9, 7]
wind_dragon = [7, 9, 4, 10, 6, 6]
earth_dragon = [9, 10, 9, 5, 7, 8]
water_dragon = [9, 8, 6, 7, 5, 7]

for dragon in [fire_dragon, wind_dragon, earth_dragon, water_dragon]:
    dragon += dragon[:1]

angles = np.linspace(0, 2 * np.pi, n_attributes, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

colors = ['purple', 'green', 'red', 'blue']
dragon_names = ['Water Dragon', 'Fire Dragon', 'Earth Dragon', 'Wind Dragon']
dragon_data = [water_dragon, fire_dragon, earth_dragon, wind_dragon]

for idx, dragon in enumerate(dragon_data):
    ax.plot(angles, dragon, color=colors[idx], linewidth=2, linestyle='solid', label=dragon_names[idx])
    ax.fill(angles, dragon, color=colors[idx], alpha=0.25)

plt.xticks(angles[:-1], attributes, fontsize=12, fontweight='bold', color='darkblue')

ax.set_facecolor('whitesmoke')
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
ax.set_yticklabels([])

plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), title='Dragon Types', fontsize=10)

plt.title('Comparative Overview of Dragon Breeds\nLegendary Traits Visualization', size=16, fontweight='bold', pad=30, color='black')

plt.tight_layout()

plt.show()