import matplotlib.pyplot as plt
import numpy as np

# Data
wizardry_schools = ['Arcane Academy', 'Mystic Institute', 'Elemental Guild', 'Enchantment Realm']

arcane_spells = [25, 5, 20, 10, 30, 10]
mystic_spells = [15, 30, 10, 25, 0, 20]
elemental_spells = [35, 5, 20, 25, 15, 0]
enchantment_spells = [10, 10, 15, 15, 25, 25]

average_power_levels = [8, 6, 7, 9]

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

fig, (ax2, ax1) = plt.subplots(1, 2, figsize=(18, 9))

# Plotting the bar chart
ax2.barh(wizardry_schools, average_power_levels, color='#85e085')
ax2.set_xlim(0, 10)

# Plotting the donut pie charts for each Wizardry school
data = [arcane_spells, mystic_spells, elemental_spells, enchantment_spells]

for i, school_data in enumerate(data):
    ax1.clear()
    wedges, texts = ax1.pie(
        school_data,
        colors=colors,
        startangle=90,
        wedgeprops=dict(width=0.3, edgecolor='w')
    )
    center_circle = plt.Circle((0, 0), 0.7, fc='white')
    ax1.add_artist(center_circle)
    plt.pause(1)

plt.tight_layout()
plt.show()