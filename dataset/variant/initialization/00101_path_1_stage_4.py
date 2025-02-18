import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2024)
papers_published = np.array([150, 170, 190, 220, 260, 310, 400, 480, 590, 680, 820, 950, 1100, 1280])

annotations = {
    2013: "QEC",
    2017: "Q Supremacy",
    2020: "QML Boom"
}

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.scatter(years, papers_published, c=years, cmap='cool', edgecolor='black', s=100)
ax1.plot(years, papers_published, linestyle='-', color='navy', linewidth=2)

for year, label in annotations.items():
    ax1.annotate(label, 
                 (year, papers_published[year-2010]), 
                 textcoords="offset points", 
                 xytext=(-30,10), 
                 ha='center',
                 fontsize=10, 
                 bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='white', alpha=0.7),
                 arrowprops=dict(arrowstyle='->', connectionstyle="arc3", color='gray'))

ax1.set_title("Quantum Papers Published (2010-2023)", fontsize=16)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Papers Count", fontsize=12, color='navy')
ax1.tick_params(axis='y', labelcolor='navy')

ax1.set_ylim(0, 1400)
ax1.set_xlim(years.min() - 1, years.max() + 1)

plt.tight_layout()
plt.show()