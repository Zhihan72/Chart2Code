import matplotlib.pyplot as plt
import numpy as np

vegetables = ['Tomatoes', 'Carrots', 'Lettuce', 'Peppers', 'Cucumbers', 'Zucchini', 'Spinach', 'Beans']
gardeners = [70, 100, 55, 120, 65, 85, 95, 60]
growth = [12, 8, 14, 15, 5, 3, 7, 10]

# Shuffled colors for the bars
colors = ['#81C784', '#9575CD', '#FFD54F', '#4DD0E1', '#A1887F', '#64B5F6', '#E57373', '#FF8A65']

fig, ax = plt.subplots(2, 1, figsize=(12, 10))

ax[0].barh(vegetables, gardeners, color=colors, alpha=0.8)
ax[0].set_title("Community Gardeners' Favorite Vegetables", fontsize=16, fontweight='bold', pad=20)
ax[0].set_xlabel('Number of Gardeners', fontsize=14)
ax[0].set_ylabel('Vegetable Types', fontsize=14)
ax[0].tick_params(axis='y', rotation=45, labelsize=12)
ax[0].tick_params(axis='x', labelsize=12)

growth_colors = ['#76FF03' if g > 0 else '#F44336' for g in growth]
ax[1].barh(vegetables, growth, color=growth_colors, alpha=0.8)
ax[1].set_title("Growth in the Number of Gardeners Over the Past Year", fontsize=16, fontweight='bold', pad=20)
ax[1].set_xlabel('Growth in Number of Gardeners', fontsize=14)
ax[1].set_ylabel('Vegetable Types', fontsize=14)
ax[1].tick_params(axis='y', rotation=45, labelsize=12)
ax[1].tick_params(axis='x', labelsize=12)

for i, v in enumerate(growth):
    ax[1].text(v + (1 if v > 0 else -1), i, f"{v}", va='center', ha='left' if v > 0 else 'right', fontsize=12, color='black')

plt.tight_layout()
plt.show()