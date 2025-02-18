import numpy as np
import matplotlib.pyplot as plt
from math import pi

categories = ['Flavor Variety', 'Affordability', 'Customer Service', 'Ambience', 'Quality']
N = len(categories)

shopA_scores = [8, 6, 9, 7, 8]
shopB_scores = [7, 8, 8, 6, 9]
shopC_scores = [9, 7, 7, 8, 7]
shopD_scores = [6, 9, 8, 7, 8]

angles = np.linspace(0, 2 * pi, N, endpoint=False).tolist()
angles += angles[:1]

shopA_scores += shopA_scores[:1]
shopB_scores += shopB_scores[:1]
shopC_scores += shopC_scores[:1]
shopD_scores += shopD_scores[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each shop with filled area and remove redundant lines
ax.fill(angles, shopA_scores, color='#1f77b4', alpha=0.25, label='Ice Cream Delight')
ax.fill(angles, shopB_scores, color='#ff7f0e', alpha=0.25, label='Frozen Paradise')
ax.fill(angles, shopC_scores, color='#2ca02c', alpha=0.25, label='Sweet Treat Haven')
ax.fill(angles, shopD_scores, color='#d62728', alpha=0.25, label='Chill & Thrill')

plt.xticks(angles[:-1], categories, color='grey', size=10)
ax.set_ylim(0, 10)

plt.title("Battle of the Ice Cream Shops:\nA Comprehensive Attribute Comparison", size=15, color='black', y=1.1)
plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1.15), fontsize=10, frameon=False, title="Shops")
plt.tight_layout()
plt.show()