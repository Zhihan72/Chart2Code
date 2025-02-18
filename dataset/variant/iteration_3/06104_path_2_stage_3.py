import matplotlib.pyplot as plt
import numpy as np

energy_sources = ['Solar', 'Wind', 'Hydro', 'Nuclear', 'Geothermal', 'Fusion', 'Biomass']
current_share = [25, 20, 30, 15, 10, 0, 0]
future_share = [35, 25, 20, 15, 5, 10, 5]
experimental_share = [5, 10, 5, 5, 5, 20, 20]

colors = ['#FFD700', '#00BFFF', '#32CD32', '#FFA07A', '#8A2BE2', '#FF4500', '#7FFF00']

fig, ax = plt.subplots(figsize=(10, 7))
bar_width = 0.25
index = np.arange(len(energy_sources))

rects1 = ax.bar(index, current_share, bar_width, color=colors, edgecolor='black')
rects2 = ax.bar(index + bar_width, future_share, bar_width, color='#ADD8E6', edgecolor='black')
rects3 = ax.bar(index + 2 * bar_width, experimental_share, bar_width, color='#FF6347', edgecolor='black')

# Removed title, xlabel, ylabel, xticks, xticklabels, and legend

plt.tight_layout()
plt.show()