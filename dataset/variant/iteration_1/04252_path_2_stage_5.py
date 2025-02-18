import matplotlib.pyplot as plt
import numpy as np

energy_sources = ['Coal', 'Natural Gas', 'Nuclear', 'Hydroelectric', 'Solar', 'Wind']
cost = [65, 50, 112, 30, 50, 40]
capacity = [1000, 800, 400, 500, 300, 450]

# Sorting based on cost
sorted_indices = np.argsort(cost)[::-1]
energy_sources = [energy_sources[i] for i in sorted_indices]
cost = [cost[i] for i in sorted_indices]
capacity = [capacity[i] for i in sorted_indices]

fig, ax1 = plt.subplots(figsize=(14, 8))

color2 = 'mediumseagreen'
ax1.bar(energy_sources, cost, color=color2, alpha=0.8, width=0.3, align='edge', hatch='\\')
ax1.tick_params(axis='y', width=2)
ax1.tick_params(axis='x', bottom=False, labelbottom=False)  # Remove x-axis ticks

ax2 = ax1.twinx()
color3 = 'gold'
ax2.bar(energy_sources, capacity, color=color3, alpha=0.8, width=0.3, align='center', hatch='o')
ax2.tick_params(axis='y', width=2)

fig.tight_layout()

plt.show()