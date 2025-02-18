import matplotlib.pyplot as plt
import numpy as np

sectors = ["AI", "Blockchain", "IoT", "CyberSec", "Quantum"]

initial_funding = [7, 5, 10, 6, 8]  
year_end_revenue = [11, 7, 15, 10, 12]  

growth_percentage = [(rev - init) / init * 100 for init, rev in zip(initial_funding, year_end_revenue)]

fig, ax = plt.subplots(figsize=(14, 8))

bars_initial = ax.bar(np.arange(len(sectors)) - 0.2, initial_funding, width=0.4, label='Initial Fund', color='#4daf4a')
bars_revenue = ax.bar(np.arange(len(sectors)) + 0.2, year_end_revenue, width=0.4, label='Yr-End Rev', color='#377eb8')

ax.set_title('TechVille Innovation Results', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Sectors', fontsize=12)
ax.set_ylabel('Amount (M USD)', fontsize=12)
ax.set_xticks(np.arange(len(sectors)))
ax.set_xticklabels(sectors)

ax.bar_label(bars_initial, padding=3, fontsize=10)
ax.bar_label(bars_revenue, padding=3, fontsize=10)

ax2 = ax.twinx()
ax2.plot(np.arange(len(sectors)), growth_percentage, color='darkorange', marker='o', linestyle='--', linewidth=2, label='Growth %')
ax2.set_ylabel('Growth (%)', fontsize=12)
ax2.set_ylim(0, max(growth_percentage) + 10)

for i, gp in enumerate(growth_percentage):
    ax2.text(i, gp + 1, f'{gp:.1f}%', ha='center', va='bottom', color='darkorange', fontsize=10, fontweight='bold')

fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.95), fontsize=10)
fig.legend(loc='upper right', bbox_to_anchor=(0.9, 0.95), fontsize=10)

plt.tight_layout()
plt.show()