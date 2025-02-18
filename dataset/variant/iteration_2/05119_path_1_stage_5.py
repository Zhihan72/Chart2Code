import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2023, 2031)

# Original datasets
ai_exhibitors = np.array([15, 20, 25, 30, 38, 42, 45, 48])
robotics_exhibitors = np.array([10, 15, 22, 28, 37, 41, 44, 47])
quantum_exhibitors = np.array([5, 8, 12, 18, 27, 32, 39, 43])
ar_exhibitors = np.array([7, 10, 14, 19, 26, 33, 37, 40])

# Positive sets expand one side (e.g., AI and Robotics)
pos_data = np.array([ai_exhibitors, robotics_exhibitors])

# Negative sets expand other side (e.g., Quantum and AR)
neg_data = np.array([-quantum_exhibitors, -ar_exhibitors])

fig, ax = plt.subplots(figsize=(14, 7))

# Plot positive datasets
ax.bar(years, pos_data[0], color='crimson', hatch='/', alpha=0.7, label='AI Exhibitors')
ax.bar(years, pos_data[1], bottom=pos_data[0], color='darkcyan', hatch='x', alpha=0.7, label='Robotics Exhibitors')

# Plot negative datasets
ax.bar(years, neg_data[0], color='goldenrod', hatch='+', alpha=0.7, label='Quantum Exhibitors')
ax.bar(years, neg_data[1], bottom=neg_data[0], color='slateblue', hatch='\\', alpha=0.7, label='AR Exhibitors')

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=10)
ax.set_yticks(np.arange(-150, 150, step=20))
ax.grid(True, axis='y', linestyle='-.', linewidth=0.6)

# Legend indicating categories
ax.legend(loc='upper right')

plt.tight_layout()
plt.show()