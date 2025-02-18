import matplotlib.pyplot as plt
import numpy as np

combined_data = [1.2, 1.5, 1.3, 1.4, 1.6, 1.5, 1.7, 1.8, 1.6, 1.7,
                 2.1, 2.3, 2.5, 2.2, 2.4, 2.6, 2.5, 2.7, 2.8, 2.6,
                 1.7, 1.6, 1.9, 1.8, 2.0, 1.9, 2.1, 2.2, 1.8, 2.0,
                 0.8, 1.0, 1.1, 1.2, 1.3, 1.1, 1.0, 1.2, 1.4, 1.3,
                 3.2, 3.0, 3.3, 3.5, 3.6, 3.4, 3.5, 3.6, 3.7, 3.8]

fig, ax = plt.subplots(figsize=(8, 6))

ax.boxplot(combined_data, vert=True, patch_artist=True,
           boxprops=dict(facecolor='#87CEFA', color='darkgreen'),
           whiskerprops=dict(color='darkorange'),
           capprops=dict(color='darkorange'),
           flierprops=dict(marker='^', color='darkgreen', markersize=6, alpha=0.4),
           medianprops=dict(color='darkred', linewidth=1))

ax.set_title('Park Size Dist.', fontsize=16, fontweight='heavy', pad=25)
ax.set_ylabel('Size (Sq Km)', fontsize=12, fontweight='medium')
ax.set_xticks([])
ax.grid(axis='y', linestyle='-.', alpha=0.5)

ax.spines['top'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_color('grey')
ax.spines['right'].set_color('grey')

plt.tight_layout()
plt.show()