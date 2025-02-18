import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
usa_missions = np.array([35, 37, 30, 15, 16, 21, 33, 32, 22, 27, 18])
russia_missions = np.array([24, 22, 25, 23, 25, 20, 28, 30, 27, 24, 22])
china_missions = np.array([18, 25, 28, 12, 5, 10, 20, 15, 8, 6, 23])

total_missions = usa_missions + russia_missions + china_missions

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(years, usa_missions, label='USA', marker='x', linestyle='-', color='blue', linewidth=2)
ax1.plot(years, russia_missions, label='Russia', marker='^', linestyle=':', color='green', linewidth=2)
ax1.plot(years, china_missions, label='China', marker='s', linestyle='-', color='red', linewidth=2)

ax2 = ax1.twinx()
ax2.plot(years, total_missions, label='Total', color='orange', linestyle='--', marker='o', linewidth=2)

ax1.set_title("Space Missions (2010-2020)", fontsize=18, fontweight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=14)
ax1.set_ylabel("Successful Missions", fontsize=14)
ax2.set_ylabel("Total", fontsize=14)

ax1.grid(True, linestyle=':', alpha=0.5, color='grey')

annotations = {
    2015: 'Spurt',
    2020: 'Peak'
}

for year, text in annotations.items():
    ax1.annotate(text, (year, total_missions[year - 2010]),
                xytext=(15, 25), textcoords='offset points',
                arrowprops=dict(arrowstyle='->', color='black'),
                ha='center', fontsize=10, color='purple')

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right', fontsize=12, frameon=False)

ax1.set_xticks(years)
plt.tight_layout()
plt.show()