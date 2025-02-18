import matplotlib.pyplot as plt
import numpy as np

emissions_values = [1000, 300, 150, -200, -100, -150]
final_emission = 1000 + sum(emissions_values)
emissions_values.append(final_emission - 1000)

# Sort emissions in descending order
sorted_values = sorted(emissions_values, reverse=True)

colors = ['#6da34d' if x >= 0 else '#e06c75' for x in sorted_values]

fig, ax = plt.subplots(figsize=(12, 7))

bars = ax.bar(range(len(sorted_values)), sorted_values, color=colors, edgecolor='black')

plt.xticks(range(len(sorted_values)), rotation=30, ha='right', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()