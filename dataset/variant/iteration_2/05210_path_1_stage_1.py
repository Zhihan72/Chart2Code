import matplotlib.pyplot as plt
import numpy as np

# Data for the year 2022: Installed capacity (in GW)
renewable_sources = ['Solar', 'Wind', 'Hydro']
capacities_2022 = np.array([850, 790, 1160])  # Corresponding capacities

# Sort the capacities in descending order
sorted_indices = np.argsort(capacities_2022)[::-1]  # Indices for sorting in descending order
sorted_sources = np.array(renewable_sources)[sorted_indices]
sorted_capacities = capacities_2022[sorted_indices]

# Create the bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(sorted_sources, sorted_capacities, color=['gold', 'skyblue', 'steelblue'], edgecolor='black')

# Annotations for bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2.0, height, f'{height}GW', ha='center', va='bottom', fontsize=10)

# Chart title and labels
plt.title('Installed Capacity of Renewable Energy Sources in 2022', fontsize=16, fontweight='bold')
plt.xlabel('Renewable Energy Sources', fontsize=12)
plt.ylabel('Installed Capacity (GW)', fontsize=12)

# Tight layout to avoid text overlap
plt.tight_layout()

# Display the plot
plt.show()