import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2023, 2031)

ai_exhibitors = [15, 20, 25, 30, 38, 42, 45, 48]
robotics_exhibitors = [10, 15, 22, 28, 37, 41, 44, 47]
quantum_exhibitors = [5, 8, 12, 18, 27, 32, 39, 43]
ar_exhibitors = [7, 10, 14, 19, 26, 33, 37, 40]

robotics_cumulative = np.array(ai_exhibitors) + np.array(robotics_exhibitors)
quantum_cumulative = robotics_cumulative + np.array(quantum_exhibitors)
ar_cumulative = quantum_cumulative + np.array(ar_exhibitors)

fig, ax = plt.subplots(figsize=(14, 7))

ax.bar(years, ai_exhibitors, color='crimson', hatch='/', alpha=0.7)
ax.bar(years, robotics_exhibitors, bottom=ai_exhibitors, color='darkcyan', hatch='x', alpha=0.7)
ax.bar(years, quantum_exhibitors, bottom=robotics_cumulative, color='goldenrod', hatch='+', alpha=0.7)
ax.bar(years, ar_exhibitors, bottom=quantum_cumulative, color='slateblue', hatch='\\', alpha=0.7)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=10)
ax.set_yticks(np.arange(0, 150, step=20))
ax.grid(True, axis='y', linestyle='-.', linewidth=0.6)

plt.tight_layout()

plt.show()