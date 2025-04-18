import matplotlib.pyplot as plt
import numpy as np

# Data setup
produce_types = ['Galactic Grains', 'Cosmic Fruits', 'Stellar Vegetables', 'Nebula Nuts', 'Astro Apples']
xylot_output = [120, 100, 80, 90, 110]
zarnon_output = [90, 130, 100, 70, 95]
kryla_output = [110, 80, 120, 60, 105]
lunar_output = [75, 95, 110, 85, 90]

bar_width = 0.2
bar_positions = np.arange(len(produce_types))

fig, ax = plt.subplots(figsize=(12, 8))

# Adjusted positions for grouped bar chart
ax.bar(bar_positions - 1.5 * bar_width, xylot_output, width=bar_width, label='Xylot', color='#d9a0f7', edgecolor='white')
ax.bar(bar_positions - 0.5 * bar_width, zarnon_output, width=bar_width, label='Zarnon', color='#66cc99', edgecolor='white')
ax.bar(bar_positions + 0.5 * bar_width, kryla_output, width=bar_width, label='Kryla', color='#4db8ff', edgecolor='white')
ax.bar(bar_positions + 1.5 * bar_width, lunar_output, width=bar_width, label='Lunar', color='#ffcc66', edgecolor='white')

ax.set_title('Intergalactic Agricultural Produce Distribution\nAcross Andromeda\'s Planets in Various Quadrants', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Type of Produce', fontsize=12)
ax.set_ylabel('Total Production (Units)', fontsize=12)
ax.set_xticks(bar_positions)
ax.set_xticklabels(produce_types, fontsize=10, rotation=15)
ax.legend(title='Planet', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10, title_fontsize='11')

# Remove stacked values and potential annotations for totals for clarity
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()