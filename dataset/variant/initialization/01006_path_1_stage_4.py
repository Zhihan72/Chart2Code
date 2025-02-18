import matplotlib.pyplot as plt
import numpy as np

decades = ['1980s', '2000s', '2020s']
adventure = np.array([10, 20, 30])
cultural = np.array([30, 30, 25])
relaxation = np.array([40, 35, 40])
data = np.vstack([adventure, cultural, relaxation])

single_color = '#66b3ff'

fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(decades, data, colors=[single_color]*3, alpha=0.8)

ax.legend(loc='lower right', fontsize=11, bbox_to_anchor=(1, 0))
ax.grid(axis='x', linestyle='-.', alpha=0.5)

ax.set_yticks(np.arange(0, 101, 10))
ax.set_xticks(decades)
ax.set_xticklabels(decades, rotation=45, fontsize=11)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()