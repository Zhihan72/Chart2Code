import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)
population = np.array([
    150, 154, 158, 165, 170, 176, 183, 190, 198, 210,
    222, 235, 248, 260, 272, 285, 297, 310, 325, 340, 355
])
household_income = np.array([
    35, 36, 38, 40, 42, 45, 48, 50, 53, 56,
    60, 63, 67, 70, 74, 78, 82, 86, 90, 94, 98
])

fig, ax = plt.subplots(figsize=(14, 8))

# Altered styles: Change colors and marker styles
ax.plot(years, population, label="Residents (in thousands)", color='green', linestyle='--', marker='x', linewidth=1.5)
ax.plot(years, household_income, label="Household Earnings (in thousands)", color='purple', linestyle='-.', marker='d', linewidth=1.5)

ax.set_title("NeoMetropolis Evolution (2000-2020)\nCitizens & Income over Time", fontsize=16, pad=20)
ax.set_xlabel("Timeline", fontsize=14)
ax.set_ylabel("Measured Figures", fontsize=14)

# Changed legend location and fontsize
ax.legend(loc='lower right', fontsize=10)
# Modified grid lines
ax.grid(True, linestyle='-', alpha=0.3)
# New set of x-ticks
ax.set_xticks(np.arange(2000, 2021, 3))

milestones = [(2005, 'Urban Plan'), (2010, 'Investment Leap'), (2015, 'Population Surge')]
for year, event in milestones:
    ax.axvline(x=year, color='orange', linestyle=':', linewidth=1, ymin=0.05, ymax=0.9)
    ax.annotate(event, 
                xy=(year, ax.get_ylim()[1]), 
                xytext=(year, ax.get_ylim()[1] * 1.05),
                arrowprops=dict(facecolor='blue', shrink=0.05, width=1),
                fontsize=9, 
                ha='center', 
                bbox=dict(boxstyle="round,pad=0.3", edgecolor='none', facecolor='white', alpha=0.7))

plt.tight_layout()
plt.show()