import matplotlib.pyplot as plt
import numpy as np

# Data for the transport modes and adoption rates
transport_modes = ['Beam Movers', 'Planar Transporters', 'Levitation Rails', 'Robot Coaches', 'Skyward Autos']
adoption_rates = np.array([60, 90, 150, 80, 120])
colors = ['#4682b4', '#32cd32', '#ff69b4', '#6a5acd', '#ff8c00']

# Sort the data in descending order of adoption rates
sorted_indices = np.argsort(adoption_rates)[::-1]
transport_modes_sorted = [transport_modes[i] for i in sorted_indices]
adoption_rates_sorted = adoption_rates[sorted_indices]
colors_sorted = [colors[i] for i in sorted_indices]

x_positions = np.arange(len(transport_modes_sorted))

# Plot the sorted bar chart
fig, ax = plt.subplots(figsize=(12, 7))
ax.bar(x_positions, adoption_rates_sorted, color=colors_sorted, width=0.6)

# Titles and labels
ax.set_xlabel('Types of Transit', fontsize=14)
ax.set_ylabel('Engagement Levels (in thousands)', fontsize=14)

# Assign the x-ticks and labels
ax.set_xticks(x_positions)
ax.set_xticklabels(transport_modes_sorted, fontsize=12, rotation=30, ha='right')

# Annotate bars
for i, yval in enumerate(adoption_rates_sorted):
    ax.text(i, yval + 2, f'{yval}K', ha='center', va='bottom', fontsize=12, fontweight='bold')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()