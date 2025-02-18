import matplotlib.pyplot as plt
import numpy as np

months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
desert_generation = np.array([20, 22, 25, 30, 40, 45, 50, 48, 38, 35, 30, 25])
mountains_generation = np.array([50, 55, 60, 70, 80, 85, 90, 88, 78, 68, 55, 50])
urban_generation = np.array([15, 18, 20, 25, 30, 35, 38, 36, 30, 25, 20, 18])
ocean_generation = np.array([10, 12, 15, 18, 22, 25, 28, 26, 20, 18, 15, 12])

total_generation = desert_generation + mountains_generation + urban_generation + ocean_generation
desert_percentage = (desert_generation / total_generation) * 100
mountains_percentage = (mountains_generation / total_generation) * 100
urban_percentage = (urban_generation / total_generation) * 100
ocean_percentage = (ocean_generation / total_generation) * 100

fig, axs = plt.subplots(1, 2, figsize=(18, 9))

color = 'grey'  # Define the single consistent color

axs[0].fill_between(months, 0, desert_generation, color=color, alpha=0.7)
axs[0].fill_between(months, desert_generation, desert_generation + mountains_generation, color=color, alpha=0.7)
axs[0].fill_between(months, desert_generation + mountains_generation, desert_generation + mountains_generation + urban_generation, color=color, alpha=0.7)
axs[0].fill_between(months, desert_generation + mountains_generation + urban_generation, total_generation, color=color, alpha=0.7)
axs[0].set_title("Project Solstice:\nMonthly Solar Power Generation Across Terrains in 2123", fontsize=16, weight='bold', pad=20)
axs[0].set_xlabel("Months", fontsize=12)
axs[0].set_ylabel("Solar Power Generation (Gigawatts)", fontsize=12)
axs[0].set_xticks(months)
axs[0].tick_params(axis='x', rotation=45)
axs[0].set_yticks(np.arange(0, 301, 50))
axs[0].spines['top'].set_visible(False)
axs[0].spines['right'].set_visible(False)
axs[0].spines['left'].set_visible(False)
axs[0].spines['bottom'].set_visible(False)

axs[1].plot(months, desert_percentage, marker='o', linestyle='-', color=color)
axs[1].plot(months, mountains_percentage, marker='o', linestyle='-', color=color)
axs[1].plot(months, urban_percentage, marker='o', linestyle='-', color=color)
axs[1].plot(months, ocean_percentage, marker='o', linestyle='-', color=color)
axs[1].set_title("Percentage Contribution of Terrains\n to Total Solar Power Generation", fontsize=16, weight='bold', pad=20)
axs[1].set_xlabel("Months", fontsize=12)
axs[1].set_ylabel("Contribution (%)", fontsize=12)
axs[1].set_xticks(months)
axs[1].tick_params(axis='x', rotation=45)
axs[1].set_yticks(np.arange(0, 101, 20))
axs[1].spines['top'].set_visible(False)
axs[1].spines['right'].set_visible(False)
axs[1].spines['left'].set_visible(False)
axs[1].spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()