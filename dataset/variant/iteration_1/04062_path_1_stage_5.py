import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2018, 2023)

apples_production = [135, 150, 120, 140, 130]
bananas_production = [100, 90, 110, 95, 105]
oranges_production = [125, 130, 115, 110, 120]

bar_height = 0.25

r1 = np.arange(len(years))
r2 = [x + bar_height for x in r1]
r3 = [x + bar_height for x in r2]

fig, ax = plt.subplots(figsize=(12, 7))

# Plot horizontal bars with altered styles
ax.barh(r1, apples_production, color='skyblue', height=bar_height, edgecolor='black', hatch='x')
ax.barh(r2, bananas_production, color='pink', height=bar_height, edgecolor='black', hatch='//')
ax.barh(r3, oranges_production, color='lightgreen', height=bar_height, edgecolor='black', hatch='.')

# Adding altered grid style
ax.grid(axis='x', linestyle='-.', alpha=0.3)

# Adding a legend with altered position
ax.legend(['Apples', 'Bananas', 'Oranges'], loc='upper right')

plt.tight_layout()
plt.show()