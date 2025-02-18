import matplotlib.pyplot as plt
import numpy as np

# Dragon attributes
attributes = ['Wisdom', 'Healing Force', 'Stealth', 'Fire Power', 'Defense', 'Sky Speed']
n_attributes = len(attributes)

# Dragon attribute values
fire_dragon = [8, 5, 7, 9, 6, 4]
wind_dragon = [6, 7, 8, 4, 6, 10]
earth_dragon = [5, 10, 9, 8, 6, 7]
water_dragon = [8, 7, 7, 9, 6, 5]

# Ensure the plot closes at the same point
for dragon in [fire_dragon, wind_dragon, earth_dragon, water_dragon]:
    dragon += dragon[:1]

# Angles for radar plot
angles = np.linspace(0, 2 * np.pi, n_attributes, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))

dragon_data = [fire_dragon, wind_dragon, earth_dragon, water_dragon]
dragon_names = ['Flame Wyvern', 'Sky Beast', 'Earth Guardian', 'Aqua Serpent']

colors = ['crimson', 'teal', 'purple', 'forestgreen']

# Plot each dragon with filled areas
for i, dragon in enumerate(dragon_data):
    ax.fill(angles, dragon, color=colors[i], alpha=0.25, label=dragon_names[i])

plt.xticks(angles[:-1], attributes, fontsize=12, fontweight='bold', color='darkred')

ax.set_facecolor('lightyellow')
ax.grid(color='black', linestyle=':', linewidth=0.6, alpha=0.7)
ax.spines['polar'].set_visible(False)

plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 1.1), title='Mystic Dragons', fontsize=10)

plt.title('Attributes of Legendary Dragons\nAn Intricate Comparison', size=18, fontweight='bold', pad=30, color='darkgreen')

plt.tight_layout()
plt.show()