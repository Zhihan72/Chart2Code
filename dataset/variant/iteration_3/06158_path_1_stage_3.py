import numpy as np
import matplotlib.pyplot as plt
from math import pi

categories = ['Flavor Variety', 'Affordability', 'Customer Service', 'Ambience', 'Quality']
N = len(categories)

shopA_scores = [8, 6, 9, 7, 8]
shopB_scores = [7, 8, 8, 6, 9]
shopC_scores = [9, 7, 7, 8, 7]
shopD_scores = [6, 9, 8, 7, 8]
shopE_scores = [8, 9, 7, 8, 8]  # New data series for an additional shop

angles = np.linspace(0, 2 * pi, N, endpoint=False).tolist()
angles += angles[:1]

shopA_scores += shopA_scores[:1]
shopB_scores += shopB_scores[:1]
shopC_scores += shopC_scores[:1]
shopD_scores += shopD_scores[:1]
shopE_scores += shopE_scores[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each shop with varied marker types and line styles
ax.plot(angles, shopA_scores, 'o--', color='#1f77b4', linewidth=1.5, label='Ice Cream Delight')
ax.plot(angles, shopB_scores, 's-.', color='#ff7f0e', linewidth=1.5, label='Frozen Paradise')
ax.plot(angles, shopC_scores, '^:', color='#2ca02c', linewidth=1.5, label='Sweet Treat Haven')
ax.plot(angles, shopD_scores, 'd-', color='#d62728', linewidth=1.5, label='Chill & Thrill')
ax.plot(angles, shopE_scores, 'p-', color='#9467bd', linewidth=1.5, label='Cool Confections')  # Plotting the new shop

plt.xticks(angles[:-1], categories, color='black', size=11)
ax.set_ylim(0, 10)

ax.grid(color='gray', linestyle='--', linewidth=0.5)
ax.spines['polar'].set_visible(True)
ax.spines['polar'].set_color('darkgrey')

plt.title("Battle of the Ice Cream Shops:\nA Comprehensive Attribute Comparison", size=16, color='navy', y=1.1)
plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 1.1), fontsize=9, frameon=True, shadow=True, title="Ice Cream Shops")
plt.tight_layout()
plt.show()