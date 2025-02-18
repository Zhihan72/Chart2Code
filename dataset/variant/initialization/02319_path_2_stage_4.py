import matplotlib.pyplot as plt
import numpy as np

initial_emissions = 10000
# Manually shuffled emissions changes
emissions_changes = np.array([-1200, 300, -1500, -800, -500])

emissions_positions = np.zeros(len(emissions_changes) + 1)
emissions_positions[0] = initial_emissions
for i in range(1, len(emissions_positions)):
    emissions_positions[i] = emissions_positions[i-1] + emissions_changes[i-1]

# Manually shuffled stages
stages = [
    'Wind\nEnergy',
    'Hydroelectric\nPower',
    'Energy\nPolicies',
    'Initial\nEmissions',
    'Population\nGrowth',
    'Solar\nEnergy'
]

consistent_color = '#808080'  
colors = [consistent_color] * (len(emissions_changes) + 1)

fig, ax = plt.subplots(figsize=(14, 8))
bars = ax.bar(stages, emissions_positions, color=colors)

for i in range(1, len(emissions_positions)):
    ax.plot([i-1, i], [emissions_positions[i-1], emissions_positions[i-1]], "k--", linewidth=0.5)

for bar, pos in zip(bars, emissions_positions):
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, f"{pos:,.0f}", ha='center', va='bottom' if yval >= 0 else 'top', fontsize=10)

ax.set_title("Urban Sustainability and Its Dynamic Elements:\nA Divergent Perspective", fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Emissions Change (Metric Tons)', fontsize=12)
ax.set_xlabel('Stages of Transition', fontsize=12)

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()