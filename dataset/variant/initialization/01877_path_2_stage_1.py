import numpy as np
import matplotlib.pyplot as plt

months = np.arange(1, 13)
popularity_scores = np.array([15, 22, 10, 5, 8, 12, 20, 25, 18, 10, 6, 30])

max_radius = 10
radii = popularity_scores / popularity_scores.max() * max_radius

angles = np.linspace(0, 2 * np.pi, len(months), endpoint=False)

colors = plt.cm.viridis(np.linspace(0, 1, len(months)))
colors = colors[np.random.permutation(len(months))]  # Shuffle the color order

plt.figure(figsize=(10, 10))
ax = plt.subplot(111, polar=True)

bars = ax.bar(angles, radii, width=2*np.pi/len(months), color=colors, alpha=0.7, edgecolor='black')

month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ax.set_xticks(angles)
ax.set_xticklabels(month_labels)

ax.set_title("Festival Popularity in Harmony Bay\nby Month", va='bottom', fontsize=16, fontweight='bold')
ax.grid(color='grey', linestyle='--', linewidth=0.5, alpha=0.7)

legend_labels = [f"{month}: {score}" for month, score in zip(month_labels, popularity_scores)]
ax.legend(bars, legend_labels, loc='upper right', bbox_to_anchor=(1.3, 1.1), title="Monthly Popularity Scores")

plt.tight_layout()
plt.show()