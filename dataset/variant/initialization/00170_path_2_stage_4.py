import matplotlib.pyplot as plt
import numpy as np

# Shuffled manually emissions_values while keeping dimensional structure intact
emissions_values = [-150, 1000, 300, 150, -100, -200]
final_emission = 1000 + sum(emissions_values)
emissions_values.append(final_emission - 1000)  # append net emissions to preserve length

# Sort emissions in descending order
sorted_values = sorted(emissions_values, reverse=True)

# Adjust colors according to the shuffled emissions
colors = ['#e06c75' if x < 0 else '#6da34d' for x in sorted_values]

fig, ax = plt.subplots(figsize=(12, 7))

marker_styles = ['o', 'v', '^', '<', '>', 's', 'p', '*', '+', 'x']
line_styles = ['-', '--', '-.', ':']

# Manually shuffled edgecolors
bars = ax.bar(range(len(sorted_values)), sorted_values, color=colors, 
              edgecolor=['#3a3d54', '#7a7d94', '#4a4d64', '#2b2d42', '#5a5d74', '#8a8da4', '#6a6d84'])

plt.xticks(range(len(sorted_values)), rotation=45, ha='right', fontsize=12)
plt.grid(axis='x', linestyle=line_styles[1], alpha=0.8)
plt.legend(['Emissions'], loc='upper right', fontsize=11, frameon=True, shadow=True)
plt.tight_layout()

plt.show()