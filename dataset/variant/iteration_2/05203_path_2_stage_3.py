import matplotlib.pyplot as plt
import numpy as np

cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
total_emissions = [1230, 1155, 1080, 1285, 980]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

fig, ax = plt.subplots(figsize=(10, 6))

ax.barh(cities, total_emissions, color=colors)

ax.set_xlabel('Total CO2 Emissions (metric tons)')
ax.set_ylabel('Cities')

plt.tight_layout()
plt.show()