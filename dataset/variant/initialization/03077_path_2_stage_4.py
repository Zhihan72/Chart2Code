import matplotlib.pyplot as plt
import numpy as np

centuries = np.arange(14, 22)

classical = [60, 55, 45, 30, 20, 10, 5, 0]
renaissance = [20, 30, 40, 35, 25, 10, 5, 0]
baroque = [10, 10, 10, 20, 30, 40, 30, 0]
modernism = [5, 5, 10, 15, 20, 30, 40, 60]
abstract = [5, 0, 0, 0, 5, 10, 20, 40]
cubism = [0, 0, 5, 10, 15, 25, 30, 20]
popart = [0, 0, 0, 5, 10, 20, 30, 50]

famous_artworks = [150, 170, 220, 250, 300, 350, 400, 450]

data = np.array([classical, renaissance, baroque, modernism, abstract, cubism, popart])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

ax1.stackplot(centuries, data, alpha=0.8)
ax1.set_title("Artistic Evolution by Century", fontsize=14, fontweight='bold', pad=20)
ax1.set_xlabel('Century', fontsize=12)
ax1.set_ylabel('Popularity (%)', fontsize=12)

ax2.plot(centuries, famous_artworks, marker='o', linestyle='-', color='darkcyan')
ax2.set_title('Trend of Famous Artworks', fontsize=14, fontweight='bold', pad=20)
ax2.set_xlabel('Century', fontsize=12)
ax2.set_ylabel('Number', fontsize=12)

plt.tight_layout()
plt.show()