import matplotlib.pyplot as plt
import numpy as np

# Define artificial data for each vegetable type, adding stem and bulb vegetables
root_vegetables = [1.8, 2.0, 1.9, 2.1, 1.75, 2.2, 1.95, 2.15, 1.85]
leaf_vegetables = [3.4, 3.6, 3.5, 3.3, 3.8, 3.2, 3.7, 3.4, 3.9]
fruit_vegetables = [2.6, 2.8, 2.7, 2.5, 2.9, 2.4, 2.75, 2.85, 2.65]
stem_vegetables = [1.3, 1.5, 1.4, 1.2, 1.6, 1.25, 1.45, 1.35, 1.55]
bulb_vegetables = [3.0, 2.8, 2.9, 3.1, 2.7, 2.95, 2.85, 3.05, 2.75]

# Create variations data for the violin plot
variation_factors = [0.8, 0.75, 0.85, 0.7, 0.9, 0.65, 0.8, 0.95, 0.7]
root_vegetables_var = np.multiply(root_vegetables, variation_factors)
leaf_vegetables_var = np.multiply(leaf_vegetables, variation_factors)
fruit_vegetables_var = np.multiply(fruit_vegetables, variation_factors)
stem_vegetables_var = np.multiply(stem_vegetables, variation_factors)
bulb_vegetables_var = np.multiply(bulb_vegetables, variation_factors)

# Prepare data for the plots
box_plot_data = [root_vegetables, leaf_vegetables, fruit_vegetables, stem_vegetables, bulb_vegetables]
violin_plot_data = [root_vegetables_var, leaf_vegetables_var, fruit_vegetables_var, stem_vegetables_var, bulb_vegetables_var]
labels = ["Root Vegetables", "Leaf Vegetables", "Fruit Vegetables", "Stem Vegetables", "Bulb Vegetables"]

# Create subplots
fig, axs = plt.subplots(2, 1, figsize=(12, 12))

# First subplot: Violin plot
violin_parts = axs[0].violinplot(violin_plot_data, vert=False, showmeans=False, showmedians=True)

# Customizing color of violin plots
colors = ['lightblue', 'lightgreen', 'lightcoral', 'wheat', 'orchid']
for pc, color in zip(violin_parts['bodies'], colors):
    pc.set_facecolor(color)
    pc.set_edgecolor('navy')
    pc.set_alpha(0.6)

# Set color for median lines
violin_parts['cmedians'].set_color('darkred')
violin_parts['cmedians'].set_linewidth(2)

# Titles and labels for the violin plot
axs[0].set_title("Distribution of Nutrient Concentrations in Vegetables", fontsize=15, fontweight='bold')
axs[0].set_xlabel("Nutrient Concentration with Variability", fontsize=12)
axs[0].set_yticks(np.arange(1, len(labels) + 1))
axs[0].set_yticklabels(labels, fontsize=12)

# Second subplot: Box plot with overlay of individual data points
axs[1].boxplot(box_plot_data, vert=False, patch_artist=True, notch=True, 
               boxprops=dict(facecolor='skyblue', color='navy', linewidth=2),
               whiskerprops=dict(color='navy', linewidth=2),
               capprops=dict(color='navy', linewidth=2),
               medianprops=dict(color='darkred', linewidth=2))

# Overlaying individual data points
for i, data in enumerate(box_plot_data):
    y = np.random.normal(i + 1, 0.04, size=len(data))
    axs[1].scatter(data, y, alpha=0.6, color=colors[i], edgecolor='darkblue', linewidth=0.7)

# Titles and labels for the box plot
axs[1].set_title("Vegetables Nutrient Profiles with Individual Data Points", fontsize=15, fontweight='bold')
axs[1].set_xlabel("Nutrient Concentration", fontsize=12)
axs[1].set_yticks(np.arange(1, len(labels) + 1))
axs[1].set_yticklabels(labels, fontsize=12)

# Adjust layout for both plots
plt.tight_layout()

# Show the plot
plt.show()