import matplotlib.pyplot as plt
import numpy as np

months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
desert_generation = np.array([20, 22, 25, 30, 40, 45, 50, 48, 38, 35, 30, 25])
mountains_generation = np.array([50, 55, 60, 70, 80, 85, 90, 88, 78, 68, 55, 50])
urban_generation = np.array([15, 18, 20, 25, 30, 35, 38, 36, 30, 25, 20, 18])
ocean_generation = np.array([10, 12, 15, 18, 22, 25, 28, 26, 20, 18, 15, 12])

fig, ax = plt.subplots(figsize=(9, 9))

color = 'grey'  # Define the single consistent color

ax.fill_between(months, desert_generation, desert_generation + mountains_generation, color=color, alpha=0.7)
ax.fill_between(months, desert_generation + mountains_generation, desert_generation + mountains_generation + urban_generation, color=color, alpha=0.7)
ax.fill_between(months, desert_generation + mountains_generation + urban_generation, desert_generation + mountains_generation + urban_generation + ocean_generation, color=color, alpha=0.7)
ax.set_title("Project Solstice:\nMonthly Solar Power Generation Across Terrains in 2123", fontsize=16, weight='bold', pad=20)
ax.set_xlabel("Months", fontsize=12)
ax.set_ylabel("Solar Power Generation (Gigawatts)", fontsize=12)
ax.set_xticks(months)
ax.tick_params(axis='x', rotation=45)
ax.set_yticks(np.arange(0, 301, 50))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()