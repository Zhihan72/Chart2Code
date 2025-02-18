import matplotlib.pyplot as plt
import numpy as np

# Data for each vegetable type
root_vegetables = [1.8, 2.0, 1.9, 2.1, 1.75, 2.2, 1.95, 2.15, 1.85]
leaf_vegetables = [3.4, 3.6, 3.5, 3.3, 3.8, 3.2, 3.7, 3.4, 3.9]
fruit_vegetables = [2.6, 2.8, 2.7, 2.5, 2.9, 2.4, 2.75, 2.85, 2.65]

# Variation data for violin plot
variation_factors = [0.8, 0.75, 0.85, 0.7, 0.9, 0.65, 0.8, 0.95, 0.7]
root_vegetables_var = np.multiply(root_vegetables, variation_factors)
leaf_vegetables_var = np.multiply(leaf_vegetables, variation_factors)
fruit_vegetables_var = np.multiply(fruit_vegetables, variation_factors)

# Prepare data
box_plot_data = [root_vegetables, leaf_vegetables, fruit_vegetables]
violin_plot_data = [root_vegetables_var, leaf_vegetables_var, fruit_vegetables_var]
labels = ["Root", "Leaf", "Fruit"]

# Create subplots
fig, axs = plt.subplots(2, 1, figsize=(12, 10))

# Violin plot
violin_parts = axs[0].violinplot(violin_plot_data, vert=False, showmeans=False, showmedians=True)

# Apply a single color
common_color = 'lightblue'
for pc in violin_parts['bodies']:
    pc.set_facecolor(common_color)
    pc.set_edgecolor('navy')
    pc.set_alpha(0.6)

# Set color for median lines
violin_parts['cmedians'].set_color('darkred')
violin_parts['cmedians'].set_linewidth(2)

# Titles and labels
axs[0].set_title("Nutrient Distribution", fontsize=15, fontweight='bold')
axs[0].set_xlabel("Concentration (Var.)", fontsize=12)
axs[0].set_yticks(np.arange(1, len(labels) + 1))
axs[0].set_yticklabels(labels, fontsize=12)

# Box plot
axs[1].boxplot(box_plot_data, vert=False, patch_artist=True, notch=True, 
               boxprops=dict(facecolor=common_color, color='navy', linewidth=2),
               whiskerprops=dict(color='navy', linewidth=2),
               capprops=dict(color='navy', linewidth=2),
               medianprops=dict(color='darkred', linewidth=2))

# Overlay individual data points
for i, data in enumerate(box_plot_data):
    y = np.random.normal(i + 1, 0.04, size=len(data))
    axs[1].scatter(data, y, alpha=0.6, color=common_color, edgecolor='darkblue', linewidth=0.7)

# Titles and labels
axs[1].set_title("Nutrient Profiles", fontsize=15, fontweight='bold')
axs[1].set_xlabel("Concentration", fontsize=12)
axs[1].set_yticks(np.arange(1, len(labels) + 1))
axs[1].set_yticklabels(labels, fontsize=12)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()