import matplotlib.pyplot as plt
import numpy as np

vitamin_intake = np.array([55, 75, 85, 95, 110, 130, 150, 165, 180, 200, 220, 240, 260, 280, 300])
energy_levels = np.array([3, 4, 4, 5, 6, 5, 7, 6, 8, 7, 8, 9, 8, 9, 10])

bins = [50, 100, 150, 200, 250, 300]
bin_indices = np.digitize(vitamin_intake, bins)
average_energy_levels = [np.mean(energy_levels[bin_indices == i]) for i in range(1, len(bins))]

sorted_indices = np.argsort(average_energy_levels)
sorted_average_energy_levels = np.array(average_energy_levels)[sorted_indices]

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Plot the sorted bar chart without text
axes[0].bar(sorted_indices, sorted_average_energy_levels, color='skyblue', alpha=0.8)
axes[0].set_ylim(min(average_energy_levels) - 1, max(average_energy_levels) + 1)

# Plot the scatter plot without text
axes[1].scatter(vitamin_intake, energy_levels, color='orange', s=100, alpha=0.75)
axes[1].set_xlim(min(vitamin_intake) - 10, max(vitamin_intake) + 10)
axes[1].set_ylim(min(energy_levels) - 1, max(energy_levels) + 1)

plt.tight_layout()
plt.show()