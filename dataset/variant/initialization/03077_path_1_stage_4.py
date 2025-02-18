import matplotlib.pyplot as plt
import numpy as np

centuries = np.arange(14, 22)

# Original data groups
classical = [60, 55, 45, 30, 20, 10, 5, 0]
renaissance = [20, 30, 40, 35, 25, 10, 5, 0]
baroque = [10, 10, 10, 20, 30, 40, 30, 0]
modernism = [5, 5, 10, 15, 20, 30, 40, 60]
abstract = [5, 0, 0, 0, 5, 10, 20, 40]
famous_artworks = [150, 170, 220, 250, 300, 350, 400, 450]

# Shuffling the original arrays
classical_shuffled = [30, 5, 20, 10, 60, 0, 45, 55]
renaissance_shuffled = [5, 35, 30, 25, 40, 20, 0, 10]
baroque_shuffled = [30, 0, 10, 10, 10, 40, 20, 30]
modernism_shuffled = [20, 5, 40, 30, 5, 15, 60, 10]
abstract_shuffled = [10, 40, 0, 5, 20, 0, 5, 0]

data = np.array([classical_shuffled, renaissance_shuffled, baroque_shuffled, modernism_shuffled, abstract_shuffled])

color = '#4682B4'

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Stackplot with shuffled data
ax1.stackplot(centuries, data, colors=[color]*5, alpha=0.7)
ax1.grid(axis='both', color='black', linestyle=':', linewidth=0.7)

# Line plot for famous artworks
ax2.plot(centuries, famous_artworks, marker='^', linestyle=':', color=color)
ax2.grid(axis='both', color='black', linestyle='-', linewidth=0.7)

plt.tight_layout()
plt.show()