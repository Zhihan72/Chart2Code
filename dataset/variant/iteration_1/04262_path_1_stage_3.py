import matplotlib.pyplot as plt
import numpy as np

genres = ['Fict', 'Non-Fic', 'Myst', 'Sci-Fi', 'Rom', 'Bio', 'Fan', 'Self-Help', 'Kids']

popularity_downtown = [85, 70, 65, 50, 90, 40, 75, 60, 55]
monthly_revenue_downtown = [13, 8, 6, 5, 15, 4, 10, 7, 6]
popularity_uptown = [80, 65, 60, 55, 85, 45, 70, 50, 60]
monthly_revenue_uptown = [12, 7, 5, 6, 14, 4, 9, 5, 7]

fig, axes = plt.subplots(2, 2, figsize=(18, 12))

axes[0, 0].bar(genres, popularity_downtown, color='skyblue')
axes[0, 0].set_ylabel('Pop', fontsize=12)
axes[0, 0].set_xticklabels(genres, rotation=45, ha='right')

axes[0, 1].bar(genres, monthly_revenue_downtown, color='skyblue')
axes[0, 1].set_ylabel('Rev ($K)', fontsize=12)
axes[0, 1].set_xticklabels(genres, rotation=45, ha='right')

axes[1, 0].bar(genres, popularity_uptown, color='lightgreen')
axes[1, 0].set_ylabel('Pop', fontsize=12)
axes[1, 0].set_xticklabels(genres, rotation=45, ha='right')

axes[1, 1].bar(genres, monthly_revenue_uptown, color='lightgreen')
axes[1, 1].set_ylabel('Rev ($K)', fontsize=12)
axes[1, 1].set_xticklabels(genres, rotation=45, ha='right')

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()