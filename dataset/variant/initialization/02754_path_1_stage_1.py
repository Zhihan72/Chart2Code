import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
sales = np.array([50, 70, 100, 160, 250, 400, 650, 1000, 1500, 2300, 3500])

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(years, sales, marker='o', linestyle='-', color='navy', linewidth=2, markersize=6, label='EV Sales')

ax.set_title('The Rise of Electric Vehicles:\nA Decade of Growth in Global Sales', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Sales (in thousands)', fontsize=14)

ax.grid(True, linestyle='--', alpha=0.6)

ax.annotate('Significant Growth Begins', xy=(2013, 160), xytext=(2011, 800),
            arrowprops=dict(facecolor='navy', arrowstyle='->', lw=1.5),
            fontsize=12, color='navy', bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightgrey', alpha=0.8))
ax.annotate('Exponential Increase', xy=(2018, 1500), xytext=(2016, 3000),
            arrowprops=dict(facecolor='navy', arrowstyle='->', lw=1.5),
            fontsize=12, color='navy', bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightgrey', alpha=0.8))

ax.set_xlim(2010, 2020)
ax.set_ylim(0, 4000)

ax.legend(loc='upper left', fontsize=12)

plt.tight_layout()
plt.show()