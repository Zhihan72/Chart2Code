import matplotlib.pyplot as plt
import numpy as np

sectors = ["AI", "Blockchain", "IoT", "CyberSec", "Quantum"]

initial_funding = [7, 5, 10, 6, 8]  
year_end_revenue = [11, 7, 15, 10, 12]  

growth_percentage = [(rev - init) / init * 100 for init, rev in zip(initial_funding, year_end_revenue)]

fig, ax = plt.subplots(figsize=(14, 8))

bars_initial = ax.barh(np.arange(len(sectors)), initial_funding, height=0.4, label='Initial Fund', color='skyblue', edgecolor='black')
bars_revenue = ax.barh(np.arange(len(sectors)), year_end_revenue, height=0.2, label='Yr-End Rev', color='salmon', edgecolor='grey', hatch='/')

ax.set_title('TechVille Innovation Results', fontsize=16, fontweight='bold', pad=20)
ax.set_yticks(np.arange(len(sectors)))
ax.set_yticklabels(sectors, fontsize=11)
ax.set_xlabel('Amount (M USD)', fontsize=12, color='purple')

ax.bar_label(bars_initial, padding=5, fontsize=10, color='blue', fontweight='normal')
ax.bar_label(bars_revenue, padding=5, fontsize=10, color='red', fontweight='normal')

ax2 = ax.twiny()
ax2.plot(growth_percentage, np.arange(len(sectors)), color='green', marker='^', linestyle='-', linewidth=1.5, label='Growth %')
ax2.set_xlabel('Growth (%)', fontsize=12, color='green')
ax2.set_xlim(0, max(growth_percentage) + 12)

for i, gp in enumerate(growth_percentage):
    ax2.text(gp + 1, i, f'{gp:.1f}%', va='center', ha='left', color='green', fontsize=10)

fig.legend(loc='lower right', fontsize=10)
plt.tight_layout()
plt.show()