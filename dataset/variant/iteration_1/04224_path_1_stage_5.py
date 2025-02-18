import matplotlib.pyplot as plt
import numpy as np

# Data for different categories with manually altered content
tubers = np.array([12, 10, 18, 14, 22, 28, 34, 40, 45, 50, 60, 55, 65, 70, 75, 85, 80, 90, 95, 100, 110, 105, 115, 120, 125, 130, 135, 145, 140, 150, 155])
legumes = np.array([9, 5, 7, 16, 12, 20, 30, 25, 36, 42, 48, 62, 55, 70, 78, 87, 96, 106, 116, 127, 138, 150, 162, 175, 188, 202, 216, 246, 231, 262, 278])
leafy_greens = np.array([3, 6, 4, 8, 12, 10, 15, 17, 26, 23, 20, 30, 33, 37, 41, 45, 50, 59, 54, 64, 70, 75, 81, 87, 93, 100, 106, 113, 120, 128, 135])
fruits = np.array([5, 2, 3, 7, 15, 10, 20, 26, 39, 32, 46, 54, 63, 72, 82, 92, 103, 114, 126, 139, 166, 152, 181, 196, 229, 212, 247, 266, 285, 305, 325])

# Prepare data for boxplot
data = [tubers, legumes, leafy_greens, fruits]
labels = ['Tubers', 'Legumes', 'Leafy Greens', 'Fruits']

fig, ax = plt.subplots(figsize=(12, 8))

# Create a horizontal boxplot
ax.boxplot(data, vert=False, patch_artist=True, labels=labels,
           boxprops=dict(facecolor="#FFD700", color="black"),
           whiskerprops=dict(color="black"),
           capprops=dict(color="black"),
           medianprops=dict(color="red"))

ax.set_xlabel("Volume (Tons)", fontsize=14)
ax.set_ylabel("Category", fontsize=14)

plt.tight_layout()
plt.show()