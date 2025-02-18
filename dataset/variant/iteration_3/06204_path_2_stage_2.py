import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
# Shuffling the contents of the mission arrays
usa_missions = np.array([37, 30, 15, 27, 33, 22, 21, 16, 35, 18, 32])
russia_missions = np.array([25, 30, 22, 23, 20, 24, 24, 22, 28, 27, 25])
china_missions = np.array([5, 10, 20, 8, 12, 28, 18, 6, 15, 23, 25])

total_missions = usa_missions + russia_missions + china_missions

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(years, usa_missions, label='USA', marker='o', linestyle='-', color='orange', linewidth=2, markersize=8)
ax1.plot(years, russia_missions, label='Russia', marker='d', linestyle='--', color='magenta', linewidth=2, markersize=8)
ax1.plot(years, china_missions, label='China', marker='s', linestyle='-.', color='cyan', linewidth=2, markersize=8)

ax2 = ax1.twinx()
ax2.plot(years, total_missions, label='Total Missions', color='gray', linestyle='-', marker='v', linewidth=3, markersize=10, alpha=0.6)

ax1.set_title("A Decade of International Space Missions Success (2010-2020)", fontsize=18, fontweight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=14)
ax1.set_ylabel("Number of Successful Missions", fontsize=14)
ax2.set_ylabel("Total Missions", fontsize=14)

ax1.grid(True, linestyle='--', alpha=0.7)

annotations = {
    2015: 'USA surpasses 20 missions',
    2018: 'China reaches 20 missions',
    2020: 'Total missions peak'
}

for year, text in annotations.items():
    ax1.annotate(text, (year, total_missions[year - 2010]),
                xytext=(5, 30), textcoords='offset points',
                arrowprops=dict(arrowstyle='->', color='black'),
                ha='center', fontsize=10, color='brown')

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=10)

ax1.set_xticks(years)

plt.tight_layout()

plt.show()