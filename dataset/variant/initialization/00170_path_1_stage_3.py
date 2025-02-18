import matplotlib.pyplot as plt
import numpy as np

emissions_labels = [
    'Initial Emissions', 'Industrial Growth', 'Increased Vehicle Use',
    'Green Technology Subsidy', 'Renewable Energy Adoption', 
    'Urban Area Compaction', 'Tree Planting', 'Energy Efficiency Programs', 
    'Final Emissions'
]
emissions_values = [1000, 300, 150, -180, -200, -70, -100, -150]
final_emission = 1000 + sum(emissions_values)

emissions_values.append(final_emission - 1000)

emissions_start = np.zeros(len(emissions_values))
emissions_start[1:] = np.cumsum(emissions_values[:-1])

# Updated color set
colors = ['#FF5733' if x >= 0 else '#1F618D' for x in emissions_values]

fig, ax = plt.subplots(figsize=(12, 7))

bars = ax.bar(emissions_labels, emissions_values, bottom=emissions_start, color=colors)

for i in range(1, len(emissions_values)):
    ax.plot([i - 1, i], [emissions_start[i], emissions_start[i]], color='black', linestyle='-', linewidth=0.5)

ax.set_title('Annual Carbon Emissions in EcoVille\nImpact of Activities and Initiatives', fontsize=16, pad=20)
ax.set_ylabel('Carbon Emissions (Metric Tons)', fontsize=12)
ax.set_xlabel('Emission Activities and Reductions', fontsize=12)

for i, (bar, value) in enumerate(zip(bars, emissions_values)):
    yval = bar.get_height() + emissions_start[i]
    ax.text(bar.get_x() + bar.get_width() / 2, yval + (10 if value >= 0 else -15), f'{yval:.0f}', 
            ha='center', va='bottom' if value >= 0 else 'top', color='black', fontsize=10, weight='bold')

plt.xticks(rotation=30, ha='right', fontsize=10)

plt.show()