import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2018, 2023)
action = np.array([500, 550, 600, 650, 700])
comedy = np.array([300, 310, 320, 330, 340])
drama = np.array([400, 450, 460, 470, 480])
animation = np.array([150, 160, 170, 180, 190])

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#9467bd']

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.15
x_indices = np.arange(len(years))

ax.bar(x_indices - bar_width, action, width=bar_width, color=colors[0], alpha=0.85, label='Actn')
ax.bar(x_indices, comedy, width=bar_width, color=colors[1], alpha=0.85, label='Cmdy')
ax.bar(x_indices + bar_width, drama, width=bar_width, color=colors[2], alpha=0.85, label='Drma')
ax.bar(x_indices + 2*bar_width, animation, width=bar_width, color=colors[3], alpha=0.85, label='Anim')

ax.set_title('Movie Rev. (2018-22)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Yr', fontsize=14, labelpad=10)
ax.set_ylabel('Rev. (in M USD)', fontsize=14, labelpad=10)

ax.set_xticks(x_indices)
ax.set_xticklabels(years, rotation=45, ha='right')
ax.legend(title="Genre")

plt.tight_layout()
plt.show()