import matplotlib.pyplot as plt
import numpy as np

# Data for the year 2022: Installed capacity (in GW)
renewable_sources = ['Solar', 'Wind', 'Hydro']
capacities_2022 = np.array([850, 790, 1160])  # Corresponding capacities

# Sort the capacities in descending order
sorted_indices = np.argsort(capacities_2022)[::-1]
sorted_sources = np.array(renewable_sources)[sorted_indices]
sorted_capacities = capacities_2022[sorted_indices]

# Create the bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(sorted_sources, sorted_capacities, color=['gold', 'skyblue', 'steelblue'], edgecolor='black')

# Annotations for bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2.0, height, f'{height}GW', ha='center', va='bottom', fontsize=10)

# Remove chart title and labels
plt.xticks([])  # Remove x-axis labels
plt.yticks([])  # Remove y-axis labels
plt.xlabel('')
plt.ylabel('')
plt.title('')

# Display the plot
plt.show()