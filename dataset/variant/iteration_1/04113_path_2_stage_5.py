import matplotlib.pyplot as plt
import numpy as np

departments = ["Dev", "Mkt", "Supp"]
dev_scores = [3, 4, 4, 5, 4, 3, 2, 3, 4, 5, 4, 3]
mkt_scores = [4, 4, 3, 4, 3, 4, 5, 4, 3, 4, 5, 4]
supp_scores = [4, 3, 4, 4, 3, 4, 3, 4, 5, 4, 3, 4]

satisfaction_data = {
    "Dev": dev_scores,
    "Mkt": mkt_scores,
    "Supp": supp_scores
}

months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

# Manually assigned new colors
colors = ['b', 'g', 'm']  # New shuffled colors corresponding to Dev, Mkt, Supp

for ax, (dept, scores), color in zip(axes[:-1], satisfaction_data.items(), colors):
    ax.plot(months, scores, marker='^', linestyle='--', color=color, label=f'{dept} Sat.')
    ax.set_title(f'{dept} Sat.', fontsize=14, fontweight='bold')
    ax.set_xlabel('Mths', fontsize=12)
    ax.set_ylabel('Score', fontsize=12)
    ax.set_ylim(1, 5.5)
    ax.grid(True, linestyle='-', linewidth=0.7, alpha=0.9)
    ax.legend(loc='lower right')

plt.suptitle("Sat. Scores by Dept.", fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()