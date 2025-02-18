import matplotlib.pyplot as plt
import numpy as np

energy_sources = ['Solar', 'Wind', 'Hydro', 'Nuclear', 'Geothermal', 'Fusion', 'Biomass']
current_share = [25, 20, 30, 15, 10, 0, 0]
future_share = [35, 25, 20, 15, 5, 10, 5]
experimental_share = [5, 10, 5, 5, 5, 20, 20]

fig, ax = plt.subplots(figsize=(10, 7))
bar_width = 0.25
index = np.arange(len(energy_sources))

# Apply a single color consistently across all data groups
single_color = '#4682B4'
ax.bar(index, current_share, bar_width, color=single_color, edgecolor='black')
ax.bar(index + bar_width, future_share, bar_width, color=single_color, edgecolor='black')
ax.bar(index + 2 * bar_width, experimental_share, bar_width, color=single_color, edgecolor='black')

plt.tight_layout()
plt.show()