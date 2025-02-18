import matplotlib.pyplot as plt
import numpy as np

emissions_values = [1000, 300, 150, -200, -100, -150]
final_emission = 1000 + sum(emissions_values)
emissions_values.append(final_emission - 1000)

# Sort emissions in descending order
sorted_values = sorted(emissions_values, reverse=True)

colors = ['#6da34d' if x >= 0 else '#e06c75' for x in sorted_values]

fig, ax = plt.subplots(figsize=(12, 7))

# Choose varied marker shapes and line styles
marker_styles = ['o', 'v', '^', '<', '>', 's', 'p', '*', '+', 'x']
line_styles = ['-', '--', '-.', ':']

# Randomly change edgecolor to different shades
bars = ax.bar(range(len(sorted_values)), sorted_values, color=colors, 
              edgecolor=['#2b2d42', '#3a3d54', '#4a4d64', '#5a5d74', '#6a6d84', '#7a7d94', '#8a8da4'])

plt.xticks(range(len(sorted_values)), rotation=45, ha='right', fontsize=12)
plt.grid(axis='x', linestyle=line_styles[1], alpha=0.8)  # Change grid to 'x' axis with a different style
plt.legend(['Emissions'], loc='upper right', fontsize=11, frameon=True, shadow=True)  # Add a styled legend
plt.tight_layout()

plt.show()