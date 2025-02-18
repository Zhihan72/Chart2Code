import matplotlib.pyplot as plt
import numpy as np

root_vegetables = [1.8, 2.0, 1.9, 2.1, 1.75, 2.2, 1.95, 2.15, 1.85]
leaf_vegetables = [3.4, 3.6, 3.5, 3.3, 3.8, 3.2, 3.7, 3.4, 3.9]
fruit_vegetables = [2.6, 2.8, 2.7, 2.5, 2.9, 2.4, 2.75, 2.85, 2.65]
bean_vegetables = [1.1, 1.3, 1.2, 1.15, 1.25, 1.35, 1.0, 1.05, 1.2]
bulb_vegetables = [2.9, 3.0, 2.95, 3.05, 3.1, 3.2, 3.15, 3.0, 2.85]

variation_factors = [0.8, 0.75, 0.85, 0.7, 0.9, 0.65, 0.8, 0.95, 0.7]
root_vegetables_var = np.multiply(root_vegetables, variation_factors)
leaf_vegetables_var = np.multiply(leaf_vegetables, variation_factors)
fruit_vegetables_var = np.multiply(fruit_vegetables, variation_factors)
bean_vegetables_var = np.multiply(bean_vegetables, variation_factors)
bulb_vegetables_var = np.multiply(bulb_vegetables, variation_factors)

box_plot_data = [root_vegetables, leaf_vegetables, fruit_vegetables, bean_vegetables, bulb_vegetables]
violin_plot_data = [root_vegetables_var, leaf_vegetables_var, fruit_vegetables_var, bean_vegetables_var, bulb_vegetables_var]
labels = ["Root", "Leaf", "Fruit", "Bean", "Bulb"]

fig, axs = plt.subplots(2, 1, figsize=(12, 12))

# Violin plot
violin_parts = axs[0].violinplot(violin_plot_data, vert=False, showmeans=True, showmedians=False)
common_color = 'lightgreen'
for pc in violin_parts['bodies']:
    pc.set_facecolor(common_color)
    pc.set_edgecolor('black')
    pc.set_alpha(0.5)

violin_parts['cmeans'].set_color('darkorange')
violin_parts['cmeans'].set_linestyle('--')

axs[0].set_title("Nutrient Distribution", fontsize=15, fontweight='bold', color='darkblue')
axs[0].set_xlabel("Concentration (Var.)", fontsize=12, color='darkblue')
axs[0].set_yticks(np.arange(1, len(labels) + 1))
axs[0].set_yticklabels(labels, fontsize=12, color='darkblue')
axs[0].grid(which='both', linestyle=':', linewidth=0.5)

# Box plot
axs[1].boxplot(box_plot_data, vert=False, patch_artist=True, notch=False, 
               boxprops=dict(facecolor=common_color, color='black', linewidth=2),
               whiskerprops=dict(color='black', linewidth=1),
               capprops=dict(color='black', linewidth=1),
               medianprops=dict(color='darkorange', linewidth=2, linestyle='-.'))

for i, data in enumerate(box_plot_data):
    y = np.random.normal(i + 1, 0.02, size=len(data))
    axs[1].scatter(data, y, alpha=0.6, color='darkorange', edgecolor='purple', marker='d')

axs[1].set_title("Nutrient Profiles", fontsize=15, fontweight='bold', color='darkblue')
axs[1].set_xlabel("Concentration", fontsize=12, color='darkblue')
axs[1].set_yticks(np.arange(1, len(labels) + 1))
axs[1].set_yticklabels(labels, fontsize=12, color='darkblue')
axs[1].grid(which='minor', linestyle='--', linewidth=0.5)

plt.tight_layout()
plt.show()