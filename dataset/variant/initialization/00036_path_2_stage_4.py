import matplotlib.pyplot as plt
import numpy as np

positive_side = np.array([2500, 1000, 800, 300, 600, 400])
negative_side = np.array([1500, 1200, 500, 1000, 500, 200, 300])

consumption = np.concatenate([-negative_side, positive_side])

# Shuffled colors
colors = ['#ffcc99', '#66b3ff', '#99ff99', '#ff9999', '#c2c2f0', '#ffb3e6', '#66b3ff', '#99ff99', '#ff9999', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ff9999']

fig, ax = plt.subplots(figsize=(12, 10))
y_pos = np.arange(len(consumption))

ax.barh(y_pos, consumption, color=colors, edgecolor='gray')

for i in range(len(consumption)):
    ax.text(consumption[i], y_pos[i], f'{abs(consumption[i]):d}', va='center', ha='center', color='black', fontsize=9)

ax.set_yticks([])  # Remove y-axis ticks

plt.tight_layout()
plt.show()