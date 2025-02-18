import matplotlib.pyplot as plt
import numpy as np

veg = ['Tomatoes', 'Carrots', 'Lettuce', 'Peppers', 'Cucumbers', 'Zucchini', 'Spinach', 'Beans']
num_gardeners = [70, 100, 55, 120, 65, 85, 95, 60]

colors = ['#81C784', '#9575CD', '#FFD54F', '#4DD0E1', '#A1887F', '#64B5F6', '#E57373', '#FF8A65']

fig, ax = plt.subplots(figsize=(12, 5))

ax.barh(veg, num_gardeners, color=colors, alpha=0.8)
ax.set_title("Garden Veggies", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Gardeners', fontsize=14)
ax.set_ylabel('Veggies', fontsize=14)
ax.tick_params(axis='y', rotation=45, labelsize=12)
ax.tick_params(axis='x', labelsize=12)

plt.tight_layout()
plt.show()