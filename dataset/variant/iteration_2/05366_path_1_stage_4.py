import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2026)

vanilla = np.array([30, 30, 29, 28, 27, 25, 24, 23, 22, 20, 18])
chocolate = np.array([20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])
strawberry = np.array([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10])
mint = np.array([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])

fig, ax = plt.subplots(figsize=(14, 7))

# Changed the order of colors to shuffle them
ax.stackplot(years, vanilla, chocolate, strawberry, mint,
             labels=['Classic Vanilla', 'Choco Delight', 'Berry', 'Minty Fresh'],
             colors=['#70a288', '#ffb347', '#af4035', '#f3cbd3'], alpha=0.85)

ax.set_title("Frozen Dessert Share Evolution (2015 - 2025)", fontsize=18, fontweight='regular', family='monospace')
ax.set_xlabel("Timeline", fontsize=12)
ax.set_ylabel("Percentage of Market (%)", fontsize=12)
plt.xticks(years, rotation=30)
plt.yticks(np.arange(0, 101, 20))

ax.legend(loc='lower right', title="Delicious Treats", fontsize=10)
ax.grid(True, linestyle='-.', alpha=0.4)

ax.annotate('Noteworthy Shift around 2020', xy=(2020, 50),
            xytext=(2021, 70), arrowprops=dict(facecolor='gray', shrink=0.05), fontsize=10,
            bbox=dict(boxstyle="square,pad=0.3", edgecolor='gray', facecolor='lightgray'))

plt.tight_layout()
plt.show()