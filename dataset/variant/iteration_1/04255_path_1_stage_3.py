import matplotlib.pyplot as plt
import numpy as np

attributes = ['Stealth', 'Healing Power', 'Defense', 'Flying Speed', 'Fire Power', 'Wisdom']
n_attributes = len(attributes)

fire_dragon = [5, 5, 6, 8, 9, 7]
wind_dragon = [7, 9, 4, 10, 6, 6]

for dragon in [fire_dragon, wind_dragon]:
    dragon += dragon[:1]

angles = np.linspace(0, 2 * np.pi, n_attributes, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

colors = ['red', 'blue']
line_styles = ['dashed', 'dashdot']
marker_types = ['o', '*']
dragon_names = ['Fire Dragon', 'Wind Dragon']
dragon_data = [fire_dragon, wind_dragon]

for idx, dragon in enumerate(dragon_data):
    ax.plot(angles, dragon, color=colors[idx], linestyle=line_styles[idx], 
            marker=marker_types[idx], linewidth=2, label=dragon_names[idx])
    ax.fill(angles, dragon, color=colors[idx], alpha=0.25)

plt.xticks(angles[:-1], attributes, fontsize=12, fontweight='bold', color='teal')

ax.set_facecolor('lightyellow')
ax.grid(color='darkgray', linestyle=':', linewidth=1, alpha=0.8)
ax.spines['polar'].set_visible(True)

plt.legend(loc='lower left', bbox_to_anchor=(-0.1, -0.1), title='Dragon Types', fontsize=9)

plt.title('Comparative Dragon Traits Overview', size=16, fontweight='bold', pad=20, color='darkred')

plt.tight_layout()

plt.show()