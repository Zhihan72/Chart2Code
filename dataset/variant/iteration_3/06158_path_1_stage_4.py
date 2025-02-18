import numpy as np
import matplotlib.pyplot as plt
from math import pi

categories = ['Flavor Variety', 'Affordability', 'Customer Service', 'Ambience', 'Quality']
N = len(categories)

shopA_scores = [8, 6, 9, 7, 8]
shopB_scores = [7, 8, 8, 6, 9]
shopC_scores = [9, 7, 7, 8, 7]
shopD_scores = [6, 9, 8, 7, 8]
shopE_scores = [8, 9, 7, 8, 8]

angles = np.linspace(0, 2 * pi, N, endpoint=False).tolist()
angles += angles[:1]

shopA_scores += shopA_scores[:1]
shopB_scores += shopB_scores[:1]
shopC_scores += shopC_scores[:1]
shopD_scores += shopD_scores[:1]
shopE_scores += shopE_scores[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

ax.plot(angles, shopA_scores, 'o--', color='#1f77b4', linewidth=1.5)
ax.plot(angles, shopB_scores, 's-.', color='#ff7f0e', linewidth=1.5)
ax.plot(angles, shopC_scores, '^:', color='#2ca02c', linewidth=1.5)
ax.plot(angles, shopD_scores, 'd-', color='#d62728', linewidth=1.5)
ax.plot(angles, shopE_scores, 'p-', color='#9467bd', linewidth=1.5)

ax.set_ylim(0, 10)

ax.grid(color='gray', linestyle='--', linewidth=0.5)
ax.spines['polar'].set_visible(True)
ax.spines['polar'].set_color('darkgrey')

plt.tight_layout()
plt.show()