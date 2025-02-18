import numpy as np
import matplotlib.pyplot as plt

destinations = ['Moon', 'Mars', 'Hotels']
tourists_data = np.array([
    [20, 25, 30, 35, 40],  # Moon
    [5, 10, 15, 22, 30],   # Mars
    [15, 20, 28, 36, 45],  # Hotels
])

# Calculate total tourists for each destination
total_tourists = tourists_data.sum(axis=1)

# Sort the data by total number of tourists in descending order
sorted_indices = np.argsort(total_tourists)[::-1]
sorted_destinations = np.array(destinations)[sorted_indices]
sorted_totals = total_tourists[sorted_indices]

# Plotting sorted bar chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(sorted_destinations, sorted_totals, color=['#1f77b4', '#ff7f0e', '#2ca02c'])

ax.set_xlabel('Destination', fontsize=12)
ax.set_ylabel('Total Tourists (K)', fontsize=12)
ax.set_title('Total Tourists to Each Destination (Sorted 2050-54)', fontsize=14, weight='bold')

plt.tight_layout()
plt.show()