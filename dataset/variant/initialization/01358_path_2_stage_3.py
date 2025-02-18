import matplotlib.pyplot as plt
import numpy as np

regions = ["Northern Region", "Coastal Region", "Desert Region", "Urban Region"]

# Calculate the mean efficiency for each region
mean_efficiency = np.mean([[18, 15, 22, 17, 20],
                           [21, 18, 22, 19, 20],
                           [27, 23, 25, 21, 20],
                           [21, 16, 22, 18, 19]], axis=1)

# Sort the regions based on mean efficiency
sorted_indices = np.argsort(mean_efficiency)  # Ascending order
# sorted_indices = np.argsort(mean_efficiency)[::-1]  # Descending order for reverse

# Sort data based on the sorted indices
sorted_mean_efficiency = mean_efficiency[sorted_indices]
sorted_regions = [regions[i] for i in sorted_indices]

fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(sorted_regions, sorted_mean_efficiency, color=['blue', 'green', 'orange', 'red'])

ax.set_title('Average Efficiency of Renewable Energy Adoption\nAcross Regions (2018-2022)',
             fontsize=14, fontweight='bold')
ax.set_xlabel('Region', fontsize=12)
ax.set_ylabel('Average Efficiency (%)', fontsize=12)

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()