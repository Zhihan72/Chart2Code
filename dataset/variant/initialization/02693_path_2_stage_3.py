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

# Altered bar chart styles
ax.bar(bar_positions - 1.5 * bar_width, xylot_output, width=bar_width, label='Xylot', color='#ff9999', edgecolor='#333333', linestyle='-', hatch='\\')
ax.bar(bar_positions - 0.5 * bar_width, zarnon_output, width=bar_width, label='Zarnon', color='#66b3ff', edgecolor='#666666', linestyle='--', hatch='|')
ax.bar(bar_positions + 0.5 * bar_width, kryla_output, width=bar_width, label='Kryla', color='#99ff99', edgecolor='#999999', linestyle='-.', hatch='o')
ax.bar(bar_positions + 1.5 * bar_width, lunar_output, width=bar_width, label='Lunar', color='#ffcc99', edgecolor='#cccccc', linestyle=':', hatch='*')

ax.set_title('Intergalactic Produce Distribution\nAcross Andromeda\'s Planets', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Type of Produce', fontsize=12)
ax.set_ylabel('Total Production (Units)', fontsize=12)
ax.set_xticks(bar_positions)
ax.set_xticklabels(produce_types, fontsize=10, rotation=15)
ax.legend(title='Planet', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10, title_fontsize='11')

# Altered grid style
ax.yaxis.grid(True, linestyle='-', alpha=0.5)

# Adjusted layout
plt.tight_layout()
plt.show()