import matplotlib.pyplot as plt
import numpy as np

initial_emissions = 10000
emissions_changes = np.array([
    -1500, 
    -1200, 
    -800,   
    -500,   
    300     
])

emissions_positions = np.zeros(len(emissions_changes) + 1)
emissions_positions[0] = initial_emissions
for i in range(1, len(emissions_positions)):
    emissions_positions[i] = emissions_positions[i-1] + emissions_changes[i-1]

colors = ['#4CAF50' if x < 0 else '#FF5733' for x in emissions_changes]
colors = ['#808080'] + colors

fig, ax = plt.subplots(figsize=(14, 8))
bars = ax.bar(range(len(emissions_positions)), emissions_positions, color=colors, edgecolor='black')

for i in range(1, len(emissions_positions)):
    ax.plot([i-1, i], [emissions_positions[i-1], emissions_positions[i-1]], "k--", linewidth=0.5)

for bar, pos in zip(bars, emissions_positions):
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, f"{pos:,.0f}", ha='center', va='bottom' if yval >= 0 else 'top', fontsize=10)

plt.xticks(rotation=45, ha='right')

# Removing textual elements such as title, x and y labels
ax.set_title("")
ax.set_ylabel('')
ax.set_xlabel('')

plt.tight_layout()
plt.show()