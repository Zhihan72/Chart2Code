import matplotlib.pyplot as plt
import numpy as np

# Data for plotting horizontal box charts
data = {
    'Tubers': np.array([10, 12, 14, 18, 22, 28, 34, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155]),
    'Legumes': np.array([5, 7, 9, 12, 16, 20, 25, 30, 36, 42, 48, 55, 62, 70, 78, 87, 96, 106, 116, 127, 138, 150, 162, 175, 188, 202, 216, 231, 246, 262, 278]),
    'Fruits': np.array([2, 3, 5, 7, 10, 15, 20, 26, 32, 39, 46, 54, 63, 72, 82, 92, 103, 114, 126, 139, 152, 166, 181, 196, 212, 229, 247, 266, 285, 305, 325])
}

fig, ax = plt.subplots(figsize=(10, 7))

# Create horizontal box plots
ax.boxplot(data.values(), vert=False, patch_artist=True,
           boxprops=dict(facecolor='#FFD700', color='black', linewidth=1.2),
           medianprops=dict(color='red', linewidth=1.5),
           whiskerprops=dict(color='black', linewidth=1.2),
           capprops=dict(color='black', linewidth=1.2),
           flierprops=dict(marker='o', color='black', markersize=5, alpha=0.5))

# Set y-ticks to category labels
ax.set_yticklabels(data.keys(), fontsize=12)

# Set plot titles and labels
ax.set_title("Mars Colony Annual Food Production (2040-2070)", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel("Production Volume (Tons)", fontsize=14)

plt.tight_layout()
plt.show()