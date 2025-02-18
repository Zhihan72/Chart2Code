import matplotlib.pyplot as plt
import numpy as np

# Data setup
energy_contribution = np.array([45, 25, 15, 10])

new_colors = ['#ff5733', '#33ff57', '#3357ff', '#ff33a1']

fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(range(len(energy_contribution)), energy_contribution, color=new_colors, edgecolor='black')

for bar, contribution in zip(bars, energy_contribution):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 1, f'{height}%', va='bottom', ha='center', fontsize=10, color='black')

# Remove borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.show()