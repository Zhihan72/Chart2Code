import matplotlib.pyplot as plt
import numpy as np

regions = ["North", "Coast", "Desert", "Urban", "Mountain"]

efficiency = np.array([
    [15, 17, 18, 20, 22], 
    [18, 19, 20, 21, 22], 
    [20, 21, 23, 25, 27], 
    [16, 18, 19, 21, 22], 
    [14, 15, 16, 17, 18]   
])

mean_efficiency = np.mean(efficiency, axis=1)

sorted_indices = np.argsort(-mean_efficiency)
sorted_regions = [regions[i] for i in sorted_indices]
sorted_efficiency = mean_efficiency[sorted_indices]

fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(sorted_regions, sorted_efficiency, color=['purple', 'orange', 'green', 'red', 'blue'])

ax.set_title('Energy Efficiency by Region (2018-2022)', fontsize=14, fontweight='bold')
ax.set_xlabel('Region', fontsize=12)
ax.set_ylabel('Avg. Efficiency (%)', fontsize=12)
ax.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()