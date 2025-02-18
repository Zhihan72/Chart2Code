import matplotlib.pyplot as plt
import numpy as np

# Original data
countries = ['Finland', 'Norway', 'Iceland', 'Denmark', 'Netherlands', 
             'Sweden', 'Switzerland', 'Belgium', 'Canada', 'Brazil']
consumption_kg = [12, 9.9, 9, 8.7, 8.4, 8.2, 7.9, 6.8, 6.5, 6.1]

# Shuffled data - manually altered
shuffled_countries = ['Norway', 'Switzerland', 'Brazil', 'Iceland', 'Sweden', 
                      'Finland', 'Belgium', 'Canada', 'Denmark', 'Netherlands']
shuffled_consumption_kg = [9.9, 7.9, 6.1, 9, 8.2, 12, 6.8, 6.5, 8.7, 8.4]

fig, ax = plt.subplots(figsize=(12, 8))

colors = ['lightcoral', 'skyblue', 'lightgreen', 'plum', 'khaki', 
          'lightpink', 'lightyellow', 'lightgrey', 'thistle', 'lightsalmon']
edge_colors = ['darkred', 'darkblue', 'darkgreen', 'indigo', 'goldenrod', 
               'deeppink', 'darkorange', 'dimgray', 'purple', 'darkorange']
linestyles = ['-', '--', '-.', ':', (0, (3, 5, 1, 5)), (0, (1, 10)), '-', '--', '-.', ':']

bars = ax.barh(shuffled_countries, shuffled_consumption_kg, color=colors, edgecolor=edge_colors)

ax.set_title('Global Caffeine Rush:\nTop Coffee Consuming Countries in 2023', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Average Annual Coffee Consumption (kg per capita)', fontsize=11)

for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width} kg',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(3, 0),
                textcoords='offset points',
                ha='left', va='center', fontsize=9, color='darkslategray')

ax.xaxis.grid(True, linestyle=linestyles[0], linewidth=0.8, alpha=0.5)
ax.set_axisbelow(True)

ax.invert_yaxis()

ax.spines['top'].set_visible(False)
ax.spines['right'].set_linewidth(1.5)

plt.tight_layout()

plt.show()