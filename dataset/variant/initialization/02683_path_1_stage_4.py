import matplotlib.pyplot as plt
import numpy as np

months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
desert_generation = np.array([50, 55, 60, 70, 80, 85, 90, 88, 78, 68, 55, 50])
mountains_generation = np.array([20, 22, 25, 30, 40, 45, 50, 48, 38, 35, 30, 25])
urban_generation = np.array([15, 18, 20, 25, 30, 35, 38, 36, 30, 25, 20, 18])
ocean_generation = np.array([10, 12, 15, 18, 22, 25, 28, 26, 20, 18, 15, 12])

total_generation = desert_generation + mountains_generation + urban_generation + ocean_generation

fig, ax = plt.subplots(figsize=(9, 9))

ax.fill_between(months, 0, desert_generation, color='red', alpha=0.6, label='Desert')
ax.fill_between(months, desert_generation, desert_generation + mountains_generation, color='green', alpha=0.6, label='Mountains')
ax.fill_between(months, desert_generation + mountains_generation, desert_generation + mountains_generation + urban_generation, color='purple', alpha=0.6, label='Urban')
ax.fill_between(months, desert_generation + mountains_generation + urban_generation, total_generation, color='orange', alpha=0.6, label='Ocean')

ax.grid(False)  # Disable the grid for stylistic variation
ax.set_xticks(months)
ax.tick_params(axis='x', rotation=30)  # Changed rotation for visual variety
ax.set_yticks(np.arange(0, 301, 50))

ax.spines['top'].set_visible(False)  # Hide the top border
ax.spines['right'].set_visible(False) # Hide the right border

ax.legend(loc='upper left', fontsize='small')  # Add a legend with labels

plt.tight_layout()
plt.show()