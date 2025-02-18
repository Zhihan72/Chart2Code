import matplotlib.pyplot as plt
import numpy as np

regions = ['Zone 1', 'Area B', 'Sector C', 'Division D', 'Network E']
apples = [1200, 850, 1250, 950, 1100]
oranges = [900, 1200, 820, 950, 1020]
grapes = [880, 950, 1100, 1200, 980]

total_production = np.array(apples) + np.array(oranges) + np.array(grapes)

fig, ax = plt.subplots(figsize=(12, 8))

# Applying a single color consistently across all data groups
consistent_color = '#4682B4'
ax.barh(regions, apples, label='Red Apples', color=consistent_color)
ax.barh(regions, oranges, left=apples, label='Orange Citrus', color=consistent_color)
ax.barh(regions, grapes, left=np.array(apples) + np.array(oranges), label='Purple Grapes', color=consistent_color)

ax.set_title("Yearly Fruit Yield in Different Areas\nAnalyzing Apples, Oranges, and Grapes in 2023", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Output in Kilograms (kg)", fontsize=12)
ax.set_ylabel("Areas", fontsize=12)
ax.set_xlim(0, max(total_production) + 300)

ax.legend(title="Fruit Categories", loc='upper right')
ax.grid(axis='x', linestyle='--', alpha=0.7)

for idx, (region, total) in enumerate(zip(regions, total_production)):
    ax.text(total + 50, idx, f"{total} kgs", va='center', ha='left', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()