import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2021)
sector_names = ['AI & Machine Learning', 'Cybersecurity', 'Blockchain', 'Cloud Computing']

# Revenue data (in billions USD)
ai_revenue = [6, 9, 12, 18, 25, 40]
cybersecurity_revenue = [15, 18, 20, 23, 30, 45]
blockchain_revenue = [1, 2, 3, 6, 9, 12]
cloud_revenue = [5, 8, 15, 22, 30, 50]

bar_width = 0.2
x_pos = np.arange(len(years))

fig, ax = plt.subplots(figsize=(14, 8))

# Using the same color for all bars (e.g., '#0072B2', a shade of blue)
uniform_color = '#0072B2'
bars1 = ax.bar(x_pos - 1.5*bar_width, ai_revenue, bar_width, label=sector_names[0], color=uniform_color)
bars2 = ax.bar(x_pos - 0.5*bar_width, cybersecurity_revenue, bar_width, label=sector_names[1], color=uniform_color)
bars3 = ax.bar(x_pos + 0.5*bar_width, blockchain_revenue, bar_width, label=sector_names[2], color=uniform_color)
bars4 = ax.bar(x_pos + 1.5*bar_width, cloud_revenue, bar_width, label=sector_names[3], color=uniform_color)

# Text annotations
for bar, y in zip(bars1, ai_revenue):
    ax.text(bar.get_x() + bar.get_width()/2, y + 1, f'{y}', ha='center', va='bottom', fontsize=9)
for bar, y in zip(bars2, cybersecurity_revenue):
    ax.text(bar.get_x() + bar.get_width()/2, y + 1, f'{y}', ha='center', va='bottom', fontsize=9)
for bar, y in zip(bars3, blockchain_revenue):
    ax.text(bar.get_x() + bar.get_width()/2, y + 1, f'{y}', ha='center', va='bottom', fontsize=9)
for bar, y in zip(bars4, cloud_revenue):
    ax.text(bar.get_x() + bar.get_width()/2, y + 1, f'{y}', ha='center', va='bottom', fontsize=9)

ax.set_xlabel('Year', fontsize=12, fontweight='bold')
ax.set_ylabel('Revenue (billion USD)', fontsize=12, fontweight='bold')
ax.set_title('Growth of Key Technology Sectors: 2015-2020', fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(x_pos)
ax.set_xticklabels(years, rotation=45, ha='right')
ax.legend(loc='upper left', fontsize=10)

ax.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax.text(4.5, 55, 'Cloud Computing shows the highest growth', fontsize=10, bbox=dict(facecolor='yellow', alpha=0.5))

plt.tight_layout()
plt.show()