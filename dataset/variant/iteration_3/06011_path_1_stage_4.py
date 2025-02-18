import matplotlib.pyplot as plt
import numpy as np

regions = ['Zone 1', 'Area B', 'Sector C', 'Division D', 'Network E']
apples = [1200, 850, 1250, 950, 1100]
oranges = [900, 1200, 820, 950, 1020]
grapes = [880, 950, 1100, 1200, 980]

total_production = np.array(apples) + np.array(oranges) + np.array(grapes)

fig, ax = plt.subplots(figsize=(12, 8))

# Random stylistic changes applied here
ax.barh(regions, apples, label='Red Apples', color='red', edgecolor='black', hatch='/')
ax.barh(regions, oranges, left=apples, label='Orange Citrus', color='orange', edgecolor='black', hatch='-')
ax.barh(regions, grapes, left=np.array(apples) + np.array(oranges), label='Purple Grapes', color='purple', edgecolor='black', hatch='\\')

ax.set_title("Fruit Production Analysis by Region for 2023", fontsize=16, pad=15)
ax.set_xlabel("Production (kg)", fontsize=12)
ax.set_xlim(0, max(total_production) + 300)

# Legend style modifications
ax.legend(title="Fruit Types", loc='lower right', fontsize=10, frameon=False)

# Modified grid and border styles
ax.grid(axis='x', linestyle='-', linewidth=0.5, color='gray')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_color('purple')
ax.spines['right'].set_linewidth(1.5)

for idx, (region, total) in enumerate(zip(regions, total_production)):
    ax.text(total + 50, idx, f"{total} kg", va='center', fontsize=9)

plt.tight_layout()
plt.show()