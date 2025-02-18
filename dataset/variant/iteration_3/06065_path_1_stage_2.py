import matplotlib.pyplot as plt
import numpy as np

sectors = ["AI", "Blockchain", "Internet of Things", "Cyber Security", "Quantum Computing"]
initial_funding = [10, 8, 7, 6, 5]
year_end_revenue = [15, 12, 11, 10, 7]

growth_percentage = [(rev - init) / init * 100 for init, rev in zip(initial_funding, year_end_revenue)]

fig, ax = plt.subplots(figsize=(14, 8))

# Apply a single color '#1f77b4' consistently for both initial funding and year-end revenue
bars_initial = ax.bar(np.arange(len(sectors)) - 0.2, initial_funding, width=0.4, color='#1f77b4')
bars_revenue = ax.bar(np.arange(len(sectors)) + 0.2, year_end_revenue, width=0.4, color='#1f77b4')

ax.set_title('TechVille Tech Innovation Challenge Results', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Technology Sectors', fontsize=12)
ax.set_ylabel('Amount (Million USD)', fontsize=12)
ax.set_xticks(np.arange(len(sectors)))
ax.set_xticklabels(sectors)

ax.bar_label(bars_initial, padding=3, fontsize=10)
ax.bar_label(bars_revenue, padding=3, fontsize=10)

ax2 = ax.twinx()
ax2.plot(np.arange(len(sectors)), growth_percentage, color='green', marker='o', linestyle='--', linewidth=2)
ax2.set_ylabel('Growth Percentage (%)', fontsize=12)
ax2.set_ylim(0, max(growth_percentage) + 10)

for i, gp in enumerate(growth_percentage):
    ax2.text(i, gp + 1, f'{gp:.1f}%', ha='center', va='bottom', color='green', fontsize=10, fontweight='bold')

ax.grid(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()