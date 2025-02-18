import matplotlib.pyplot as plt
import numpy as np

months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
desert_generation = np.array([50, 55, 60, 70, 80, 85, 90, 88, 78, 68, 55, 50])
mountains_generation = np.array([20, 22, 25, 30, 40, 45, 50, 48, 38, 35, 30, 25])
ocean_generation = np.array([10, 12, 15, 18, 22, 25, 28, 26, 20, 18, 15, 12])

total_generation = desert_generation + mountains_generation + ocean_generation

fig, ax = plt.subplots(figsize=(9, 9))

ax.fill_between(months, 0, desert_generation, color='red', alpha=0.6, label='Desert')
ax.fill_between(months, desert_generation, desert_generation + mountains_generation, color='green', alpha=0.6, label='Mountains')
ax.fill_between(months, desert_generation + mountains_generation, total_generation, color='orange', alpha=0.6, label='Ocean')

ax.set_xticks(months)
ax.tick_params(axis='x', rotation=30)
ax.set_yticks(np.arange(0, 251, 50))

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.legend(loc='upper left', fontsize='small')

plt.tight_layout()
plt.show()