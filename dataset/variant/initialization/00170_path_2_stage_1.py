import matplotlib.pyplot as plt
import numpy as np

emissions_values = [1000, 300, 150, -200, -100, -150]
final_emission = 1000 + sum(emissions_values)
emissions_values.append(final_emission - 1000)

emissions_start = np.zeros(len(emissions_values))
emissions_start[1:] = np.cumsum(emissions_values[:-1])

colors = ['#6da34d' if x >= 0 else '#e06c75' for x in emissions_values]

fig, ax = plt.subplots(figsize=(12, 7))

bars = ax.bar(range(len(emissions_values)), emissions_values, bottom=emissions_start, color=colors, edgecolor='black')

for i in range(1, len(emissions_values)):
    ax.plot([i - 1, i], [emissions_start[i], emissions_start[i]], color='black', linestyle='-', linewidth=0.5)

plt.xticks(rotation=30, ha='right', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()