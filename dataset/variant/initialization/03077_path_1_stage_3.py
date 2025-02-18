import matplotlib.pyplot as plt
import numpy as np

centuries = np.arange(14, 22)
classical = [60, 55, 45, 30, 20, 10, 5, 0]
renaissance = [20, 30, 40, 35, 25, 10, 5, 0]
baroque = [10, 10, 10, 20, 30, 40, 30, 0]
modernism = [5, 5, 10, 15, 20, 30, 40, 60]
abstract = [5, 0, 0, 0, 5, 10, 20, 40]
famous_artworks = [150, 170, 220, 250, 300, 350, 400, 450]
data = np.array([classical, renaissance, baroque, modernism, abstract])

# Set a single color for uniformity
color = '#4682B4'

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Apply a uniform color for stackplot
ax1.stackplot(centuries, data, colors=[color]*5, alpha=0.7)
ax1.grid(axis='both', color='black', linestyle=':', linewidth=0.7)

# Use the same color for line plot
ax2.plot(centuries, famous_artworks, marker='^', linestyle=':', color=color)
ax2.grid(axis='both', color='black', linestyle='-', linewidth=0.7)

plt.tight_layout()
plt.show()