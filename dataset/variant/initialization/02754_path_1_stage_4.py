import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
ev_sales = np.array([50, 70, 100, 160, 250, 400, 650, 1000, 1500, 2300, 3500])
hybrid_sales = np.array([30, 40, 60, 90, 150, 220, 330, 480, 700, 1100, 1700])

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(years, ev_sales, marker='^', linestyle='-.', color='darkorange', linewidth=2, markersize=8, label='EV')
ax.plot(years, hybrid_sales, marker='v', linestyle=':', color='deepskyblue', linewidth=3, markersize=7, label='Hybrid')

ax.set_title('Rise of EVs & Hybrids: Sales Growth', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Yr', fontsize=14)
ax.set_ylabel('Sales (k)', fontsize=14)

ax.grid(True, linestyle='-', color='grey', alpha=0.3)

ax.annotate('Growth Begins', xy=(2013, 160), xytext=(2011, 800),
            arrowprops=dict(facecolor='darkorange', arrowstyle='->', lw=1.5),
            fontsize=12, color='darkorange', bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightgrey', alpha=0.8))
ax.annotate('Exponential Rise', xy=(2018, 1500), xytext=(2016, 3000),
            arrowprops=dict(facecolor='darkorange', arrowstyle='->', lw=1.5),
            fontsize=12, color='darkorange', bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightgrey', alpha=0.8))

for spine in ax.spines.values():
    spine.set_edgecolor('darkgrey')
    spine.set_linewidth(2)

ax.set_xlim(2010, 2020)
ax.set_ylim(0, 4000)

ax.legend(loc='lower right', fontsize=12, frameon=True, shadow=True, facecolor='lightgoldenrodyellow', edgecolor='grey')

plt.tight_layout()
plt.show()