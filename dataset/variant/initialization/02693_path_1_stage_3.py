import matplotlib.pyplot as plt
import numpy as np

produce_types = ['Universal Grain', 'Fruit Cosmos', 'Stardust Veggies', 'Nebula Beans', 'Astro Pears', 'Galactic Sprouts']
xylot_output = [120, 100, 80, 90, 110, 85]
zarnon_output = [90, 130, 100, 70, 95, 75]
kryla_output = [110, 80, 120, 60, 105, 65]
lunar_output = [75, 95, 110, 85, 90, 80]
solara_output = [50, 60, 55, 65, 70, 60]

bar_positions = np.arange(len(produce_types))

fig, ax = plt.subplots(figsize=(12, 8))

ax.bar(bar_positions, xylot_output, label='Xylot', color='#ff6666', edgecolor='gray', hatch='/')
ax.bar(bar_positions, zarnon_output, bottom=xylot_output, label='Zarnon', color='#66b3ff', edgecolor='gray', hatch='\\')
ax.bar(bar_positions, kryla_output, bottom=np.array(xylot_output) + np.array(zarnon_output), label='Kryla', color='#99ff99', edgecolor='gray', hatch='|')
ax.bar(bar_positions, lunar_output, bottom=np.array(xylot_output) + np.array(zarnon_output) + np.array(kryla_output), label='Lunar', color='#ffcc99', edgecolor='gray', hatch='-')
ax.bar(bar_positions, solara_output, bottom=np.array(xylot_output) + np.array(zarnon_output) + np.array(kryla_output) + np.array(lunar_output), label='Solara', color='#c2c2f0', edgecolor='gray', hatch='o')

ax.set_title('Universal Yield of Alien Fare\nIn the Known Cosmos', fontsize=16, fontweight='light', pad=15)
ax.set_xlabel('Type of Produce', fontsize=11)
ax.set_ylabel('Yield (Cosmic Units)', fontsize=11)

ax.set_xticks(bar_positions)
ax.set_xticklabels(produce_types, fontsize=9, rotation=10)

ax.legend(title='Source World', loc='upper right', fontsize=9, title_fontsize='10')

for i, (x, z, k, l, s) in enumerate(zip(xylot_output, zarnon_output, kryla_output, lunar_output, solara_output)):
    total = x + z + k + l + s
    ax.text(i, total + 5, str(total), ha='center', fontsize=9, fontweight='light')

ax.yaxis.grid(True, linestyle='-', alpha=0.5)

plt.tight_layout()
plt.show()