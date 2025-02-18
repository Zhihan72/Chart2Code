import matplotlib.pyplot as plt
import numpy as np

# Data Creation
wizardry_schools = ['Arcane Academy', 'Mystic Institute', 'Elemental Guild', 'Enchantment Realm']
spell_types = ['Fire Spells', 'Water Spells', 'Earth Spells', 'Air Spells', 'Lightning Spells', 'Healing Spells']

# Spells cast by each school (in percentage of total spells)
arcane_spells = [25, 5, 20, 10, 30, 10]
mystic_spells = [15, 30, 10, 25, 0, 20]
elemental_spells = [35, 5, 20, 25, 15, 0]
enchantment_spells = [10, 10, 15, 15, 25, 25]

# Average power level of spells by each school (1-10 scale)
average_power_levels = [8, 6, 7, 9]

# Colors for each spell type
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Create the figure and axis for subplots
fig, (ax2, ax1) = plt.subplots(1, 2, figsize=(18, 9))

# Plotting the bar chart showing average power levels
ax2.barh(wizardry_schools, average_power_levels, color='#85e085')
ax2.set_title('Average Spell Power Levels', fontsize=16, fontweight='bold')
ax2.set_xlabel('Power Level (1-10)')
ax2.set_xlim(0, 10)

# Plotting the pie charts for each Wizardry school
data = [arcane_spells, mystic_spells, elemental_spells, enchantment_spells]

for i, school_data in enumerate(data):
    ax1.clear()
    wedges, texts, autotexts = ax1.pie(
        school_data,
        labels=spell_types,
        autopct='%1.1f%%',
        pctdistance=0.85,
        colors=colors,
        startangle=90,
        wedgeprops=dict(width=0.4, edgecolor='w')
    )
    plt.setp(texts, size=12, weight='semibold')
    plt.setp(autotexts, size=10, weight='semibold')
    center_circle = plt.Circle((0, 0), 0.55, fc='white')
    fig.gca().add_artist(center_circle)
    ax1.set_title(wizardry_schools[i], fontsize=16, fontweight='bold', loc='center')
    plt.pause(1)

# Title for the main figure
fig.suptitle("Spell Casting Distribution in the Grand Magical Tournament & Average Power Levels", fontsize=20, fontweight='bold')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()