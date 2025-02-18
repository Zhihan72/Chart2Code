import matplotlib.pyplot as plt
import numpy as np

decades = np.arange(1500, 1600, 10)
ruff_collars = [10, 15, 25, 35, 50, 60, 75, 85, 90, 95]
brocade_fabrics = [20, 30, 35, 45, 55, 65, 75, 80, 85, 90]

fig, ax = plt.subplots(figsize=(12, 7))

colors = ['#e31a1c', '#1f78b4']

ax.plot(decades, ruff_collars, marker='o', linestyle='-', color=colors[1], linewidth=2.5)
ax.fill_between(decades, ruff_collars, color=colors[1], alpha=0.1)

ax.plot(decades, brocade_fabrics, marker='^', linestyle=':', color=colors[0], linewidth=2.5)
ax.fill_between(decades, brocade_fabrics, color=colors[0], alpha=0.1)

for i, (decade, rc, bf) in enumerate(zip(decades, ruff_collars, brocade_fabrics)):
    ax.annotate(str(rc), (decade, rc), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=8, color=colors[1])
    ax.annotate(str(bf), (decade, bf), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=8, color=colors[0])

ax.set_title('Renaissance Fashion Trends\nThrough the Decades: 1500s to 1590s', fontsize=16, fontweight='bold', y=1.05)
ax.set_xlabel('Decades', fontsize=14)
ax.set_ylabel('Popularity Index', fontsize=14)
ax.set_xticks(decades)
ax.set_yticks(np.arange(0, 101, 10))

fig.tight_layout()
plt.show()