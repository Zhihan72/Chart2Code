import matplotlib.pyplot as plt
import numpy as np

wizardry_schools = ['Arcane Academy', 'Mystic Institute', 'Elemental Guild', 'Enchantment Realm']

arcane_spells = [25, 5, 20, 10, 30, 10]
mystic_spells = [15, 30, 10, 25, 0, 20]
elemental_spells = [35, 5, 20, 25, 15, 0]
enchantment_spells = [10, 10, 15, 15, 25, 25]

average_power_levels = [8, 6, 7, 9]

# Shuffled colors
colors = ['#66b3ff', '#99ff99', '#ffcc99', '#ff9999', '#c2c2f0', '#ffb3e6']

fig, (ax2, ax1) = plt.subplots(1, 2, figsize=(18, 9))

ax2.barh(wizardry_schools, average_power_levels, color='#8dd3c7', edgecolor='#000000', hatch='/')
ax2.set_xlim(0, 10)
ax2.grid(True, linestyle='--', linewidth=0.5, color='gray')
ax2.legend(['Average Power'], loc='lower right', frameon=True, fontsize='medium')

data = [arcane_spells, mystic_spells, elemental_spells, enchantment_spells]
marker_styles = ['x', '^', 'o', 's']

for i, school_data in enumerate(data):
    ax1.clear()
    wedges, texts = ax1.pie(
        school_data,
        colors=colors,
        startangle=90,
        wedgeprops=dict(width=0.3, edgecolor='k', linestyle='-', linewidth=1)
    )
    ax1.scatter(0, 0, s=100, c='black', marker=marker_styles[i])
    
    center_circle = plt.Circle((0, 0), 0.7, fc='white')
    ax1.add_artist(center_circle)
    ax1.legend(wizardry_schools, loc='best', frameon=True)

    plt.pause(1)

plt.tight_layout()
plt.show()