import matplotlib.pyplot as plt
import numpy as np

wizardry_schools = ['Elemental Guild', 'Enchantment Realm', 'Mystic Institute', 'Arcane Academy']
spell_types = ['Earth Spells', 'Healing Spells', 'Fire Spells', 'Air Spells', 'Lightning Spells', 'Water Spells']

arcane_spells = [25, 5, 20, 10, 30, 10]
mystic_spells = [15, 30, 10, 25, 0, 20]
elemental_spells = [35, 5, 20, 25, 15, 0]
enchantment_spells = [10, 10, 15, 15, 25, 25]

average_power_levels = [8, 6, 7, 9]

single_color = '#66b3ff'

fig, axs = plt.subplots(2, 2, figsize=(18, 9))

data = [arcane_spells, mystic_spells, elemental_spells, enchantment_spells]

for i, ax in enumerate(axs.flatten()[:len(data)]):
    ax.pie(
        data[i],
        autopct='%1.1f%%',
        pctdistance=0.85,
        colors=[single_color] * len(data[i]),
        startangle=90,
        wedgeprops=dict(width=0.4, edgecolor='w')
    )
    center_circle = plt.Circle((0, 0), 0.55, fc='white')
    ax.add_artist(center_circle)
    ax.set_title(wizardry_schools[i], fontsize=16, fontweight='bold', loc='center')

fig.suptitle("Casting & Power: A Wizard's Arithmetic", fontsize=20, fontweight='bold')

axs.flatten()[-1].barh(wizardry_schools, average_power_levels, color=single_color)
axs.flatten()[-1].set_title('Mean Power Levels for Spells', fontsize=16, fontweight='bold')
axs.flatten()[-1].set_xlabel('Strength Meter (1-10)')
axs.flatten()[-1].set_xlim(0, 10)

plt.tight_layout()
plt.show()