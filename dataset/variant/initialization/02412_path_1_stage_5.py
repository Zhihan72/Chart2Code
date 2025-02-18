import numpy as np
import matplotlib.pyplot as plt

destinations = ['Moon', 'Hotels']  # Removed 'Mars'
tourists_data = np.array([
    [20, 25, 30, 35, 40],  # Moon
    [15, 20, 28, 36, 45],  # Hotels
])

total_tourists = tourists_data.sum(axis=1)

sorted_indices = np.argsort(total_tourists)[::-1]
sorted_destinations = np.array(destinations)[sorted_indices]
sorted_totals = total_tourists[sorted_indices]

shuffled_colors = ['#1f77b4', '#ff7f0e']  # Adjusted for two destinations

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(sorted_destinations, sorted_totals, color=shuffled_colors)

ax.set_xlabel('Destination', fontsize=12)
ax.set_ylabel('Total Tourists (K)', fontsize=12)
ax.set_title('Total Tourists to Each Destination (Sorted 2050-54)', fontsize=14, weight='bold')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()