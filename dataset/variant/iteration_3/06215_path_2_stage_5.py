import matplotlib.pyplot as plt
import numpy as np

cities = ['Chicago', 'New York', 'Los Angeles']

electricity_cost = [150, 135, 145]
water_cost = [50, 55, 45]

# Calculate means for each city to offset the bars correctly
means = [np.mean([e, w]) for e, w in zip(electricity_cost, water_cost)]

# Calculate offsets to position the bars from a central point (mean)
elec_offsets = [e - m for e, m in zip(electricity_cost, means)]
water_offsets = [w - m for w, m in zip(water_cost, means)]

index = np.arange(len(cities))
bar_width = 0.4

fig, ax = plt.subplots(figsize=(14, 8))

ax.barh(index, elec_offsets, bar_width, label='Electricity Cost', color='#1f77b4')
ax.barh(index, water_offsets, bar_width, left=elec_offsets, label='Water Cost', color='#ff7f0e')

ax.set_yticks(index)
ax.set_yticklabels(cities)
ax.set_xlabel('Deviation from Mean Cost per Month (in USD)', fontsize=12)
ax.set_title('2023 Utility Costs Divergence in Urban Areas', fontsize=16, fontweight='bold')
ax.axvline(0, color='black', linewidth=0.8)  # Central axis

# Add data labels
for i in range(len(cities)):
    ax.text(elec_offsets[i]/2, i, f'${electricity_cost[i]:.0f}', ha='center', va='center', fontsize=10, color='white')
    ax.text(elec_offsets[i] + water_offsets[i]/2, i, f'${water_cost[i]:.0f}', ha='center', va='center', fontsize=10, color='white')

ax.legend()

plt.tight_layout()
plt.show()