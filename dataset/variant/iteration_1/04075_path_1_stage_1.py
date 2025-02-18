import matplotlib.pyplot as plt
import numpy as np

# Data representing the spectral ranges used in various genres of music
classical_music = [2.1, 2.3, 2.8, 2.7, 2.5, 2.6, 2.9, 3.0, 2.8, 2.7]
jazz_music = [4.0, 4.2, 4.4, 4.5, 4.6, 4.3, 4.2, 4.1, 4.8, 4.7]
rock_music = [6.5, 6.6, 6.7, 6.8, 6.9, 6.7, 6.5, 6.8, 6.9, 7.0]
electronic_music = [8.3, 8.4, 8.5, 8.6, 8.7, 8.6, 8.5, 8.4, 8.8, 8.9]

# Variation factors for realism in the data
variation_factors = [0.95, 0.9, 1.05, 1.1, 1.08, 0.98, 0.96, 1.0, 1.07, 1.02]
classical_var = np.multiply(classical_music, variation_factors)
jazz_var = np.multiply(jazz_music, variation_factors)
rock_var = np.multiply(rock_music, variation_factors)
electronic_var = np.multiply(electronic_music, variation_factors)

# Prepare data for violin plot
violin_plot_data = [classical_var, jazz_var, rock_var, electronic_var]
labels = ["Classical", "Jazz", "Rock", "Electronic"]

# Create the figure and a subplot for the horizontal violin plot
fig, ax = plt.subplots(figsize=(10, 6))

# Create a horizontal violin plot
violin_parts = ax.violinplot(violin_plot_data, vert=False, showmeans=False, showmedians=True)

# Colors for the violin plot
colors = ['lightyellow', 'lightblue', 'lightgreen', 'lightpink']
for pc, color in zip(violin_parts['bodies'], colors):
    pc.set_facecolor(color)
    pc.set_edgecolor('black')
    pc.set_alpha(0.7)

# Set color for median lines
violin_parts['cmedians'].set_color('red')
violin_parts['cmedians'].set_linewidth(2)

# Titles and labels
ax.set_title("Spectral Richness Across Different Music Genres", fontsize=16, fontweight='bold')
ax.set_xlabel("Spectral Usage in Music", fontsize=12)
ax.set_yticks(np.arange(1, len(labels) + 1))
ax.set_yticklabels(labels, fontsize=12)

# Annotations for additional insights
ax.annotate('Broad variation in Electronic', xy=(8.5, 4), xytext=(9.3, 4),
            arrowprops=dict(facecolor='black', arrowstyle="->"),
            fontsize=10, fontweight='bold')
ax.annotate('Stable median', xy=(6.8, 3), xytext=(7.5, 3),
            arrowprops=dict(facecolor='black', arrowstyle="->"),
            fontsize=10, fontweight='bold')

# Adjust layout to ensure no overlapping elements
plt.tight_layout()

# Show the plot
plt.show()