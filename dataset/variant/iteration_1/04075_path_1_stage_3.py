import matplotlib.pyplot as plt
import numpy as np

# Manually altered data for each music genre
classical_music = [2.7, 2.8, 3.0, 2.6, 2.9, 2.3, 2.5, 2.1, 2.8, 2.7]  # Swapped a few values
jazz_music = [4.6, 4.1, 4.4, 4.2, 4.7, 4.0, 4.3, 4.5, 4.8, 4.2]      # Swapped a few values
rock_music = [6.8, 6.9, 6.7, 7.0, 6.6, 6.5, 6.9, 6.5, 6.8, 6.7]      # Swapped a few values
electronic_music = [8.7, 8.3, 8.9, 8.5, 8.4, 8.8, 8.4, 8.5, 8.6, 8.6] # Swapped a few values

variation_factors = [0.95, 0.9, 1.05, 1.1, 1.08, 0.98, 0.96, 1.0, 1.07, 1.02] 
classical_var = np.multiply(classical_music, variation_factors)
jazz_var = np.multiply(jazz_music, variation_factors)
rock_var = np.multiply(rock_music, variation_factors)
electronic_var = np.multiply(electronic_music, variation_factors)

violin_plot_data = [classical_var, jazz_var, rock_var, electronic_var]
labels = ["Classical", "Jazz", "Rock", "Electronic"]

fig, ax = plt.subplots(figsize=(10, 6))

violin_parts = ax.violinplot(violin_plot_data, vert=False, showmeans=True, showextrema=True)

colors = ['lavender', 'lightcoral', 'lightseagreen', 'thistle']
for pc, color in zip(violin_parts['bodies'], colors):
    pc.set_facecolor(color)
    pc.set_edgecolor('grey')
    pc.set_alpha(0.6)

for i, data in enumerate(violin_plot_data, start=1):
    median = np.median(data)
    mean = np.mean(data)
    ax.scatter(median, i, color='blue', label="Median" if i == 1 else "", zorder=3)
    ax.scatter(mean, i, color='orange', label="Mean" if i == 1 else "", zorder=3)

ax.set_title("Spectral Richness Across Music Genres", fontsize=14, fontweight='regular')
ax.set_xlabel("Spectral Usage", fontsize=11)
ax.set_yticks(np.arange(1, len(labels) + 1))
ax.set_yticklabels(labels, fontsize=11)

ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax.annotate('Electronic Diversity', xy=(8.5, 4), xytext=(9.3, 3.8),
            arrowprops=dict(facecolor='grey', arrowstyle="wedge"),
            fontsize=9, fontweight='regular')
ax.annotate('Consistent Rock Median', xy=(6.8, 3), xytext=(5.5, 2.5),
            arrowprops=dict(facecolor='grey', arrowstyle="->"),
            fontsize=9, fontweight='regular')

plt.tight_layout()
plt.show()