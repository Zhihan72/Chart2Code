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

# Bar chart without textual elements
ax.bar(bar_positions - 1.5 * bar_width, xylot_output, width=bar_width, color='#ff9999', edgecolor='#333333', linestyle='-', hatch='\\')
ax.bar(bar_positions - 0.5 * bar_width, zarnon_output, width=bar_width, color='#66b3ff', edgecolor='#666666', linestyle='--', hatch='|')
ax.bar(bar_positions + 0.5 * bar_width, kryla_output, width=bar_width, color='#99ff99', edgecolor='#999999', linestyle='-.', hatch='o')
ax.bar(bar_positions + 1.5 * bar_width, lunar_output, width=bar_width, color='#ffcc99', edgecolor='#cccccc', linestyle=':', hatch='*')

ax.set_xticks(bar_positions)
ax.set_xticklabels([''] * len(produce_types))  # Removing group labels

ax.yaxis.grid(True, linestyle='-', alpha=0.5)

plt.tight_layout()
plt.show()