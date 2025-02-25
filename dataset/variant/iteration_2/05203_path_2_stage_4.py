import matplotlib.pyplot as plt
import numpy as np

cities = ['Chicago', 'Los Angeles', 'New York', 'Houston', 'Phoenix']
total_emissions = [1080, 1155, 1230, 1285, 980]
colors = ['#2ca02c', '#ff7f0e', '#1f77b4', '#d62728', '#9467bd']

fig, ax = plt.subplots(figsize=(10, 6))

ax.barh(cities, total_emissions, color=colors)

ax.set_xlabel('Total CO2 Emissions (metric tons)')
ax.set_ylabel('Cities')

plt.tight_layout()
plt.show()