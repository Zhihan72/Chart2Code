import matplotlib.pyplot as plt
import numpy as np

vegetables = ['Lettuce', 'Beans', 'Spinach', 'Carrots', 'Zucchini', 'Peppers', 'Cucumbers', 'Tomatoes']
gardeners = [60, 55, 65, 85, 70, 95, 100, 120]
growth = [5, 8, 3, 10, 7, 12, 14, 15]
colors = ['#81C784', '#9575CD', '#4DD0E1', '#FFD54F', '#A1887F', '#FF8A65', '#64B5F6', '#E57373']

fig, ax = plt.subplots(1, 2, figsize=(14, 6))

ax[0].bar(vegetables, gardeners, color=colors, alpha=0.8)
ax[0].tick_params(axis='x', rotation=45, labelsize=12)
ax[0].tick_params(axis='y', labelsize=12)

growth_colors = ['#76FF03' if g > 0 else '#F44336' for g in growth]
ax[1].bar(vegetables, growth, color=growth_colors, alpha=0.8)
ax[1].tick_params(axis='x', rotation=45, labelsize=12)
ax[1].tick_params(axis='y', labelsize=12)

for i, v in enumerate(growth):
    ax[1].text(i, v + (1 if v > 0 else -1), f"{v}", ha='center', va='bottom' if v > 0 else 'top', fontsize=12, color='black')

plt.tight_layout()
plt.show()