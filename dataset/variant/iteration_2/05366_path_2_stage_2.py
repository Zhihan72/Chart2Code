import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2026)
vanilla = np.array([30, 30, 29, 28, 27, 25, 24, 23, 22, 20, 18])
chocolate = np.array([20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])
strawberry = np.array([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10])
mint = np.array([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
cookie_dough = np.array([10, 10, 11, 12, 11, 12, 13, 14, 14, 16, 17])
others = np.array([10, 10, 10, 10, 12, 13, 13, 13, 14, 14, 15])

fig, ax = plt.subplots(figsize=(14, 7))
ax.stackplot(years, vanilla, chocolate, strawberry, mint, cookie_dough, others,
             colors=['#c2c2c2', '#98ff98', '#8b4513', '#f7d8ba', '#ff6f61', '#ddadaf'], alpha=0.75)

ax.set_title("Ice Cream Market Share Trends\n (2015 - 2025)", fontsize=16, fontweight='bold', family='serif')
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Market Share (%)", fontsize=14)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 101, 10))

ax.annotate('Marked shift in market share trend (2020)', xy=(2020, 50),
            xytext=(2022, 60), arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12,
            bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='white'))

plt.tight_layout()
plt.show()