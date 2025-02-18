import matplotlib.pyplot as plt
import numpy as np

# Shuffle versions of the original data for demonstration
months = np.array(["Oct", "Feb", "Dec", "Aug", "Jul", "Jan", "Jun", "May", "Mar", "Apr", "Nov", "Sep"])
desert_generation = np.array([22, 25, 30, 48, 20, 50, 45, 35, 25, 30, 38, 40])
mountains_generation = np.array([85, 55, 60, 88, 90, 50, 80, 55, 70, 68, 78, 60])
urban_generation = np.array([20, 18, 30, 36, 38, 15, 35, 25, 20, 25, 30, 18])
ocean_generation = np.array([12, 15, 22, 26, 28, 10, 25, 18, 15, 18, 20, 15])

fig, ax = plt.subplots(figsize=(9, 9))

color = 'grey' 

ax.fill_between(months, desert_generation, desert_generation + mountains_generation, color=color, alpha=0.7)
ax.fill_between(months, desert_generation + mountains_generation, desert_generation + mountains_generation + urban_generation, color=color, alpha=0.7)
ax.fill_between(months, desert_generation + mountains_generation + urban_generation, desert_generation + mountains_generation + urban_generation + ocean_generation, color=color, alpha=0.7)
ax.set_title("Project Aster:\nYearly Solar Energy Yield by Terrain in 3123", fontsize=16, weight='bold', pad=20)
ax.set_xlabel("Time Frame", fontsize=12)
ax.set_ylabel("Energy Output (Terawatts)", fontsize=12)
ax.set_xticks(months)
ax.tick_params(axis='x', rotation=45)
ax.set_yticks(np.arange(0, 401, 50))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()