import numpy as np
import matplotlib.pyplot as plt
from math import pi

categories = ['Flavor Variety', 'Affordability', 'Customer Service', 'Ambience', 'Quality']
N = len(categories)

shopA_scores = [7, 8, 8, 9, 6]
shopB_scores = [6, 9, 7, 8, 8]
shopC_scores = [8, 7, 9, 7, 7]
shopD_scores = [8, 6, 9, 8, 7]

angles = np.linspace(0, 2 * pi, N, endpoint=False).tolist()
angles += angles[:1]

shopA_scores += shopA_scores[:1]
shopB_scores += shopB_scores[:1]
shopC_scores += shopC_scores[:1]
shopD_scores += shopD_scores[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

ax.fill(angles, shopA_scores, color='#1f77b4', alpha=0.25, label="Shop A")
ax.fill(angles, shopB_scores, color='#ff7f0e', alpha=0.25, label="Shop B")
ax.fill(angles, shopC_scores, color='#2ca02c', alpha=0.25, label="Shop C")
ax.fill(angles, shopD_scores, color='#d62728', alpha=0.25, label="Shop D")

ax.set_ylim(0, 10)
ax.xaxis.grid(False)
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
plt.tight_layout()
plt.show()