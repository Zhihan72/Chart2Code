import matplotlib.pyplot as plt
import numpy as np

wizardry_schools = ['Arcane Academy', 'Mystic Institute', 'Elemental Guild', 'Enchantment Realm']
spell_types = ['Fire Spells', 'Water Spells', 'Earth Spells', 'Air Spells', 'Lightning Spells', 'Healing Spells']

arcane_spells = [25, 5, 20, 10, 30, 10]
mystic_spells = [15, 30, 10, 25, 0, 20]
elemental_spells = [35, 5, 20, 25, 15, 0]
enchantment_spells = [10, 10, 15, 15, 25, 25]

average_power_levels = [8, 6, 7, 9]

single_color = '#66b3ff'

# Create the figure and axis for subplots with a different arrangement (2 rows, 2 columns)
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

fig.suptitle("Spell Casting Distribution & Average Power Levels", fontsize=20, fontweight='bold')

# Plotting the bar chart showing average power levels in the last subplot
axs.flatten()[-1].barh(wizardry_schools, average_power_levels, color=single_color)
axs.flatten()[-1].set_title('Average Spell Power Levels', fontsize=16, fontweight='bold')
axs.flatten()[-1].set_xlabel('Power Level (1-10)')
axs.flatten()[-1].set_xlim(0, 10)

plt.tight_layout()
plt.show()