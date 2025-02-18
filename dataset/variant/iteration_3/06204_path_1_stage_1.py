import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
# Manually shuffled mission data
usa_missions = np.array([35, 37, 30, 15, 16, 21, 33, 32, 22, 27, 18])
russia_missions = np.array([24, 22, 25, 23, 25, 20, 28, 30, 27, 24, 22])
china_missions = np.array([18, 25, 28, 12, 5, 10, 20, 15, 8, 6, 23])

# Calculate total space missions per year with changed data
total_missions = usa_missions + russia_missions + china_missions

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(years, usa_missions, label='USA', marker='o', linestyle='-', color='blue', linewidth=2, markersize=8)
ax1.plot(years, russia_missions, label='Russia', marker='d', linestyle='--', color='red', linewidth=2, markersize=8)
ax1.plot(years, china_missions, label='China', marker='s', linestyle='-.', color='green', linewidth=2, markersize=8)

ax2 = ax1.twinx()
ax2.plot(years, total_missions, label='Total Missions', color='purple', linestyle='-', marker='v', linewidth=3, markersize=10, alpha=0.6)

# Maintain titles and labels
ax1.set_title("A Decade of International Space Missions Success (2010-2020)", fontsize=18, fontweight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=14)
ax1.set_ylabel("Number of Successful Missions", fontsize=14)
ax2.set_ylabel("Total Missions", fontsize=14)

ax1.grid(True, linestyle='--', alpha=0.7)

annotations = {
    2015: 'USA exceeds previous missions',
    2018: 'Russia stable at 25+ missions',
    2020: 'China nears 30 missions'
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