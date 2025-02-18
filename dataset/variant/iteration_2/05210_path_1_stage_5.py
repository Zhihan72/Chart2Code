import matplotlib.pyplot as plt
import numpy as np

# Data for the year 2022: Installed capacity (in GW)
renewable_sources = ['Solar', 'Hydro']
capacities_2022 = np.array([850, 1160])

# Sort the capacities in descending order
sorted_indices = np.argsort(capacities_2022)[::-1]
sorted_sources = np.array(renewable_sources)[sorted_indices]
sorted_capacities = capacities_2022[sorted_indices]

# Create the bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(sorted_sources, sorted_capacities, color='steelblue', edgecolor='black')

# Display the plot
plt.show()