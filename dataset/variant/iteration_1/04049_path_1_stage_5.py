import matplotlib.pyplot as plt
import numpy as np

# Data: Vitamin C content (mg/100g) for different fruit groups
citrus_fruits = [53.2, 60.1, 90.8, 88.3, 80.5, 45.2, 49.8]
berries = [12.1, 58.8, 67.7, 21.3, 79.7, 14.5]
tropical_fruits = [61.1, 30.2, 36.4, 45.4, 52.4, 39.2, 55.8, 47.6]
stone_fruits = [6.6, 8.4, 10.3, 4.9, 11.9, 13.2]
pomes = [5.4, 14.3, 13.6, 10.1, 15.7]
melons = [18.3, 13.0, 24.5, 17.8, 19.7, 16.2]
dragons = [75.3, 82.5, 70.4, 65.8, 78.0]

data = [citrus_fruits, berries, tropical_fruits, stone_fruits, pomes, melons, dragons]
fruit_groups = ['Berries', 'Tropical Fruits', 'Citrus Fruits', 'Pomes', 'Stone Fruits', 'Melons', 'Dragons']

fig, ax = plt.subplots(figsize=(12, 7))
box_colors = ['#FF55AA', '#55FFAA', '#AA55FF', '#FFAA55', '#55AAFF', '#FFFF55', '#55FFFF']

bp = ax.boxplot(data, vert=False, patch_artist=True, notch=True, whis=1.5)

for patch, color in zip(bp['boxes'], box_colors):
    patch.set_facecolor(color)

ax.set_yticklabels(fruit_groups, fontsize=11)
ax.set_xlabel('Vitamin C Content per 100g (mg)', fontsize=12)
ax.set_title('Diverse Fruit Vitamin Analysis:\nA Comprehensive Study', fontsize=14, pad=20)

plt.tight_layout()
plt.show()