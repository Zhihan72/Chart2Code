import matplotlib.pyplot as plt
import numpy as np

# Data Creation
wizardry_schools = ['Arcane Academy', 'Mystic Institute', 'Elemental Guild', 'Enchantment Realm']
spell_types = ['Fire Spells', 'Water Spells', 'Earth Spells', 'Air Spells', 'Lightning Spells', 'Healing Spells']

arcane_spells = [25, 5, 20, 10, 30, 10]
mystic_spells = [15, 30, 10, 25, 0, 20]
elemental_spells = [35, 5, 20, 25, 15, 0]
enchantment_spells = [10, 10, 15, 15, 25, 25]

average_power_levels = [8, 6, 7, 9]

# Define a single color for all data groups
single_color = '#66b3ff'

# Create the figure and axis for subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9))

# Plotting the pie charts for each Wizardry school
data = [arcane_spells, mystic_spells, elemental_spells, enchantment_spells]

for i, school_data in enumerate(data):
    ax1.clear()
    ax1.pie(
        school_data,
        autopct='%1.1f%%',
        pctdistance=0.85,
        colors=[single_color] * len(school_data),
        startangle=90,
        wedgeprops=dict(width=0.4, edgecolor='w')
    )
    center_circle = plt.Circle((0, 0), 0.55, fc='white')
    ax1.add_artist(center_circle)
    ax1.set_title(wizardry_schools[i], fontsize=16, fontweight='bold', loc='center')
    plt.pause(1)

fig.suptitle("Spell Casting Distribution & Average Power Levels", fontsize=20, fontweight='bold')

# Plotting the bar chart showing average power levels
ax2.barh(wizardry_schools, average_power_levels, color=single_color)
ax2.set_title('Average Spell Power Levels', fontsize=16, fontweight='bold')
ax2.set_xlabel('Power Level (1-10)')
ax2.set_xlim(0, 10)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()