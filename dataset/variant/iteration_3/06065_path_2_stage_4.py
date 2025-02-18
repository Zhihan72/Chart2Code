import matplotlib.pyplot as plt
import numpy as np

sectors = ["AI", "Blockchain", "IoT", "CyberSec", "Quantum"]

initial_funding = [7, 5, 10, 6, 8]  
year_end_revenue = [11, 7, 15, 10, 12]  

growth_percentage = [(rev - init) / init * 100 for init, rev in zip(initial_funding, year_end_revenue)]

fig, ax = plt.subplots(figsize=(14, 8))

bars_initial = ax.barh(np.arange(len(sectors)) - 0.2, initial_funding, height=0.4, label='Initial Fund', color='#4daf4a')
bars_revenue = ax.barh(np.arange(len(sectors)) + 0.2, year_end_revenue, height=0.4, label='Yr-End Rev', color='#377eb8')

ax.set_title('TechVille Innovation Results', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Sectors', fontsize=12)
ax.set_xlabel('Amount (M USD)', fontsize=12)
ax.set_yticks(np.arange(len(sectors)))
ax.set_yticklabels(sectors)

ax.bar_label(bars_initial, padding=3, fontsize=10)
ax.bar_label(bars_revenue, padding=3, fontsize=10)

ax2 = ax.twiny()
ax2.plot(growth_percentage, np.arange(len(sectors)), color='darkorange', marker='o', linestyle='--', linewidth=2, label='Growth %')
ax2.set_xlabel('Growth (%)', fontsize=12)
ax2.set_xlim(0, max(growth_percentage) + 10)

for i, gp in enumerate(growth_percentage):
    ax2.text(gp + 1, i, f'{gp:.1f}%', va='center', ha='left', color='darkorange', fontsize=10, fontweight='bold')

fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.95), fontsize=10)
fig.legend(loc='upper right', bbox_to_anchor=(0.9, 0.95), fontsize=10)

plt.tight_layout()
plt.show()