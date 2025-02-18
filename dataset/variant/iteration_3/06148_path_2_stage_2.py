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

ax.plot(years, population, label="Residents (in thousands)", color='blue', linestyle='-', marker='o', linewidth=2)
ax.plot(years, household_income, label="Household Earnings (in thousands)", color='red', linestyle='-', marker='^', linewidth=2)

ax.set_title("NeoMetropolis Evolution (2000-2020)\nCitizens & Income over Time", fontsize=16, pad=20)
ax.set_xlabel("Timeline", fontsize=14)
ax.set_ylabel("Measured Figures", fontsize=14)

ax.legend(loc='upper left', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_xticks(np.arange(2000, 2021, 2))

milestones = [(2005, 'Urban Plan'), (2010, 'Investment Leap'), (2015, 'Population Surge')]
for year, event in milestones:
    ax.axvline(x=year, color='grey', linestyle='--', linewidth=1.5, ymin=0.05, ymax=0.9)
    ax.annotate(event, 
                xy=(year, ax.get_ylim()[1]), 
                xytext=(year, ax.get_ylim()[1] * 1.1),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1),
                fontsize=10, 
                ha='center', 
                bbox=dict(boxstyle="round,pad=0.3", edgecolor='none', facecolor='lightgrey', alpha=0.5))

plt.tight_layout()
plt.show()