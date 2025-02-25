import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2020)
rainfall = np.array([870, 940, 910, 800, 960, 1140, 820, 850, 1005, 1050, 
                     1150, 950, 920, 1300, 860, 1250, 1200, 1080, 1000, 1100])

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(years, rainfall, color='blue', linewidth=2, marker='o')

annotations = {
    2003: "Drought",
    2010: "Peak",
    2018: "Climate Change"
}

for year, text in annotations.items():
    ax.annotate(text, xy=(year, rainfall[np.where(years == year)][0] + 30), 
                xytext=(10, -40), textcoords='offset points', 
                arrowprops=dict(arrowstyle='->', color='grey'),
                ha='center', fontsize=10, color='darkred', weight='bold')

ax.set_title("Rainfall in Rainville (2000-19)", fontsize=16, weight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Rainfall (mm)", fontsize=12)
ax.set_xlim(1999, 2020)
ax.set_ylim(750, 1350)

plt.tight_layout()
plt.show()