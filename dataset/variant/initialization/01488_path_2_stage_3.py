import matplotlib.pyplot as plt
import numpy as np

decades = np.arange(1500, 1600, 10)

ruff_collars = [10, 15, 25, 35, 50, 60, 75, 85, 90, 95]
puffed_sleeves = [5, 20, 40, 55, 65, 70, 65, 50, 35, 25]

fig, ax = plt.subplots(figsize=(12, 7))
single_color = '#1f78b4'

ax.plot(decades, ruff_collars, marker='o', linestyle='-', color=single_color, linewidth=2.5, label='Elaborate Collars')
ax.fill_between(decades, ruff_collars, color=single_color, alpha=0.1)

ax.plot(decades, puffed_sleeves, marker='s', linestyle='--', color=single_color, linewidth=2.5, label='Balloon Sleeves')
ax.fill_between(decades, puffed_sleeves, color=single_color, alpha=0.1)

for decade in decades:
    ax.axvline(x=decade, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

for i, (decade, rc, ps) in enumerate(zip(decades, ruff_collars, puffed_sleeves)):
    ax.annotate(str(rc), (decade, rc), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=8, color=single_color)
    ax.annotate(str(ps), (decade, ps), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=8, color=single_color)

ax.set_title('Historic Fashion Peaks\nDuring the 16th Century', fontsize=16, fontweight='bold', y=1.05)
ax.set_xlabel('Years', fontsize=14)
ax.set_ylabel('Trendiness Score', fontsize=14)
ax.set_xticks(decades)
ax.set_yticks(np.arange(0, 101, 10))
ax.grid(which='major', axis='both', linestyle='--', linewidth=0.75, alpha=0.6)

ax.legend(title='Apparel Types', loc='upper left', fontsize=12)

fig.tight_layout()
plt.show()