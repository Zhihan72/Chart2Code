import matplotlib.pyplot as plt
import numpy as np

positive_side = np.array([2500, 1000, 800, 300, 600, 400])
negative_side = np.array([1500, 1200, 500, 1000, 500, 200, 300])

consumption = np.concatenate([-negative_side, positive_side])

colors = ['#66b3ff', '#ffcc99', '#99ff99', '#ff9999', '#c2c2f0', '#ffb3e6', '#99ff99', 
          '#66b3ff', '#ff9999', '#ffcc99', '#c2c2f0', '#ffcc99', '#ff9999']

fig, ax = plt.subplots(figsize=(12, 10))
y_pos = np.arange(len(consumption))

# Randomly altered: line style, marker
ax.barh(y_pos, consumption, color=colors, edgecolor='black', linestyle='--', hatch='/')

for i in range(len(consumption)):
    ax.text(consumption[i], y_pos[i], f'{abs(consumption[i]):d}', va='center', ha='center', color='black', fontsize=9)

# Randomly altered: removed borders and added grid
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(which='major', linestyle='-', linewidth='0.5', color='gray', axis='x')

ax.set_yticks([])

plt.tight_layout()
plt.show()