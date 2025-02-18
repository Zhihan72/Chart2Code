import matplotlib.pyplot as plt
import numpy as np

classical_music = [2.7, 2.8, 3.0, 2.6, 2.9, 2.3, 2.5, 2.1, 2.8, 2.7]
jazz_music = [4.6, 4.1, 4.4, 4.2, 4.7, 4.0, 4.3, 4.5, 4.8, 4.2]
rock_music = [6.8, 6.9, 6.7, 7.0, 6.6, 6.5, 6.9, 6.5, 6.8, 6.7]
electronic_music = [8.7, 8.3, 8.9, 8.5, 8.4, 8.8, 8.4, 8.5, 8.6, 8.6]

variation_factors = [0.95, 0.9, 1.05, 1.1, 1.08, 0.98, 0.96, 1.0, 1.07, 1.02]
classical_var = np.multiply(classical_music, variation_factors)
jazz_var = np.multiply(jazz_music, variation_factors)
rock_var = np.multiply(rock_music, variation_factors)
electronic_var = np.multiply(electronic_music, variation_factors)

violin_plot_data = [classical_var, jazz_var, rock_var, electronic_var]

fig, ax = plt.subplots(figsize=(10, 6))

violin_parts = ax.violinplot(violin_plot_data, vert=False, showmeans=True, showextrema=True)

# Manually shuffled the colors
colors = ['lightcoral', 'thistle', 'lightseagreen', 'lavender']
for pc, color in zip(violin_parts['bodies'], colors):
    pc.set_facecolor(color)
    pc.set_edgecolor('grey')
    pc.set_alpha(0.6)

for i, data in enumerate(violin_plot_data, start=1):
    median = np.median(data)
    mean = np.mean(data)
    ax.scatter(median, i, color='blue', zorder=3)
    ax.scatter(mean, i, color='orange', zorder=3)

ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()