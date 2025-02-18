import matplotlib.pyplot as plt
import numpy as np

regions = ['N', 'S', 'E', 'W']
reusable_bags = [950, 1100, 800, 1200]
solar_chargers = [920, 700, 750, 850]
bamboo_toothbrushes = [610, 720, 580, 530]

fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.2
y_pos = np.arange(len(regions))

ax.barh(y_pos - bar_width, reusable_bags, bar_width, label='Bags', color='#ff6f61', edgecolor='black', linestyle='-', hatch='/')
ax.barh(y_pos, solar_chargers, bar_width, label='Chargers', color='#6b5b95', edgecolor='black', linestyle='--', hatch='\\')
ax.barh(y_pos + bar_width, bamboo_toothbrushes, bar_width, label='Brushes', color='#88b04b', edgecolor='black', linestyle=':', hatch='-')

ax.set_yticks(y_pos)
ax.set_yticklabels(regions, fontsize=11)
ax.set_xlabel('Units', fontsize=11)
ax.set_title('Campaign Impact', fontsize=14, fontweight='bold', pad=15)

ax.legend(title='Products', loc='lower right', fontsize=9, shadow=True, fancybox=True)

plt.grid(visible=False)

for i in range(len(regions)):
    ax.text(reusable_bags[i] + 20, i - bar_width, str(reusable_bags[i]), va='center', color='black', fontsize=9)
    ax.text(solar_chargers[i] + 20, i, str(solar_chargers[i]), va='center', color='black', fontsize=9)
    ax.text(bamboo_toothbrushes[i] + 20, i + bar_width, str(bamboo_toothbrushes[i]), va='center', color='black', fontsize=9)

plt.tight_layout()
plt.show()