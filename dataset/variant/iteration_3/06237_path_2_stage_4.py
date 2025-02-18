import matplotlib.pyplot as plt
import numpy as np

vegetables = ['Tomatoes', 'Carrots', 'Lettuce', 'Peppers', 'Cucumbers', 'Zucchini', 'Spinach', 'Beans']
gardeners = [70, 100, 55, 120, 65, 85, 95, 60]

# Shuffled colors for the bars
colors = ['#81C784', '#9575CD', '#FFD54F', '#4DD0E1', '#A1887F', '#64B5F6', '#E57373', '#FF8A65']

fig, ax = plt.subplots(figsize=(12, 5))

ax.barh(vegetables, gardeners, color=colors, alpha=0.8)
ax.set_title("Community Gardeners' Favorite Vegetables", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Number of Gardeners', fontsize=14)
ax.set_ylabel('Vegetable Types', fontsize=14)
ax.tick_params(axis='y', rotation=45, labelsize=12)
ax.tick_params(axis='x', labelsize=12)

plt.tight_layout()
plt.show()