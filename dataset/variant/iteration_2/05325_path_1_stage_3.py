import matplotlib.pyplot as plt
import numpy as np

root_vegetables = [1.8, 2.0, 1.9, 2.1, 1.75, 2.2, 1.95, 2.15, 1.85]
leaf_vegetables = [3.4, 3.6, 3.5, 3.3, 3.8, 3.2, 3.7, 3.4, 3.9]
fruit_vegetables = [2.6, 2.8, 2.7, 2.5, 2.9, 2.4, 2.75, 2.85, 2.65]
stem_vegetables = [1.3, 1.5, 1.4, 1.2, 1.6, 1.25, 1.45, 1.35, 1.55]
bulb_vegetables = [3.0, 2.8, 2.9, 3.1, 2.7, 2.95, 2.85, 3.05, 2.75]

variation_factors = [0.8, 0.75, 0.85, 0.7, 0.9, 0.65, 0.8, 0.95, 0.7]
root_vegetables_var = np.multiply(root_vegetables, variation_factors)
leaf_vegetables_var = np.multiply(leaf_vegetables, variation_factors)
fruit_vegetables_var = np.multiply(fruit_vegetables, variation_factors)
stem_vegetables_var = np.multiply(stem_vegetables, variation_factors)
bulb_vegetables_var = np.multiply(bulb_vegetables, variation_factors)

box_plot_data = [root_vegetables, leaf_vegetables, fruit_vegetables, stem_vegetables, bulb_vegetables]
violin_plot_data = [root_vegetables_var, leaf_vegetables_var, fruit_vegetables_var, stem_vegetables_var, bulb_vegetables_var]
labels = ["Root Vegetables", "Leaf Vegetables", "Fruit Vegetables", "Stem Vegetables", "Bulb Vegetables"]

fig, axs = plt.subplots(2, 1, figsize=(12, 12))

# Violin plot with shuffled colors
violin_parts = axs[0].violinplot(violin_plot_data, vert=False, showmeans=False, showmedians=True)

shuffled_colors = ['lightcoral', 'orchid', 'lightblue', 'wheat', 'lightgreen']
for pc, color in zip(violin_parts['bodies'], shuffled_colors):
    pc.set_facecolor(color)
    pc.set_edgecolor('navy')
    pc.set_alpha(0.6)

violin_parts['cmedians'].set_color('darkred')
violin_parts['cmedians'].set_linewidth(2)

axs[0].set_yticks(np.arange(1, len(labels) + 1))
axs[0].set_yticklabels(labels, fontsize=12)

# Box plot with overlay of individual data points and shuffled colors
axs[1].boxplot(box_plot_data, vert=False, patch_artist=True, notch=True, 
               boxprops=dict(facecolor='skyblue', color='navy', linewidth=2),
               whiskerprops=dict(color='navy', linewidth=2),
               capprops=dict(color='navy', linewidth=2),
               medianprops=dict(color='darkred', linewidth=2))

for i, data in enumerate(box_plot_data):
    y = [i + 1] * len(data)
    axs[1].scatter(data, y, alpha=0.6, color=shuffled_colors[i], edgecolor='darkblue', linewidth=0.7)

axs[1].set_yticks(np.arange(1, len(labels) + 1))
axs[1].set_yticklabels(labels, fontsize=12)

plt.tight_layout()
plt.show()