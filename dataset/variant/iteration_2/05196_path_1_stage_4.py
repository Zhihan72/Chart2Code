import matplotlib.pyplot as plt
import numpy as np

planets = ["Europa", "Mars", "Callisto", "Ganymede", "Venus", "Titan", "Ceres", "Moon", "Io", "Mercury"]
funding_percentages = [15, 30, 3, 7, 5, 10, 2, 15, 8, 5]
colors = ['#66b3ff', '#ff9999', '#ffb366', '#c2c2f0', '#ffcc99',
          '#ff6666', '#c2f0c2', '#99ff99', '#ffccff', '#f0e68c']

fig, ax = plt.subplots(figsize=(12, 8))

# Simplified pie chart
ax.pie(funding_percentages, labels=planets, colors=colors,
       autopct='%1.1f%%', startangle=90, textprops=dict(color="black"),
       wedgeprops=dict(width=0.4))

ax.set_title('Exploration Initiatives\nFunding Allocation 2050', 
             fontsize=16, fontweight='bold', color='green', pad=25)

ax.set_aspect('equal')

funding_amounts = [150, 300, 30, 70, 50, 100, 20, 150, 80, 50]
ax_bar = fig.add_subplot(212)
x_pos = np.arange(len(planets))
bars = ax_bar.bar(x_pos, funding_amounts, color=colors)

ax_bar.set_title('Funding Amounts Comparisons\nExploration Targets (in Billions)', fontsize=14, weight='bold')
ax_bar.set_xlabel('Targets', fontsize=12)
ax_bar.set_ylabel('Funding (Billion $)', fontsize=12)
ax_bar.set_xticks(x_pos)
ax_bar.set_xticklabels(planets, rotation=45, ha='right', fontsize=11, style='italic')

for bar in bars:
    height = bar.get_height()
    ax_bar.text(bar.get_x() + bar.get_width() / 2, height + 5, f"${height}B", ha='center', va='bottom', fontsize=10)

plt.tight_layout()

plt.show()